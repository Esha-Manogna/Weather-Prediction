# 🌦️ Weather Data Analysis and Prediction using Machine Learning

## 📌 Project Overview

Weather Data Analysis and Prediction is a Machine Learning project that analyzes historical weather data and predicts the daily mean temperature using historical weather attributes.

The project uses weather parameters such as humidity, wind speed, and atmospheric pressure to build a Linear Regression model capable of predicting the average daily temperature.

This project demonstrates the complete Machine Learning workflow, including data preprocessing, visualization, model training, evaluation, model persistence, and prediction.

---

# 🎯 Objective

The main objective of this project is to:

- Analyze historical weather data.
- Perform Exploratory Data Analysis (EDA).
- Identify relationships between weather parameters.
- Build a Machine Learning model to predict daily mean temperature.
- Evaluate model performance using regression metrics.
- Save the trained model for future predictions.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Jupyter Notebook
- VS Code
- Git & GitHub

---

# 📂 Dataset

**Dataset:** Daily Delhi Climate Dataset

The dataset contains **1462 daily weather records** with the following features:

- Date
- Mean Temperature
- Humidity
- Wind Speed
- Mean Pressure

---

# 📊 Project Workflow

1. Data Collection
2. Data Loading
3. Data Cleaning
4. Data Preprocessing
5. Exploratory Data Analysis (EDA)
6. Data Visualization
7. Feature Selection
8. Train-Test Split
9. Machine Learning Model Training
10. Model Evaluation
11. Save Trained Model
12. Predict Temperature

---

# 📈 Visualizations

The following visualizations were generated during Exploratory Data Analysis (EDA):

- Daily Mean Temperature Trend
- Daily Humidity Trend

These visualizations help understand seasonal temperature changes and humidity variations over time.

---

# 🤖 Machine Learning Model

The following Machine Learning algorithm was implemented:

- Linear Regression

### Input Features

- Humidity
- Wind Speed
- Mean Pressure

### Target Variable

- Mean Temperature

---

# 📊 Model Performance

| Metric | Value |
|---------|--------|
| Mean Absolute Error (MAE) | 5.20 |
| Mean Squared Error (MSE) | 37.16 |
| R² Score | 0.309 |

---

# 🏆 Model Summary

**Algorithm Used**

- Linear Regression

The model was successfully trained using historical weather data and achieved the following performance:

- MAE: **5.20**
- MSE: **37.16**
- R² Score: **0.309**

The trained model was saved using **Joblib** and can be used for future weather predictions.

---

# 📁 Project Structure

```text
Weather-Prediction
│
├── dataset
│   └── DailyDelhiClimateTrain.csv
│
├── models
│   └── weather_model.pkl
│
├── notebooks
│   └── weather_prediction.ipynb
│
├── src
│   └── predict.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📌 Key Features

- Weather Data Analysis
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Temperature Trend Visualization
- Humidity Trend Visualization
- Linear Regression Model
- Model Evaluation
- Temperature Prediction
- Saved Trained Model using Joblib
- Organized Project Structure

---

# 🚀 Future Improvements

- Apply advanced regression algorithms such as Random Forest Regressor and XGBoost Regressor.
- Improve prediction accuracy using feature engineering.
- Use Time Series Forecasting models such as LSTM.
- Integrate live weather data using Weather APIs.
- Build an interactive dashboard using Streamlit.
- Deploy the application on Streamlit Community Cloud or Render.
- Predict weather for future dates.

---

# 📚 Python Libraries Used

- pandas
- numpy
- matplotlib
- scikit-learn
- joblib
- jupyter

---

# ▶️ How to Run the Project

## Clone the Repository

```bash
git clone https://github.com/Esha-Manogna/Weather-Prediction.git
```

## Navigate to the Project Folder

```bash
cd Weather-Prediction
```

## Create a Virtual Environment

```bash
py -m venv venv
```

## Activate the Virtual Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Notebook

```bash
jupyter notebook
```

Open:

```
notebooks/weather_prediction.ipynb
```

---

# 🔮 Predict Temperature

Run the prediction script:

```bash
cd src
python predict.py
```

### Example Output

```text
Predicted Temperature: 23.05 °C
```

---

# 📷 Project Screenshots

## Daily Mean Temperature Trend

<img width="503" height="235" alt="image" src="https://github.com/user-attachments/assets/ca9e7220-3b5c-4584-abf8-1ed9d2424a0b" />


---

## Daily Humidity Trend

<img width="500" height="230" alt="image" src="https://github.com/user-attachments/assets/6dd4b2ea-7a2c-4ff2-acaf-ad3190520f2f" />


---

## Actual vs Predicted Values

<img width="500" height="235" alt="image" src="https://github.com/user-attachments/assets/01d1b4cb-2ec3-40e1-b756-94b4f9c6c4cb" />


---

## Prediction Output

(Add Screenshot Here)

---

# 📌 Conclusion

This project successfully demonstrates how Machine Learning can be used to analyze historical weather data and predict daily mean temperature.

The project follows a complete Machine Learning workflow, including data preprocessing, exploratory data analysis, visualization, model training, evaluation, model persistence, and prediction.

Using historical weather parameters such as humidity, wind speed, and atmospheric pressure, the Linear Regression model was trained to estimate daily mean temperature.

Although the model achieved a moderate R² score of **0.309**, it provides a solid foundation for understanding regression-based prediction problems and can be further improved using advanced algorithms and additional weather features.

This project helped strengthen practical skills in Python, data analysis, visualization, Machine Learning, and model deployment.

