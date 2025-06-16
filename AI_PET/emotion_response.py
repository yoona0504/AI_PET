def get_emotion_response(emotion):
    responses = {
        'happy': "You look happy!",
        'sad': "Feeling down?",
        'angry': "Take a deep breath.",
        'surprise': "Oh! Surprised?",
        'neutral': "Just a calm day.",
    }
    return responses.get(emotion, '오늘도 힘내요!')
