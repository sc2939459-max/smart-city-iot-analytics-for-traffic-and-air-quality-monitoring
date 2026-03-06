from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Smart City IoT Backend Running"

@app.route("/data")
def data():

    avg_speed = random.randint(20,80)
    density = random.randint(60,200)
    aqi = random.randint(40,180)

    if avg_speed < 25:
        congestion = "HIGH"
    elif avg_speed < 45:
        congestion = "MEDIUM"
    else:
        congestion = "LOW"

    return jsonify({
        "avg_speed": avg_speed,
        "traffic_density": density,
        "aqi": aqi,
        "congestion": congestion
    })

if __name__ == "__main__":
    app.run(port=5001,debug=True)