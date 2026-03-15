import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Swiggy Delivery Predictor",page_icon="🚚")
st.image('swiggy.jpg',use_container_width=True)
# load model
model = pickle.load(open("model.pkl","rb"))

st.title("🚚 Swiggy Delivery Time Prediction")

# -------- Numeric Inputs --------

age = st.number_input("Age",18,55)
ratings = st.number_input("Ratings",0.0,5.0)
vehicle_condition = st.selectbox("Vehicle Condition",[1,2,3])
multiple_deliveries = st.slider("Multiple Deliveries",0,5)

distance = st.selectbox("Distance (km)",[0.0,2,4,6,8,10,12,14,1])

pickup_time_minutes = st.number_input("Pickup Time Minutes",0)
order_time_hour = st.slider("Order Hour",0,23)

order_day = st.slider("Order Day",1,31)
order_month = st.slider("Order Month",1,12)

is_weekend = st.selectbox("Is Weekend(0(No),1(Yes))",[0,1])

# -------- Categorical Inputs --------

weather = st.selectbox("Weather",
["cloudy","fog","sandstorms","stormy","sunny","windy"])

type_of_order = st.selectbox("Type of Order",
["buffet","drinks","meal","snack"])

type_of_vehicle = st.selectbox("Vehicle Type",
["bicycle","electric_scooter","motorcycle","scooter"])

festival = st.selectbox("Festival",
["metropolitian","semi-urban","urban"])

city_type = st.selectbox("City Type",
["metropolitian","semi-urban","urban"])

city_name = st.selectbox("City",
['AGR','ALH','AURG','BANG','BHP','CHEN','COIMB','DEH','GOA',
 'HYD','INDO','JAP','KNP','KOC','KOL','LUDH','MUM','MYS',
 'PUNE','RANCHI','SUR','VAD'])

order_day_of_week = st.selectbox("Day of Week",
["friday","monday","saturday","sunday","thursday","tuesday","wednesday"])

order_time_of_day = st.selectbox("Order Time",
["after_midnight","afternoon","evening","morning","night"])

traffic = st.selectbox("Traffic",
["low","medium","high","jam"])

# -------- Prediction --------

if st.button("Predict Delivery Time"):

    input_data = pd.DataFrame([{
        "weather":weather,
        "type_of_order":type_of_order,
        "type_of_vehicle":type_of_vehicle,
        "festival":festival,
        "city_type":city_type,
        "city_name":city_name,
        "order_day_of_week":order_day_of_week,
        "order_time_of_day":order_time_of_day,
        "traffic":traffic,
        "age":age,
        "ratings":ratings,
        "vehicle_condition":vehicle_condition,
        "multiple_deliveries":multiple_deliveries,
        "order_day":order_day,
        "order_month":order_month,
        "is_weekend":is_weekend,
        "pickup_time_minutes":pickup_time_minutes,
        "order_time_hour":order_time_hour,
        "distance":distance
    }])

    prediction = model.predict(input_data)

    st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")