# 🌧️ Rainfall Prediction System using Machine Learning

This project is a **Rainfall Prediction System** built with **Random Forest Classifier** and deployed using **Streamlit**. The system predicts whether it will rain based on various weather parameters like temperature, humidity, pressure, wind speed, wind direction, etc.

---

## 🚀 Features

- Interactive UI using **Streamlit**
- User-friendly **sliders and dropdowns** for input
- Preprocessing with **RobustScaler**
- Balanced dataset using **resampling**
- Encoded wind direction using **LabelEncoder**
- Live prediction using **Random Forest**
- Clear prediction result: "Rainfall Expected" or "No Rainfall"

---

## 📊 Input Features

- `pressure (hPa)`
- `maxtemp (°C)`
- `temparature (°C)`
- `mintemp (°C)`
- `dewpoint (°C)`
- `humidity (%)`
- `cloud (%)`
- `sunshine (hours)`
- `winddirection (encoded)`
- `windspeed (km/h)`

---

## 📁 Files

| File Name                            | Description                                      |
|-------------------------------------|--------------------------------------------------|
| `Rainfall.csv`                      | Original weather dataset                         |
| `Rainfall_prediction.pkl`          | Trained Random Forest model                      |
| `Rainfall_prediction_labelEncoder.pkl` | LabelEncoder for wind direction             |
| `Rainfall_prediction_robustScaler.pkl` | RobustScaler for feature scaling           |
| `app.py`                            | Streamlit GUI application                        |
| `README.md`                         | Project documentation                            |

---

## 💻 How to Run the Project

### 🔧 Requirements
Make sure you have Python 3.x and the following libraries installed:

```bash
pip install streamlit pandas scikit-learn
