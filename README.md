# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a telecom customer is likely to churn and provides a churn probability to support customer retention decisions.

The project includes data preprocessing, exploratory data analysis, feature engineering, machine learning model development, model evaluation, feature analysis, and a Streamlit web application for making customer-level predictions.

---

## 🚀 Live Demo

👉 [Try the Customer Churn Prediction App](https://customer-churn-prediction-cb5owmzbyqhqejguheqsnq.streamlit.app/)

---

## 📌 Project Overview

Customer churn is an important business problem for subscription-based companies. Identifying customers who are likely to leave can help businesses take preventive retention actions.

In this project, a **Logistic Regression** model is trained on the **Telco Customer Churn** dataset to predict customer churn.

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

### 📅 Tenure

Customers with shorter tenure showed a higher likelihood of churn.

Churned customers generally had considerably shorter tenure than customers who stayed.

### 💰 Monthly Charges

Customers who churned generally had higher monthly charges compared with customers who stayed.

### 📄 Contract Type

Month-to-month customers showed the highest churn compared with customers on longer-term contracts.

### 🌐 Internet Service

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
```

---

## 🌲 Random Forest Comparison

A Random Forest classifier was also trained to compare its performance with Logistic Regression.

The Random Forest model achieved approximately **78.96% accuracy**, while the Logistic Regression model achieved **80.38% accuracy**.

Based on the overall evaluation, Logistic Regression was selected as the final model.

---

## 📊 Model Evaluation

### Logistic Regression Performance

| Metric | Score |
|---|---:|
| Accuracy | 80.38% |
| Churn Precision | 65% |
| Churn Recall | 57% |
| Churn F1-Score | 61% |

### Confusion Matrix

| | Predicted No Churn | Predicted Churn |
|---|---:|---:|
| **Actual No Churn** | 916 | 117 |
| **Actual Churn** | 159 | 215 |

The model correctly identified a significant portion of customers who were likely to churn while maintaining approximately **80% overall accuracy**.

---

## ⚖️ Class Imbalance

The dataset contains more customers who stayed than customers who churned.

Original churn distribution:

- **No Churn:** 73.42%
- **Churn:** 26.58%

A class-weighted Logistic Regression model was also tested.

The balanced model improved churn recall to approximately **80%**, but overall accuracy decreased to approximately **73%**.

Therefore, the original Logistic Regression model was selected because it provided a better overall balance between accuracy, precision, recall, and F1-score for this project.

---

## 🔎 Feature Importance

Feature importance was analyzed using the Logistic Regression coefficients.

The strongest features by absolute coefficient magnitude included:

1. Tenure
2. Monthly Charges
3. Internet Service — Fiber Optic
4. Total Charges
5. Contract — Two Year
6. Contract — One Year
7. Streaming TV
8. Streaming Movies
9. Multiple Lines
10. Payment Method — Electronic Check

These features provide useful business insights into customer churn patterns.

> Note: Logistic Regression coefficients indicate statistical associations within the trained model and should not be interpreted as proof of causation.

---

## 🖥️ Streamlit Application

The trained model was integrated into a Streamlit web application.

The application allows users to enter customer information such as:

- Senior citizen status
- Tenure
- Monthly charges
- Total charges
- Contract type
- Internet service
- Payment method
- Online security
- Technical support
- Streaming services
- Other customer service details

The application then provides:

- Churn prediction
- Churn probability
- Risk assessment
- Recommended business action
- Customer summary

---

## ⚠️ Risk Assessment

The application classifies customers into three risk levels based on predicted churn probability:

### 🔴 High Risk

Customers with a churn probability of **70% or higher**.

Recommended actions may include:

- Retention discounts
- Contract upgrades
- Personalized support
- Targeted retention campaigns

### 🟡 Medium Risk

Customers with a churn probability between **40% and 69.99%**.

Recommended actions may include:

- Targeted offers
- Customer support
- Encouraging longer-term contracts

### 🟢 Low Risk

Customers with a churn probability below **40%**.

Customers can continue to be monitored while maintaining good service quality.

---

## 📸 Project Screenshots

### Streamlit Application
![Streamlit Application](https://raw.githubusercontent.com/chandudesireddy7/Customer-Churn-Prediction/main/images/app_home.png)


### Churn Prediction

![Churn Prediction](https://raw.githubusercontent.com/chandudesireddy7/Customer-Churn-Prediction/main/images/churn_prediction.png)

### Risk Assessment

![Risk Assessment](https://raw.githubusercontent.com/chandudesireddy7/Customer-Churn-Prediction/main/images/risk_assessment.png)

### Project Overview

![Project Overview](https://raw.githubusercontent.com/chandudesireddy7/Customer-Churn-Prediction/main/images/project_overview.png)

---

## 📁 Project Structure

```text
Customer_Churn_Prediction/
│
├── app.py
├── churn_model.pkl
├── scaler.pkl
├── Customer_Churn_Prediction.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── README.md
├── requirements.txt
├── .gitignore
│
└── images/
    ├── app_home.png
    ├── churn_prediction.png
    ├── risk_assessment.png
    └── project_overview.png
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- Joblib
- Streamlit
- Git
- GitHub

---

## ▶️ How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/chandudesireddy7/Customer-Churn-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Customer-Churn-Prediction
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📈 Example Prediction

The application generates a churn probability for each customer.

For example:

**Churn Probability:** Approximately 83.40%

The customer would therefore be classified as **High Risk** according to the application's risk thresholds.

---

## 🔮 Future Improvements

Possible future improvements include:

- Hyperparameter tuning
- Trying additional machine learning algorithms
- Cross-validation
- Improving churn recall while maintaining precision
- Feature importance visualization
- Model comparison dashboard
- Customer retention campaign analysis
- Downloadable prediction reports
- Deployment improvements
- Monitoring model performance over time

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Feature engineering
- Categorical encoding
- Feature scaling
- Classification algorithms
- Model evaluation
- Confusion matrix analysis
- Handling class imbalance
- Feature importance analysis
- Model deployment
- Streamlit application development
- Git and GitHub version control

---

## 👨‍💻 Author

**Desireddy Chandan Kumar Reddy**

Computer Science and Engineering Student

GitHub: [chandudesireddy7](https://github.com/chandudesireddy7)

---

⭐ If you found this project useful, feel free to explore the repository and try the live application.