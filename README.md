# 🚦 Smart City IoT Analytics for Traffic & Air Quality Monitoring

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Active-success)

A **Smart City Monitoring System** that analyzes **traffic congestion and air quality** using IoT-style data simulation, Machine Learning, and real-time dashboards.

The project provides **two different dashboards**:

* **Streamlit Analytics Dashboard** → Data analytics & visualization
* **Web Monitoring Portal (HTML Dashboard)** → Real-time city monitoring interface

---

# 📌 Project Overview

Rapid urbanization leads to major problems such as:

* Traffic congestion
* Air pollution
* Lack of real-time monitoring

This system demonstrates how **IoT + Data Analytics + Visualization** can be used to build a **Smart City Control Center**.

The platform monitors:

* 🚗 Average traffic speed
* 📊 Traffic density
* 🚦 Congestion level
* 🌫 Air Quality Index (AQI)

---

# 🏗 System Architecture

```
IoT Sensor Data (Simulated)
          │
          │
          ▼
     Flask Backend API
          │
          ├──────────────► Streamlit Dashboard
          │                  (Analytics + Charts)
          │
          └──────────────► Web Monitoring Portal
                             (HTML Dashboard)
```

---

# 🚀 Key Features

## 🌍 Real-Time Monitoring

* Average Traffic Speed
* Traffic Density
* Congestion Level
* Air Quality Index (AQI)

## 📊 Streamlit Analytics Dashboard

* Traffic Density across Zones
* AQI Trend Visualization
* AQI Distribution Chart
* Smart City Monitoring Map
* Pollution Heat Zones

## 🖥 Web Monitoring Portal

* Live city traffic monitoring
* Traffic status across zones
* Tirupati traffic monitoring map
* Real-time alerts

---

# 🛠 Tech Stack

### Programming

* Python

### Backend

* Flask

### Data Analytics

* Pandas
* NumPy
* Scikit-Learn

### Visualization

* Plotly
* Streamlit

### Frontend

* HTML
* CSS
* JavaScript

---

# 📂 Project Structure

```
smart-city-iot-analytics
│
├── backend
│   ├── backend_app.py
│   ├── model.pkl
│   ├── scaler.pkl
│   └── requirements.txt
│
├── frontend
│   ├── frontend_dashboard.py
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── data
│
├── deployment
│
├── screenshots
│
└── README.md
```

---

# ▶️ How to Run the Project

## 1️⃣ Install Dependencies

```
pip install -r backend/requirements.txt
```

---

## 2️⃣ Run Flask Backend

```
cd backend
python backend_app.py
```

Backend API runs at:

```
http://127.0.0.1:5001
```

Test API:

```
http://127.0.0.1:5001/predict
```

---

## 3️⃣ Run Streamlit Dashboard

```
cd frontend
streamlit run frontend_dashboard.py
```

Dashboard will open at:

```
http://localhost:8501
```

---

## 4️⃣ Run HTML Monitoring Portal

Open:

```
frontend/index.html
```

Or run with Live Server:

```
http://127.0.0.1:5500/frontend/index.html
```

---

# 📸 Dashboard Preview

Add screenshots here after uploading them to the **screenshots** folder.

Example:

```
screenshots/dashboard.png
screenshots/traffic_chart.png
screenshots/map.png
```

Example display:

![Dashboard](screenshots/dashboard.png)

---

# 🎯 Applications

* Smart Traffic Management
* Air Pollution Monitoring
* Smart City Command Centers
* Urban Planning & Infrastructure Monitoring

---

# 🔮 Future Improvements

* Integration with real IoT sensors
* AI-based traffic prediction
* Real-time pollution alerts
* Live CCTV traffic monitoring
* Cloud deployment

---

