from flask import Flask, render_template
from flask_socketio import SocketIO
from service.AiStreamService import AiStreamService
from service.SerialService import SerialService
import os

# Flask 앱 생성
app = Flask(__name__)

# 세션/보안용 기본 키 설정
app.config['SECRET_KEY'] = 'mbc_secret_key'

# 소켓 서버 연결
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')


# 메인 페이지 테스트용
@app.route('/')
def home():
    return render_template('layout.html')


# IP 카메라 실시간 스트리밍 분석 페이지
@app.route('/ai-detect/aistream')
def ai_stream():
    return render_template('ai_detect/ai_stream.html')


# 백그라운드에서 AI 스트림 분석 실행
def run_ai_logic():
    # RTSP 카메라 주소
    RTSP_URL = "rtsp://admin:Mbc320!!@192.168.0.43:554/stream1"
    print("[SYSTEM] AI Background Task Start")
    AiStreamService.run_rtsp_stream(socketio, RTSP_URL, SerialService)


# 사용자가 페이지 접속하면 스트리밍 시작
@socketio.on('connect')
def handle_connect():
    socketio.emit('serial_status', SerialService.status())
    socketio.start_background_task(run_ai_logic)


# 프론트에서 감시 대상 객체명을 보내면 저장
@socketio.on('set_detection_target')
def handle_target(data):
    target = data.get('target', '')
    AiStreamService.set_target(target)


@socketio.on('serial_connect')
def handle_serial_connect(data):
    port = data.get('port') if data else None
    baudrate = data.get('baudrate') if data else None
    socketio.emit('serial_status', SerialService.connect(port, baudrate))


@socketio.on('serial_disconnect')
def handle_serial_disconnect():
    socketio.emit('serial_status', SerialService.disconnect())


@socketio.on('serial_send')
def handle_serial_send(data):
    message = data.get('message', '') if data else ''
    success = SerialService.send(message)
    status = SerialService.status()
    status['last_send_success'] = success
    socketio.emit('serial_status', status)


# 서버 실행
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5050, debug=False, use_reloader=False)
