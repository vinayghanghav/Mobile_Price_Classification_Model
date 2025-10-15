import streamlit as st
import pickle
import numpy as np

# ---------------------------
# Load the trained model
# ---------------------------
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("📱 Mobile Price Range Prediction App")
st.write("Enter the mobile specifications below to predict its price range (0 = Low, 1 = Medium, 2 = High, 3 = Very High).")

# ---------------------------
# Define input fields
# ---------------------------
battery_power = st.number_input("Battery Power (mAh)", min_value=500, max_value=5000, value=2000)
blue = st.selectbox("Bluetooth", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
clock_speed = st.number_input("Clock Speed (GHz)", min_value=0.5, max_value=3.0, value=1.5, step=0.1)
dual_sim = st.selectbox("Dual SIM", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
fc = st.number_input("Front Camera (MP)", min_value=0, max_value=20, value=5)
four_g = st.selectbox("4G Support", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
int_memory = st.number_input("Internal Memory (GB)", min_value=2, max_value=256, value=32)
m_dep = st.number_input("Mobile Depth (cm)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
mobile_wt = st.number_input("Mobile Weight (grams)", min_value=50, max_value=300, value=150)
n_cores = st.number_input("Number of Cores", min_value=1, max_value=8, value=4)
pc = st.number_input("Primary Camera (MP)", min_value=0, max_value=20, value=13)
px_height = st.number_input("Pixel Height", min_value=0, max_value=2000, value=800)
px_width = st.number_input("Pixel Width", min_value=0, max_value=2000, value=1200)
ram = st.number_input("RAM (MB)", min_value=256, max_value=8192, value=2048, step=256)
sc_h = st.number_input("Screen Height (cm)", min_value=5, max_value=20, value=10)
sc_w = st.number_input("Screen Width (cm)", min_value=2, max_value=10, value=5)
talk_time = st.number_input("Talk Time (hours)", min_value=2, max_value=20, value=10)
three_g = st.selectbox("3G Support", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
touch_screen = st.selectbox("Touch Screen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
wifi = st.selectbox("WiFi", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# ---------------------------
# Prepare the input for prediction
# ---------------------------
input_features = np.array([[battery_power, blue, clock_speed, dual_sim, fc, four_g,
                            int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
                            px_width, ram, sc_h, sc_w, talk_time, three_g,
                            touch_screen, wifi]])

# ---------------------------
# Predict
# ---------------------------
if st.button("Predict Price Range"):
    prediction = model.predict(input_features)[0]
    label_map = {
        0: "💰 Low Cost",
        1: "💵 Medium Cost",
        2: "💎 High Cost",
        3: "🏆 Very High Cost"
    }
    st.success(f"Predicted Price Range: {label_map[prediction]}")
