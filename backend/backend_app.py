from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Smart City Backend Running"

@app.route('/predict')
def predict():
    data = {
        "speed": random.randint(30, 60),
        "density": random.randint(50, 200),
        "congestion": random.choice(["Low", "Medium", "High"]),
        "aqi": random.randint(50, 150)
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)