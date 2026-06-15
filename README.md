# Customer Churn Prediction Using Machine Learning

## Overview

Customer retention is a critical business objective, as acquiring new customers is often more expensive than retaining existing ones. This project focuses on predicting customer churn using Machine Learning techniques. The goal is to identify customers who are likely to discontinue a company's services, enabling businesses to take proactive retention measures.

## Business Problem

Customer churn directly impacts revenue and growth. By accurately predicting churn behavior, organizations can target at-risk customers with personalized retention strategies, improve customer satisfaction, and reduce revenue loss.

## Project Objectives

* Analyze customer demographic and service-related data.
* Identify key factors influencing customer churn.
* Build and compare multiple Machine Learning classification models.
* Select the best-performing model based on evaluation metrics.
* Create a reusable predictive model for future customer churn analysis.

## Dataset Description

The dataset contains customer information collected from a telecommunications company. Features include:

### Customer Information

* Gender
* Senior Citizen Status
* Partner Status
* Dependents

### Service Information

* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Technical Support
* Streaming TV
* Streaming Movies

### Account Information

* Contract Type
* Payment Method
* Monthly Charges
* Total Charges
* Tenure

### Target Variable

* Churn (Yes/No)

## Methodology

### 1. Data Collection

* Imported the customer churn dataset into Python.
* Examined dataset structure, feature types, and target variable distribution.

### 2. Data Preprocessing

* Checked for missing values and handled them appropriately.
* Converted categorical variables into numerical representations using encoding techniques.
* Removed unnecessary columns where required.
* Performed feature scaling for algorithms sensitive to feature magnitude.
* Split the dataset into training and testing sets.

### 3. Exploratory Data Analysis (EDA)

* Analyzed customer demographics and service usage patterns.
* Studied churn distribution across different customer segments.
* Identified relationships between customer attributes and churn behavior.
* Used visualizations to uncover trends and patterns within the data.

### 4. Model Development

Multiple classification algorithms were trained and evaluated:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Gaussian Naive Bayes
* Gradient Boosting Classifier

### 5. Model Evaluation

Each model was evaluated using:

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Confusion Matrix

These metrics provided a comprehensive assessment of model performance and classification capability.

### 6. Model Selection

After comparing all models, the best-performing algorithm was selected based on overall performance metrics and generalization ability on unseen test data.

### 7. Model Serialization

The final trained model was saved using Joblib/Pickle, allowing it to be reused for deployment and future predictions without retraining.

## Results

The selected model achieved strong predictive performance in identifying customers likely to churn.

### Best Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 82.04% |
| Precision | 68.40% |
| Recall    | 59.79% |
| F1 Score  | 63.81% |

### Confusion Matrix

| Actual / Predicted | No Churn | Churn |
| ------------------ | -------- | ----- |
| No Churn           | 933      | 103   |
| Churn              | 150      | 223   |

The model demonstrates a good balance between overall accuracy and churn detection capability.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Jupyter Notebook

## Project Structure

Customer-Churn-Prediction/

├── Data/

│   └── customer_churn.csv

├── Notebook/

│   └── Customer_Churn_Prediction.ipynb

├── Model/

│   └── churn_model.pkl

├── requirements.txt

├── README.md

└── app.py

## Key Learnings

Through this project, I gained practical experience in:

* Data preprocessing and feature engineering
* Exploratory Data Analysis (EDA)
* Classification algorithms
* Model evaluation techniques
* Confusion matrix interpretation
* Machine Learning workflow implementation
* Model serialization and deployment preparation

## Future Enhancements

* Hyperparameter tuning using GridSearchCV.
* Feature selection for improved performance.
* Implementation of advanced boosting algorithms such as XGBoost and LightGBM.
* Deployment using Flask or Streamlit.
* Real-time churn prediction dashboard development.

## Author

### Manoranjan Behera

---

This project demonstrates a Machine Learning workflow, from data preprocessing and exploratory analysis to model development, evaluation.