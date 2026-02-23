from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/api/latest")
def latest_data():
    data = {
        "timestamp": time.strftime("%H:%M:%S"),
        "avg_speed_kmph": random.randint(30, 80),
        "traffic_density": random.randint(20, 90),
        "traffic_severity": random.choice(["Low", "Medium", "High"]),
        "predicted_aqi": round(random.uniform(80, 300), 2)
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
