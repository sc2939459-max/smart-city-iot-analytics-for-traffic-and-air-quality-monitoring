# 🚦 Smart City IoT Analytics for Traffic and Air Quality Monitoring

A real-time Smart City monitoring system that analyzes **traffic congestion and air quality** using **IoT sensor data and Machine Learning models**.
The system provides live analytics dashboards, predictive insights, and camera monitoring for urban traffic management.

---

## 📌 Project Overview

This project integrates:

* IoT Sensor Data
* Machine Learning Models
* Flask Backend API
* Streamlit Interactive Dashboard

The goal is to help cities monitor:

* 🚗 Traffic Density
* 🌫 Air Quality Index (AQI)
* 🚦 Traffic Congestion Levels
* 📊 Real-time Analytics

---

## ⚙️ Technology Stack

* **Python**
* **Machine Learning**
* **Flask API**
* **Streamlit Dashboard**
* **Pandas / Scikit-learn**
* **Plotly Visualization**

---

## 🧠 Machine Learning Models Used

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting

The best model is selected using evaluation metrics.

---

## 🏗 Project Architecture

IoT Sensor Data
↓
Data Preprocessing & Feature Engineering
↓
Machine Learning Prediction
↓
Flask Backend API
↓
Streamlit Dashboard & Alerts

---

## 📊 Dashboard Features

* Live Traffic Density Monitoring
* Air Quality Index Visualization
* Traffic Congestion Prediction
* Smart City Analytics Dashboard
* Live Traffic Camera Monitoring

---

## 📂 Project Structure

```
backend/
    backend_app.py
    model.pkl
    scaler.pkl

frontend/
    frontend_dashboard.py

data/
    sensor dataset

deployment/

notebook/
    project.ipynb
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 2️⃣ Start Backend API

```
python backend/backend_app.py
```

Backend runs on:

```
http://127.0.0.1:5001
```

---

### 3️⃣ Run Streamlit Dashboard

```
streamlit run frontend/frontend_dashboard.py
```

Dashboard runs on:

```
http://localhost:8501
```

---

## 📸 Dashboard Preview

Smart City Analytics Dashboard showing:

* Traffic Density Charts
* AQI Trend Visualization
* Live Traffic Camera Monitoring

---

## 🎯 Future Improvements

* Real-time IoT sensor integration
* Smart city traffic prediction
* AI-based vehicle detection
* Live camera analytics
* City map visualization

---
