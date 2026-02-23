import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("../data/smart_city_iot_speedlimit_dataset.csv")

# Feature engineering
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour

df["rush_hour"] = (((df["hour"] >= 7) & (df["hour"] <= 10)) |
                   ((df["hour"] >= 17) & (df["hour"] <= 20))).astype(int)

df["pollution_index"] = 0.4*df["pm10"] + 0.3*df["no2"] + 0.3*df["co"]
df["target"] = (df["avg_speed"] > df["speed_limit"]).astype(int)

features = [
    "vehicle_count","traffic_density","avg_speed",
    "pm10","no2","co",
    "temperature_c","humidity_percent",
    "rush_hour","pollution_index"
]

X = df[features]
y = df["target"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    class_weight="balanced",
    random_state=42
)
model.fit(X_train_scaled, y_train)

# Save artifacts
pickle.dump(model, open("../backend/model.pkl", "wb"))
pickle.dump(scaler, open("../backend/scaler.pkl", "wb"))

print("✅ Model and scaler saved to backend/")
