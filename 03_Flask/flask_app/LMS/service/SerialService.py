import os
import threading

import serial
from serial.tools import list_ports


class SerialService:
    _serial = None
    _lock = threading.Lock()
    _port = os.getenv("COM_PORT", "COM3")
    _baudrate = int(os.getenv("COM_BAUDRATE", "9600"))

    @classmethod
    def configure(cls, port=None, baudrate=None):
        if port:
            cls._port = port

        if baudrate:
            cls._baudrate = int(baudrate)

    @classmethod
    def available_ports(cls):
        return [port.device for port in list_ports.comports()]

    @classmethod
    def connect(cls, port=None, baudrate=None):
        cls.configure(port, baudrate)

        with cls._lock:
            if cls._serial and cls._serial.is_open:
                return cls.status()

            try:
                cls._serial = serial.Serial(
                    port=cls._port,
                    baudrate=cls._baudrate,
                    timeout=1,
                    write_timeout=1,
                )
                print(f"[COM] 연결 성공: {cls._port} ({cls._baudrate})")
            except serial.SerialException as exc:
                cls._serial = None
                print(f"[COM] 연결 실패: {cls._port} - {exc}")

            return cls.status()

    @classmethod
    def disconnect(cls):
        with cls._lock:
            if cls._serial and cls._serial.is_open:
                cls._serial.close()
                print(f"[COM] 연결 종료: {cls._port}")

            cls._serial = None
            return cls.status()

    @classmethod
    def send(cls, message):
        with cls._lock:
            if not cls._serial or not cls._serial.is_open:
                return False

            data = f"{message}\n".encode("utf-8")
            cls._serial.write(data)
            cls._serial.flush()
            return True

    @classmethod
    def status(cls):
        connected = bool(cls._serial and cls._serial.is_open)

        return {
            "connected": connected,
            "port": cls._port,
            "baudrate": cls._baudrate,
            "available_ports": cls.available_ports(),
        }
