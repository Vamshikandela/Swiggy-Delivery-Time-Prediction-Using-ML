# 🚚 Swiggy Delivery Time Prediction

## 📌 Project Overview

Food delivery platforms such as Swiggy process thousands of orders daily across multiple cities. Providing customers with an accurate Estimated Time of Arrival (ETA) is critical for maintaining trust and ensuring a smooth delivery experience.

This project leverages Machine Learning to predict food delivery time (in minutes) using real-world factors such as rider information, traffic conditions, weather, order characteristics, distance, and city-specific attributes.

Using a dataset containing over **45,000 delivery records**, multiple regression models were trained and evaluated, with **XGBoost Regressor** emerging as the best-performing model, achieving an **R² Score of 81.57%**.

---

## 🎯 Business Objective

Inaccurate delivery estimates can result in:

* Customer dissatisfaction
* Increased order cancellations
* Higher support ticket volume
* Inefficient rider allocation
* Reduced customer retention

A reliable ETA prediction system helps:

* Improve customer trust and satisfaction
* Optimize delivery partner assignments
* Reduce order cancellations
* Enhance operational efficiency
* Improve overall delivery performance

---

## ❓ Problem Statement

Develop a Machine Learning model capable of predicting food delivery time based on historical delivery data and real-time operational factors.

The model should consider:

* Distance between restaurant and customer
* Traffic conditions
* Weather conditions
* Order timing information
* Rider attributes
* City-specific factors
* Delivery workload indicators

---

## 📊 Dataset Information

The dataset contains **45,000+ delivery records** and includes information related to riders, orders, locations, environmental conditions, and delivery performance.

### Key Features

| Feature             | Description                     |
| ------------------- | ------------------------------- |
| Rider_ID            | Unique rider identifier         |
| Age                 | Rider age                       |
| Ratings             | Rider performance rating        |
| Vehicle_Condition   | Vehicle condition score         |
| Type_of_Vehicle     | Vehicle category                |
| Type_of_Order       | Order category                  |
| Multiple_Deliveries | Number of deliveries assigned   |
| Pickup_Time_Minutes | Restaurant preparation time     |
| Distance            | Delivery distance               |
| Weather             | Weather conditions              |
| Traffic             | Traffic intensity               |
| Festival            | Festival indicator              |
| City_Type           | Urban/Metropolitan/Semi-Urban   |
| Order_Time_Hour     | Hour of order placement         |
| Order_Time_Of_Day   | Morning/Afternoon/Evening/Night |
| Order_Day           | Day of month                    |
| Order_Month         | Month                           |
| Order_Day_Of_Week   | Weekday                         |
| Time_Taken          | Target Variable (Delivery Time) |

---

# 🔄 Machine Learning Pipeline

### Step 1: Business Understanding

* Defined the ETA prediction problem.
* Identified key business challenges caused by inaccurate delivery estimates.

### Step 2: Data Understanding

* Explored dataset structure and feature distributions.
* Performed statistical analysis and data quality assessment.

### Step 3: Data Cleaning

* Handled missing values.
* Removed inconsistencies and invalid records.
* Corrected data types.

### Step 4: Exploratory Data Analysis (EDA)

* Analyzed delivery patterns.
* Examined relationships between distance, traffic, weather, and delivery time.
* Visualized feature distributions and correlations.

### Step 5: Feature Engineering

* Created time-based features.
* Generated distance-related variables.
* Extracted useful insights from categorical attributes.

### Step 6: Data Preprocessing

* Encoded categorical variables using:

  * OneHotEncoder
  * OrdinalEncoder
* Scaled numerical features using:

  * MinMaxScaler

### Step 7: Feature Selection

* Selected the most relevant features using:

  * SelectKBest

### Step 8: Model Development

Trained multiple regression models:

* Decision Tree Regressor
* Random Forest Regressor
* AdaBoost Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

### Step 9: Model Evaluation

Evaluated model performance using:

* R² Score
* RMSE (Root Mean Squared Error)

### Step 10: Model Selection

* Compared all models.
* Selected XGBoost Regressor as the final model.

### Step 11: Model Deployment

* Saved the trained model using Pickle.
* Developed an interactive Streamlit application.
* Enabled real-time delivery time prediction.

---

## 🤖 Model Performance

### Best Model: XGBoost Regressor

**Performance Metrics**

* R² Score: **81.57%**
* Dataset Size: **45,000+ Records**
* Problem Type: **Regression**

---

## 🚀 Deployment

The final model was deployed using Streamlit.

### Features

* Real-time ETA prediction
* Interactive user interface
* Dynamic input forms
* Easy-to-use web application

Run Locally:

```bash
streamlit run app.py
```

---

## 🛠️ Technology Stack

### Programming & Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)

### Machine Learning

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-102230?style=for-the-badge)

### Data Visualization

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge)

### Deployment

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)

### Version Control

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)

---

## 📂 Project Structure

```text
Swiggy-Delivery-Time-Prediction
│
├── data/
│   └── swiggy_dataset.csv
│
├── notebook/
│   └── Swiggy_Delivery_Time_Prediction.ipynb
│
├── model/
│   └── model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔮 Future Enhancements

* Integrate live traffic APIs
* Implement cloud deployment (AWS/Azure/GCP)
* Containerize using Docker
* Develop real-time ETA monitoring
* Experiment with deep learning models

---

## 👨‍💻 Author

**Vamshi Kandela**

Data Science & Machine Learning Enthusiast

📧 Email: vamshikandela29@gmail.com 

🔗 LinkedIn: https://www.linkedin.com/in/kandela-vamshi-2b4457258
