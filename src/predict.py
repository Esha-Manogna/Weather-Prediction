import joblib
import pandas as pd

# Load the trained model
model = joblib.load("../models/weather_model.pkl")

# Sample input
data = pd.DataFrame({
    "humidity": [70],
    "wind_speed": [5],
    "meanpressure": [1015]
})

prediction = model.predict(data)

print("Predicted Temperature:", prediction[0])