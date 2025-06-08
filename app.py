import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained models
model = pickle.load(open("Rainfall_prediction.pkl", "rb"))
label_encoder = pickle.load(open("Rainfall_prediction_labelEncoder.pkl", "rb"))
scaler = pickle.load(open("Rainfall_prediction_robustScaler.pkl", "rb"))

# Reverse map from winddirection labels to encoded values
wind_classes = label_encoder.classes_
reverse_map = {label: idx for idx, label in enumerate(wind_classes)}

# Streamlit UI
st.set_page_config(page_title="Rainfall Prediction", layout="centered")
st.title("🌧️ Rainfall Prediction App")
st.markdown("Enter the weather conditions below to predict rainfall.")

# Input Fields (with sliders)
with st.form("rainfall_form"):
    col1, col2 = st.columns(2)

    with col1:
        pressure = st.slider("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1010.0, step=0.1)
        maxtemp = st.slider("Max Temperature (°C)", min_value=-10.0, max_value=60.0, value=35.0, step=0.1)
        temparature = st.slider("Temperature (°C)", min_value=-10.0, max_value=60.0, value=30.0, step=0.1)
        mintemp = st.slider("Min Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0, step=0.1)
        dewpoint = st.slider("Dew Point (°C)", min_value=-10.0, max_value=50.0, value=22.0, step=0.1)

    with col2:
        humidity = st.slider("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=1.0)
        cloud = st.slider("Cloud (%)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
        sunshine = st.slider("Sunshine (hours)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
        wind_dir_label = st.selectbox("Wind Direction", list(reverse_map.keys()))
        windspeed = st.slider("Wind Speed (km/h)", min_value=0.0, max_value=150.0, value=10.0, step=0.5)

    submitted = st.form_submit_button("Predict")

# Predict
if submitted:
    try:
        # Convert winddirection label to encoded number
        winddirection = reverse_map[wind_dir_label]

        # Prepare input data
        input_data = pd.DataFrame({
            'pressure ': [pressure],
            'maxtemp': [maxtemp],
            'temparature': [temparature],
            'mintemp': [mintemp],
            'dewpoint': [dewpoint],
            'humidity ': [humidity],
            'cloud ': [cloud],
            'sunshine': [sunshine],
            'winddirection': [winddirection],
            'windspeed': [windspeed]
        })

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)[0]

        # Output
        if prediction == 1:
            st.success("✅ Rainfall is expected.")
        else:
            st.info("☀️ No rainfall expected.")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
