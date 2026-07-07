import cv2
import torch
import base64
import time
import os
from ultralytics import YOLO


class AiStreamService:
    _model = None
    _target_label = ""   # 현재 감시할 객체명 저장
    _device = 'cuda' if torch.cuda.is_available() else 'cpu'
    _last_alert_time = 0
    _alert_interval = 2.0

    @classmethod
    def load_model(cls):
        # YOLO 모델 1번만 로드
        if cls._model is None:
            cls._model = YOLO('yolov8n.pt')
            cls._model.to(cls._device)
            print(f"AI Model Loaded on: {cls._device}")
        return cls._model

    @classmethod
    def set_target(cls, label):
        # 프론트에서 입력한 감시 대상 저장
        cls._target_label = label.strip().lower()

    @classmethod
    def run_rtsp_stream(cls, socketio, rtsp_url, serial_service=None):
        # RTSP를 TCP 방식으로 받도록 OpenCV 옵션 설정
        os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp|stimeout;5000000"

        # RTSP 카메라 연결
        cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        # 연결 실패 시 종료
        if not cap.isOpened():
            print(f"[ERROR] RTSP 연결 실패: {rtsp_url}")
            return

        # 모델 로드
        model = cls.load_model()
        frame_count = 0
        print(f"[START] AI 모니터링 시작 (Device: {cls._device})")

        while cap.isOpened():
            ret, frame = cap.read()

            # 프레임 읽기 실패 시 잠깐 대기 후 다음 루프
            if not ret:
                socketio.sleep(0.1)
                continue

            # 프레임 크기 고정
            frame = cv2.resize(frame, (640, 480))

            frame_count += 1

            # 3프레임당 1번만 탐지 수행
            if frame_count % 3 != 0:
                continue

            # YOLO 예측 수행
            results = model.predict(
                frame,
                device=0,
                conf=0.7,
                verbose=False,
                imgsz=640
            )

            # 탐지 박스 정보
            boxes = results[0].boxes

            # 바운딩 박스가 그려진 결과 이미지 생성
            annotated_frame = results[0].plot()

            # 브라우저 전송용 JPG 인코딩
            _, buffer = cv2.imencode('.jpg', annotated_frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            encoded_image = base64.b64encode(buffer).decode('utf-8')

            # 프론트로 영상 프레임 전송
            socketio.emit('ai_frame', {
                'image': encoded_image,
                'count': frame_count
            })

            # 감시 대상이 설정된 경우 알림 체크
            if cls._target_label:
                detected_names = [
                    model.names[int(cls_idx)].lower()
                    for cls_idx in boxes.cls.tolist()
                ]

                now = time.time()

                if cls._target_label in detected_names and now - cls._last_alert_time >= cls._alert_interval:
                    cls._last_alert_time = now

                    socketio.emit('detection_alert', {
                        'label': cls._target_label,
                        'time': time.strftime('%H:%M:%S')
                    })

                    if serial_service:
                        serial_service.send(f"DETECTED:{cls._target_label}")

            # CPU/GPU 과부하 방지용 짧은 대기
            socketio.sleep(0.01)

            # 종료 키 처리
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # 카메라 자원 해제
        cap.release()
