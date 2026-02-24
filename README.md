# 🚦 Smart City IoT Analytics for Traffic and Air Quality Monitoring

A real-time Smart City analytics platform that monitors **traffic conditions** and **air quality levels** using IoT data, Machine Learning, Flask APIs, and interactive dashboards.

The system simulates IoT sensor data, processes it through a backend analytics pipeline, and visualizes live insights via web and Streamlit dashboards.

---

## 📌 Project Overview

Urban cities face increasing challenges related to traffic congestion and air pollution.  
This project provides a **real-time analytics solution** that:

- Collects simulated IoT traffic & environmental data
- Processes data using Machine Learning workflows
- Serves analytics through a Flask REST API
- Displays live monitoring dashboards
- Generates alerts based on AQI conditions

The goal is to demonstrate **end-to-end integration of IoT + Data Analytics + Web Deployment**.

---

## 🎯 Objectives

- Monitor real-time vehicle speed and traffic density
- Analyze congestion levels dynamically
- Predict and track Air Quality Index (AQI)
- Provide live visualization dashboards
- Deploy a scalable analytics pipeline

---

## 🏗️ System Architecture

IoT Sensor Data
↓
Data Preprocessing & Feature Engineering
↓
Machine Learning Model
↓
Flask Backend API
↓
Streamlit Dashboard & Web Dashboard


---

## ⚙️ Tech Stack

### 👨‍💻 Programming & Frameworks
- Python
- Flask
- Streamlit

### 📊 Data & Machine Learning
- Pandas
- NumPy
- Scikit-learn

### 🌐 Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### ☁️ Deployment
- Render (Flask API Deployment)
- Streamlit Cloud

---

## 📂 Project Structure
smart-city-iot-analytics/
│
├── backend/ # Flask API
├── frontend/ # Web dashboard
├── deployment/ # Gunicorn & deployment configs
├── data/ # Dataset
├── notebook/ # EDA & model training
├── screenshots/ # Project demo images
└── README.md

---

## 🚀 Live Demo

### 🔹 Flask Backend API (Render)
👉 https://smart-city-iot-analytics-for-traffic-and.onrender.com

### 🔹 Streamlit Dashboard
👉 http://localhost:8501/

---

## 🔌 API Endpoint

### Get Latest IoT Analytics
GET /api/latest

### Example Response

'''json
{
  "avg_speed": 42,
  "traffic_density": 191,
  "congestion": "High",
  "aqi": 74,
  "timestamp": "16:39:18"
}

---

## 📸 Project Screenshots

### 🔹 Backend API Response
Real-time JSON response from Flask backend API.

![API Response](screenshots/api_latest.png)

---

### 🔹 Web Dashboard (Frontend)
Traffic and air-quality monitoring dashboard built using HTML, CSS, and JavaScript.

![Dashboard](screenshots/dashboard.png)

---

### 🔹 Deployment Dashboard (Render)
Cloud deployment of Flask backend service.

![Deployment](screenshots/deployment.png)

---

### 🔹 Streamlit Analytics Dashboard
Interactive analytics dashboard with live visualization and alerts.

![Streamlit Dashboard](screenshots/streamlit.png)

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone Repository

git clone https://github.com/sc2939459-max/smart-city-iot-analytics-for-traffic-and-air-quality-monitoring.git
cd smart-city-iot-analytics-for-traffic-and-air-quality-monitoring

###2️⃣ Install Dependencies
pip install -r requirements.txt

###3️⃣ Run Flask Backend
python backend/app.py
API runs at:
http://127.0.0.1:5001

###4️⃣ Run Streamlit Dashboard
streamlit run deployment/app.py
Dashboard opens at:
http://localhost:8501
