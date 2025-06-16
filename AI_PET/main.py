import cv2
from camera_capture import get_frame
from face_detector import detect_faces
from emotion_analyzer import analyze_emotion
from emotion_response import get_emotion_response
import csv
from datetime import datetime

def log_emotion(emotion, filename='emotion_log.csv'):
    """감정과 타임스탬프를 CSV에 기록"""
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().isoformat(), emotion])
    except Exception as e:
        print(f"로그 저장 실패: {e}")

def main():
    print("루루봇 감정 인식 시스템 시작 (종료: Q 키)")

    while True:
        try:
            frame = get_frame()
        except RuntimeError as e:
            print(e)
            break

        frame = detect_faces(frame)
        emotion = analyze_emotion(frame)
        response = get_emotion_response(emotion)

        log_emotion(emotion)

        print(f"[감정]: {emotion} | [루루봇]: {response}")
        cv2.putText(frame, f"{emotion}: {response}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        cv2.imshow("루루봇 - 얼굴 & 감정 인식", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("종료합니다.")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
