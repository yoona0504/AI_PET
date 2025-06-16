# face_detector.py

import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def detect_faces(frame):
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as detector:
        results = detector.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)
    return frame
