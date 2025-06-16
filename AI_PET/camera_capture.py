# camera_capture.py

import cv2

def get_frame():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError("카메라로부터 프레임을 읽을 수 없습니다.")
    return frame
