import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import joblib

scaler = joblib.load('scaler.pkl')
model = joblib.load("Customer_Churn.pkl")

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
tenure = st.number_input("Tenure", min_value=0)
Phone_service = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internetservice = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streming TV", ["Yes", "No", "No internet service"])
StreamingMovie = st.selectbox("Streming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
paperlessbilling = st.selectbox("Paper less billing", ["Yes", "No"])
paymet_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'])

monthly = st.number_input("Monthly Charges", min_value=0.0)
total = st.number_input("Total Charges", min_value=0.0)

if st.button("Predict"):

    train_columns = [
    'gender',
    'SeniorCitizen',
    'Partner',
    'Dependents',
    'tenure',
    'PhoneService',
    'PaperlessBilling',
    'MonthlyCharges',
    'TotalCharges',
    'MultipleLines_No phone service',
    'MultipleLines_Yes',
    'InternetService_Fiber optic',
    'InternetService_No',
    'OnlineSecurity_No internet service',
    'OnlineSecurity_Yes',
    'OnlineBackup_No internet service',
    'OnlineBackup_Yes',
    'DeviceProtection_No internet service',
    'DeviceProtection_Yes',
    'TechSupport_No internet service',
    'TechSupport_Yes',
    'StreamingTV_No internet service',
    'StreamingTV_Yes',
    'StreamingMovies_No internet service',
    'StreamingMovies_Yes',
    'Contract_One year',
    'Contract_Two year',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check'
    ]

    #Label Encoder

    gender = 1 if gender == "Male" else 0
    senior = 1 if senior == "Yes" else 0
    partner = 1 if partner == "Yes" else 0
    dependents = 1 if dependents == "Yes" else 0
    phone_service = 1 if Phone_service == "Yes" else 0
    paperless_billing = 1 if paperlessbilling == "Yes" else 0

    #Convert Dataframe
    input_df = pd.DataFrame(
        {
            "gender": [gender],
            "Senior Citizen": [senior],
            "Partner": [partner],
            "dependent": [dependents],
            "tenure": [tenure],
            "Phone service": [phone_service],
            "multiservice": [MultipleLines],
            "internetservice": [internetservice],
            "onlinesecurity": [online_security],
            "onlinebackup": [online_backup],
            "deviceprotection": [DeviceProtection],
            "techsupport": [TechSupport],
            "StreamTV": [StreamingTV],
            "StreamMovies": [StreamingTV],
            "Contract": [Contract],
            "paperlessbill": [paperless_billing],
            "Paymentmethod": [paymet_method],
            "Monthlycharges": [monthly],
            "totalcharges": [total]
        }
    )

    input_df = pd.get_dummies(input_df, drop_first=True) # splitted the features 
    input_df = input_df.astype(int) #boolean value convert to integer

    input_df = input_df.reindex(columns=train_columns, fill_value=0)

    input_scale = scaler.transform(input_df)
    prediction = model.predict(input_scale)

    if prediction[0] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is not likely to churn")


