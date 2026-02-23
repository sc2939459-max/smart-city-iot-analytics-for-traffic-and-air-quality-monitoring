from flask import Flask, jsonify
from flask_cors import CORS
import random
import datetime

app = Flask(__name__)

# VERY IMPORTANT — allow frontend access
CORS(app, resources={r"/*": {"origins": "*"}})

# Home route
@app.route("/")
def home():
    return "Backend API running successfully"

# API route
@app.route("/api/latest")
def latest():
    data = {
        "avg_speed": random.randint(30, 80),
        "traffic_density": random.randint(50, 200),
        "congestion": random.choice(["Low", "Medium", "High"]),
        "aqi": random.randint(50, 250),
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
