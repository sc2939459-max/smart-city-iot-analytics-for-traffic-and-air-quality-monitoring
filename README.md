# 🚦 Smart City IoT Analytics for Traffic and Air Quality Monitoring

A smart city monitoring system that analyzes **traffic density, congestion, and air quality (AQI)** using **IoT-style data streams, machine learning models, Flask APIs, and interactive dashboards**.

The system provides:

* 📊 **Streamlit Analytics Dashboard**
* 🌐 **HTML Monitoring Portal**
* 🔌 **Flask Backend API**
* 🎥 **Demo videos for system operation**

---

# 📌 Project Overview

Urban cities face serious challenges due to **traffic congestion and air pollution**.
This project simulates a **Smart City Control Center** that collects and analyzes sensor data to provide **real-time monitoring and decision support**.

The platform monitors:

* 🚗 Average Traffic Speed
* 📊 Traffic Density
* 🚦 Congestion Level
* 🌫 Air Quality Index (AQI)

---

# 🏗 System Architecture

```
IoT Sensor Data
      │
      ▼
Machine Learning Model
      │
      ▼
Flask Backend API
      │
 ┌────┴────┐
 ▼         ▼
Streamlit   HTML Monitoring
Dashboard   Portal
```

---

# ⚙️ Technologies Used

* Python
* Flask
* Streamlit
* Scikit-learn
* Pandas & NumPy
* HTML / CSS / JavaScript
* Plotly Visualization

---

# 📂 Project Structure

```
smart-city-iot-analytics
│
├── backend
│   └── backend_app.py
│
├── frontend
│   ├── frontend_dashboard.py
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── data
├── notebook
├── deployment
│
├── screenshots
│   ├── backend.jpg
│   └── backend_predict.jpg
│
├── videos
│   ├── streamlit_dashboard_demo.mp4
│   └── frontend_dashboard_demo.mp4
│
└── README.md
```

---

# 🚀 Running the Project

### Start Backend

```bash
python backend/backend_app.py
```

Backend runs at:

```
http://127.0.0.1:5001
```

Test API:

```
http://127.0.0.1:5001/predict
```

---

### Run Streamlit Dashboard

```bash
streamlit run frontend/frontend_dashboard.py
```

Dashboard opens at:

```
http://localhost:8501
```

---

### Run HTML Monitoring Portal

Open:

```
frontend/index.html
```

---

# 📸 Screenshots

### Backend Running

![Backend Running](screenshots/backend.jpg)

### API Prediction Output

![API Output](screenshots/backend%20predict.jpg)

---

# 🎥 Demo Videos

### Streamlit Dashboard Demo

Watch the full dashboard demonstration:

[videos/streamlit_dashboard_demo.mp4](videos/streamlit_dashboard_demo.mp4)

### HTML Monitoring Portal Demo

Watch the frontend monitoring system:

[videos/frontend_dashboard_demo.mp4](videos/frontend_dashboard_demo.mp4)

---

# ⭐ Key Features

* Real-time traffic monitoring
* AQI prediction and visualization
* Machine learning integration
* REST API architecture
* Interactive dashboards
* Smart city monitoring interface

---

# 🔮 Future Improvements

* Integration with real IoT sensors
* Cloud deployment
* Real-time traffic prediction
* Mobile monitoring dashboard

---

