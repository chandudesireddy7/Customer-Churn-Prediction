# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a telecom customer is likely to churn and provides a churn probability to support customer retention decisions.

The project includes data preprocessing, exploratory data analysis, feature engineering, machine learning model development, model evaluation, feature analysis, and a Streamlit web application for making customer-level predictions.

---

## 🚀 Project Overview

Customer churn is an important business problem for subscription-based companies. Identifying customers who are likely to leave can help businesses take preventive retention actions.

In this project, a **Logistic Regression** model is trained on the Telco Customer Churn dataset to predict customer churn.

The final model achieves:

- **Accuracy:** 80.38%
- **Churn Recall:** 57%
- **Churn F1-Score:** 61%

The trained model is integrated into a **Streamlit web application**, where users can enter customer details and receive a churn prediction and probability.

---

## 🎯 Business Problem

Telecom companies can lose significant revenue when customers discontinue their services.

The objective of this project is to:

- Identify customers who are likely to churn.
- Estimate the probability of customer churn.
- Understand important factors associated with churn.
- Provide actionable retention recommendations.
- Build an interactive application for customer-level predictions.

---

## 📂 Dataset

The project uses the **Telco Customer Churn** dataset.

The original dataset contains:

- **7,043 rows**
- **21 columns**

The dataset contains customer information related to:

- Demographics
- Customer tenure
- Phone services
- Internet services
- Online security
- Online backup
- Device protection
- Technical support
- Streaming services
- Contract type
- Payment method
- Monthly charges
- Total charges
- Customer churn

The `customerID` column was removed because it is an identifier and does not provide useful predictive information.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the Telco Customer Churn dataset.
2. Examined the structure and data types.
3. Identified missing values.
4. Converted `TotalCharges` from object/string format to numeric.
5. Handled the resulting missing values.
6. Removed the `customerID` identifier.
7. Converted the target variable:
   - `No` → `0`
   - `Yes` → `1`
8. Applied one-hot encoding to categorical variables.
9. Split the dataset into training and testing sets.
10. Applied feature scaling for Logistic Regression.

After preprocessing and encoding:

- **Rows:** 7,032
- **Features:** 30

---

## 🔍 Exploratory Data Analysis

Exploratory analysis was performed to understand the relationship between customer characteristics and churn.

### Key Findings

#### 📅 Tenure

Customers with shorter tenure showed a higher likelihood of churn.

Churned customers generally had considerably shorter tenure than customers who stayed.

#### 💰 Monthly Charges

Customers who churned generally had higher monthly charges compared with customers who stayed.

#### 📄 Contract Type

Month-to-month customers showed the highest churn compared with customers on longer-term contracts.

#### 🌐 Internet Service

Customers using fiber optic internet showed relatively higher churn compared with other internet service categories.

These observations helped provide business context for the machine learning model.

---

## 🤖 Machine Learning

### Logistic Regression

Logistic Regression was selected as the primary classification model because the project involves a binary target:

- `0` → Customer stays
- `1` → Customer churns

The model was trained after applying `StandardScaler` to the input features.

```python
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)

model.fit(X_train_scaled, y_train)
## 📸 Project Screenshots

### Streamlit Application
![Streamlit Application](images/app_home.png)

### Churn Prediction
![Churn Prediction](images/churn_prediction.png)

### Risk Assessment
![Risk Assessment](images/risk_assessment.png)

### Project Overview
![Project Overview](images/project_overview.png)