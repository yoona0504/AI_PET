# app.py
from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def index():
    if not os.path.exists("emotion_log.csv"):
        return "<h2>감정 기록이 없습니다.</h2>"

    df = pd.read_csv("emotion_log.csv", header=None, names=["time", "emotion"])
    latest = df.tail(10).to_dict(orient="records")
    return render_template("index.html", emotions=latest)

if __name__ == "__main__":
    app.run(debug=True)
