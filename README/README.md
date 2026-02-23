# Smart City IoT Analytics for Real-Time Traffic and Air Quality Monitoring

## Project Overview
This project uses data analytics and machine learning to analyze traffic and air quality data and generate real-time risk predictions.

## Folder Structure
- training/: Model training (offline)
- backend/: Flask API for deployment
- frontend/: Streamlit dashboard and UI
- data/: Dataset
- notebook/: EDA and experiments

## How to Run
1. Train model: `python training/train_model.py`
2. Start backend: `python backend/backend_app.py`
3. Start frontend: `streamlit run frontend/frontend_dashboard.py`
