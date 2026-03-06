# 🚦 Smart City IoT Analytics for Traffic & Air Quality Monitoring

Real-time **Smart City Analytics platform** that monitors **traffic density, congestion levels, and air quality** using IoT data streams, Machine Learning predictions, Flask APIs, and interactive dashboards.

The system provides both:

• **Streamlit analytical dashboard** for data visualization
• **HTML monitoring portal** for real-time city traffic monitoring

---

# 📌 Project Overview

Urban cities face increasing challenges with **traffic congestion and air pollution**. This project simulates a **Smart City Monitoring System** that analyzes traffic data and environmental indicators to help authorities make informed decisions.

The platform integrates:

• Machine Learning predictions
• REST APIs for data access
• Real-time dashboards
• Traffic and AQI visualization tools

---

# 🧠 Technologies Used

* **Python**
* **Flask**
* **Streamlit**
* **Machine Learning**
* **HTML / CSS / JavaScript**
* **Plotly Visualizations**
* **Leaflet Maps**

---

# 🏗 Project Architecture

```
IoT Sensor Data
       │
       ▼
Machine Learning Model
       │
       ▼
Flask Backend API
       │
 ┌─────┴─────┐
 ▼           ▼
Streamlit    Web Dashboard
Dashboard    (HTML Portal)
```

---

# 📂 Project Structure

```
smart-city-iot-analytics
│
├── backend
│   └── backend_app.py
│
├── frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── deployment
├── notebook
├── data
│
├── screenshots
│   ├── backend.jpg
│   ├── backend_predict.jpg
│
├── demo
│   ├── streamlit_dashboard.mp4
│   └── frontend_dashboard.mp4
│
└── README.md
```

---

# ⚙️ Backend API

Start the Flask backend:

```
python backend/backend_app.py
```

Backend runs on:

```
http://127.0.0.1:5001
```

API endpoint for prediction:

```
http://127.0.0.1:5001/predict
```

Example response:

```
{
  "speed": 48,
  "density": 60,
  "congestion": "Medium",
  "aqi": 94
}
```

---

# 📊 Streamlit Dashboard

Run the analytics dashboard:

```
streamlit run frontend/frontend_dashboard.py
```

Dashboard includes:

* Traffic Density Analysis
* AQI Trends
* Pie Chart Distribution
* Traffic Monitoring Map
* Pollution Heat Zones
* Semi-Circular AQI Gauge

---

# 🌐 Web Monitoring Portal

Open the frontend dashboard:

```
frontend/index.html
```

Features:

* Live Traffic Metrics
* Zone-based Traffic Status
* Interactive City Map
* Traffic Density Table
* Air Quality Monitoring

---

# 📸 Project Screenshots

## Backend Running

![Backend](screenshots/backend.jpg)

## API Prediction Output

![API](screenshots/backend%20predict.jpg)

---

# 🎥 Project Demo

### Streamlit Dashboard Demo

[Watch Demo](demo/streamlit%20dashbaord.mv.mp4)

### Frontend Monitoring Portal Demo

[Watch Demo](demo/frontend_html.mv.mp4)

---

# 🚀 Key Features

✔ Real-time traffic monitoring
✔ Air Quality Index prediction
✔ Machine learning integration
✔ REST API architecture
✔ Interactive data visualization
✔ Smart city monitoring portal

---

# 📈 Future Improvements

* Real IoT sensor integration
* Deployment on cloud platforms
* Real-time Kafka data streaming
* Mobile application dashboard
* Advanced predictive analytics

---


