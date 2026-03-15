# Project Overview

Food delivery platforms like Swiggy handle thousands of orders every day across multiple cities. One of the most critical aspects of the customer experience is providing an accurate Estimated Time of Arrival (ETA) for food delivery.

This project builds a Machine Learning model to predict the delivery time (in minutes) for an order using various real-world features such as:

- Rider information

- Traffic conditions

- Weather conditions

- Distance between restaurant and customer

**Order details**

City and time related factors

**The goal is to improve ETA accuracy so that customers receive reliable delivery time estimates.**

 # Business Problem

Accurate delivery time prediction is important because inaccurate ETAs can lead to:

-- Customer dissatisfaction

 --Order cancellations

-- Increased support requests

-- Poor delivery partner allocation

**A reliable ETA prediction system helps Swiggy:**

Improve customer trust

Optimize rider assignment

Reduce cancellations

Improve operational efficiency

# Problem Statement

Build a machine learning model that predicts the delivery time (minutes) for each order using historical delivery data.

The model should use multiple real-time factors such as:

Weather

Traffic

Distance

Order time

Rider information

City details

# Dataset Description

The dataset contains multiple features related to orders, riders, locations, and environmental conditions.

Feature	Description
Rider_id	Unique ID of delivery partner
Age	Age of delivery partner
Ratings	Average rider rating
vehicle_condition	Condition of delivery vehicle
Type_of_vehicle	Type of vehicle used
Type_of_order	Type of food ordered
multiple_deliveries	Number of deliveries handled together
pickup_time_minutes	Restaurant preparation time
restaurant_longitude	Restaurant location
delivery_longitude	Customer delivery location
Is_weekend	Whether order was on weekend
Order_time_hour	Hour of order placement
order_time_of_day	Time category (morning, afternoon, evening, night)
Weather	Weather conditions
Traffic	Traffic conditions
Festival	Whether it was a festival day
City_type	Urban / Metropolitan / Semi-Urban
City_name	City code
Distance	Distance between restaurant and delivery location
Order_day	Day of month
Order_month	Month of order
order_day_of_week	Day of week
Time_taken	Target variable (delivery time in minutes)
⚙️ Machine Learning Pipeline

The project follows the CRISP-ML(Q) methodology for building the model.

Steps followed:

 Business Understanding
 Data Understanding
 Data Preprocessing
 Feature Engineering
 Model Building
 Model Evaluation
Model Deployment

# Data Preprocessing

The following preprocessing steps were performed:

Handling missing values

Feature engineering (time features)

Encoding categorical variables

Feature scaling

Feature selection

## Techniques used:

OneHotEncoder

OrdinalEncoder

MinMaxScaler

SelectKBest

## Machine Learning Models Used

Several regression models were tested:

Decision Tree Regressor

Random Forest Regressor

AdaBoost Regressor

Gradient Boosting Regressor

XGBoost Regressor (Best Model)

The XGBoost model performed best in predicting delivery time.

##  Model Evaluation Metrics

The models were evaluated using:

R² Score

Root Mean Squared Error (RMSE)

These metrics measure how accurately the model predicts delivery time.

 # Model Deployment
The trained model was deployed using Streamlit, allowing users to input order details and predict delivery time.

Streamlit Features

User-friendly interface

Real-time prediction

Interactive input fields

Visual Swiggy banner

Run the app:

streamlit run app.py
## Technologies Used

- Python

- Pandas

- NumPy

- Scikit-learn

- XGBoost

- Streamlit


Project Structure
Swiggy-Delivery-Time-Prediction
│
├── data
│   └── swiggy_dataset.csv
│
├── notebook
│   └── Swiggy Delivery Time Prediction.ipynb
│
├── model
│   └── model.pkl
│
├── app.py
├── requirements.txt
└── README.md
## Example Prediction

Input features:

Distance = 5 km

Traffic = High

Weather = Cloudy

Multiple Deliveries = 2

Predicted output:

Estimated Delivery Time: 32 minutes
##  Future Improvements

Add live traffic APIs

Use deep learning models

Deploy using Docker or cloud platforms

Add real-time ETA updates

## Author

Vamshi Kandela

Machine Learning & Data Science Enthusiast
