# Customer Churn Prediction

## Project Overview

This project predicts whether a telecom customer is likely to churn (leave the service) based on customer demographics, account information, and service usage details. The objective is to help businesses identify at-risk customers and improve customer retention strategies.

## Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Label Encoding and One-Hot Encoding
* Feature Scaling using StandardScaler
* Machine Learning Model Training and Evaluation
* Customer Churn Prediction Web Application using Streamlit
* Model Deployment

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

## Dataset Features

The model uses customer information such as:

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Paperless Billing
* Monthly Charges
* Total Charges
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract Type
* Payment Method

## Machine Learning Workflow

1. Data Cleaning
2. Exploratory Data Analysis
3. Label Encoding for Binary Features
4. One-Hot Encoding for Multi-Class Features
5. Feature Scaling using StandardScaler
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Deployment using Streamlit

## Model Performance

* Algorithm: Logistic Regression
* Accuracy: 82.04%
* Precision: 68.40%
* Recall: 59.79%
* F1 Score: 63.81%

## Deployment

The trained Logistic Regression model was deployed using Streamlit, allowing users to enter customer information and receive real-time churn predictions.

## Project Structure

Customer-Churn-Prediction/

├── app.py

├── Customer_Churn.pkl

├── scaler.pkl

├── requirements.txt

├── README.md

└── Customer_Churn_Prediction.ipynb

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author

Manoranjan Behera

Aspiring Machine Learning Engineer
