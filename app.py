import streamlit as st
import pandas as pd
import pickle
import numpy as np

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# -----------------------
# LOAD MODEL
# -----------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# -----------------------
# LOAD DATASET (Optional)
# -----------------------
try:
    df = pd.read_csv("Housing_Cleaned.csv")
    total_houses = len(df)
except:
    total_houses = "N/A"

# -----------------------
# TITLE
# -----------------------
st.title("🏠 House Price Prediction")
st.write("Predict residential house prices using Machine Learning.")

st.divider()

# -----------------------
# INPUTS
# -----------------------
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", 500, 20000, 3000)
    bedrooms = st.selectbox("Bedrooms", [1,2,3,4,5,6])
    bathrooms = st.selectbox("Bathrooms", [1,2,3,4])
    stories = st.selectbox("Stories", [1,2,3,4])
    parking = st.selectbox("Parking Spaces", [0,1,2,3])
    furnishing = st.selectbox(
        "Furnishing Status",
        ["Unfurnished","Semi-Furnished","Furnished"]
    )

with col2:
    mainroad = st.checkbox("Main Road Access")
    guestroom = st.checkbox("Guest Room")
    basement = st.checkbox("Basement")
    hotwater = st.checkbox("Hot Water Heating")
    aircon = st.checkbox("Air Conditioning")
    preferred = st.checkbox("Preferred Area")

# -----------------------
# ENCODING
# -----------------------
furnishing_map = {
    "Unfurnished":0,
    "Semi-Furnished":1,
    "Furnished":2
}

features = np.array([[
    area,
    bedrooms,
    bathrooms,
    stories,
    int(mainroad),
    int(guestroom),
    int(basement),
    int(hotwater),
    int(aircon),
    parking,
    int(preferred),
    furnishing_map[furnishing]
]])

# -----------------------
# PREDICTION
# -----------------------
if st.button("Predict Price", use_container_width=True):

    prediction = model.predict(features)[0]

    lakhs = prediction / 100000

    st.success("Prediction Successful!")

    st.metric(
        "Predicted Price",
        f"₹ {lakhs:.2f} Lakhs"
    )

    st.info(
        f"Estimated Market Range: ₹ {lakhs*0.92:.2f}L - ₹ {lakhs*1.08:.2f}L"
    )

st.divider()

# -----------------------
# PROJECT INFO
# -----------------------
st.subheader("Project Information")

c1, c2, c3 = st.columns(3)

c1.metric("Model", "Linear Regression")
c2.metric("Accuracy (R²)", "0.6609")
c3.metric("Dataset", f"{total_houses} Houses")

st.caption("Developed by Mukesh Kumhar")