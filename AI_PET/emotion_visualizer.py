import pandas as pd
import matplotlib.pyplot as plt

def plot_emotion_history(filename='emotion_log.csv'):
    df = pd.read_csv(filename, header=None, names=["timestamp", "emotion"])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    emotion_counts = df['emotion'].value_counts()

    emotion_counts.plot(kind='bar', title='감정 빈도 분석', ylabel='횟수', xlabel='감정')
    plt.tight_layout()
    plt.show()
