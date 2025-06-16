# emotion_analyzer.py

from deepface import DeepFace

def analyze_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except Exception as e:
        print("감정 분석 실패:", e)
        return "분석 실패"
