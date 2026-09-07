import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown(
    """
    <style>

    /* Main application */
    .main {
        padding-top: 2rem;
    }

    /* Main title */
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
    }

    /* Section headings */
    h2, h3 {
        font-weight: 600;
    }

    /* Prediction button */
    .stButton > button {
        width: 100%;
        padding: 0.75rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
    }

    /* Metric styling */
    [data-testid="stMetric"] {
        padding: 15px;
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL AND SCALER
# =========================================================

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📊 Churn Prediction")

st.sidebar.markdown(
    """
    ### About This Project

    This application uses a Machine Learning model
    to predict whether a telecom customer is likely
    to churn.

    **Model:** Logistic Regression

    **Dataset:** Telco Customer Churn

    **Purpose:** Customer Retention Analysis
    """
)

st.sidebar.divider()

st.sidebar.info(
    "Enter customer details and click "
    "'Predict Churn' to generate a prediction."
)

st.sidebar.divider()

st.sidebar.subheader("📈 Model Performance")

st.sidebar.write("**Accuracy:** 80.38%")
st.sidebar.write("**Churn Recall:** 57%")
st.sidebar.write("**Churn F1-Score:** 61%")
# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📊 Churn Prediction")

st.sidebar.markdown(
    """
    ## 📌 Project Overview

    A Machine Learning application designed to
    predict telecom customer churn and support
    customer retention decisions.
    """
)

st.sidebar.divider()

st.sidebar.subheader("🤖 Model")

st.sidebar.write(
    "**Algorithm:** Logistic Regression"
)

st.sidebar.write(
    "**Problem:** Binary Classification"
)

st.sidebar.write(
    "**Target:** Customer Churn"
)

st.sidebar.divider()

st.sidebar.subheader("📈 Model Performance")

st.sidebar.metric(
    "Accuracy",
    "80.38%"
)

st.sidebar.metric(
    "Churn Recall",
    "57%"
)

st.sidebar.metric(
    "Churn F1-Score",
    "61%"
)

st.sidebar.divider()

st.sidebar.info(
    "💡 Enter customer details and click "
    "'Predict Churn' to generate a prediction."
)

# =========================================================
# MAIN TITLE
# =========================================================

# =========================================================
# PROJECT HEADER
# =========================================================

st.title("📊 Customer Churn Prediction")

st.markdown(
    """
    ### Predict customer churn using Machine Learning

    This application analyzes customer information and estimates
    the probability that a telecom customer will churn.

    **Model:** Logistic Regression &nbsp; | &nbsp;
    **Dataset:** Telco Customer Churn &nbsp; | &nbsp;
    **Purpose:** Customer Retention Analysis
    """
)

st.divider()


# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=80.0
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )


with col2:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=960.0
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )


# =========================================================
# FAMILY & PHONE SERVICES
# =========================================================

st.subheader("📞 Family & Phone Services")

col1, col2 = st.columns(2)

with col1:

    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )


with col2:

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No phone service", "No", "Yes"]
    )


# =========================================================
# INTERNET SERVICES
# =========================================================

st.subheader("🌐 Internet Services")

col1, col2 = st.columns(2)

with col1:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No internet service", "No", "Yes"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No internet service", "No", "Yes"]
    )


with col2:

    device_protection = st.selectbox(
        "Device Protection",
        ["No internet service", "No", "Yes"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No internet service", "No", "Yes"]
    )


# =========================================================
# STREAMING SERVICES
# =========================================================

st.subheader("📺 Streaming Services")

col1, col2 = st.columns(2)

with col1:

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No internet service", "No", "Yes"]
    )


with col2:

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No internet service", "No", "Yes"]
    )


# =========================================================
# CONTRACT & BILLING
# =========================================================

st.subheader("💳 Contract & Billing")

col1, col2 = st.columns(2)

with col1:

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )


with col2:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )


# =========================================================
# PREDICTION
# =========================================================

st.divider()

if st.button("🔮 Predict Churn"):

    # -----------------------------------------------------
    # CREATE CUSTOMER DATA
    # -----------------------------------------------------

    customer_data = {

        "SeniorCitizen":
            1 if senior_citizen == "Yes" else 0,

        "tenure":
            tenure,

        "MonthlyCharges":
            monthly_charges,

        "TotalCharges":
            total_charges,

        "gender_Male":
            1 if gender == "Male" else 0,

        "Partner_Yes":
            1 if partner == "Yes" else 0,

        "Dependents_Yes":
            1 if dependents == "Yes" else 0,

        "PhoneService_Yes":
            1 if phone_service == "Yes" else 0,

        "MultipleLines_No phone service":
            1 if multiple_lines == "No phone service" else 0,

        "MultipleLines_Yes":
            1 if multiple_lines == "Yes" else 0,

        "InternetService_Fiber optic":
            1 if internet_service == "Fiber optic" else 0,

        "InternetService_No":
            1 if internet_service == "No" else 0,

        "OnlineSecurity_No internet service":
            1 if online_security == "No internet service" else 0,

        "OnlineSecurity_Yes":
            1 if online_security == "Yes" else 0,

        "OnlineBackup_No internet service":
            1 if online_backup == "No internet service" else 0,

        "OnlineBackup_Yes":
            1 if online_backup == "Yes" else 0,

        "DeviceProtection_No internet service":
            1 if device_protection == "No internet service" else 0,

        "DeviceProtection_Yes":
            1 if device_protection == "Yes" else 0,

        "TechSupport_No internet service":
            1 if tech_support == "No internet service" else 0,

        "TechSupport_Yes":
            1 if tech_support == "Yes" else 0,

        "StreamingTV_No internet service":
            1 if streaming_tv == "No internet service" else 0,

        "StreamingTV_Yes":
            1 if streaming_tv == "Yes" else 0,

        "StreamingMovies_No internet service":
            1 if streaming_movies == "No internet service" else 0,

        "StreamingMovies_Yes":
            1 if streaming_movies == "Yes" else 0,

        "Contract_One year":
            1 if contract == "One year" else 0,

        "Contract_Two year":
            1 if contract == "Two year" else 0,

        "PaperlessBilling_Yes":
            1 if paperless_billing == "Yes" else 0,

        "PaymentMethod_Credit card (automatic)":
            1 if payment_method == "Credit card (automatic)" else 0,

        "PaymentMethod_Electronic check":
            1 if payment_method == "Electronic check" else 0,

        "PaymentMethod_Mailed check":
            1 if payment_method == "Mailed check" else 0
    }


    # -----------------------------------------------------
    # CONVERT TO DATAFRAME
    # -----------------------------------------------------

    customer_df = pd.DataFrame([customer_data])


    # -----------------------------------------------------
    # SCALE DATA
    # -----------------------------------------------------

    customer_scaled = scaler.transform(customer_df)


    # -----------------------------------------------------
    # MAKE PREDICTION
    # -----------------------------------------------------

    prediction = model.predict(customer_scaled)[0]


    # -----------------------------------------------------
    # CALCULATE CHURN PROBABILITY
    # -----------------------------------------------------

    churn_probability = (
        model.predict_proba(customer_scaled)[0][1] * 100
    )


    # =====================================================
    # PREDICTION RESULT
    # =====================================================

    st.subheader("📊 Prediction Result")

    result_col1, result_col2 = st.columns(2)


    with result_col1:

        if prediction == 1:

            st.error(
                "🔴 Customer is likely to CHURN"
            )

        else:

            st.success(
                "🟢 Customer is likely to STAY"
            )


    with result_col2:

        st.metric(
            "Churn Probability",
            f"{churn_probability:.2f}%"
        )


        # =====================================================
    # RISK LEVEL
    # =====================================================

    st.subheader("⚠️ Risk Assessment")

    if churn_probability >= 70:

        risk_level = "HIGH RISK"
        st.error(
            f"🔴 {risk_level} — Immediate retention action recommended."
        )

    elif churn_probability >= 40:

        risk_level = "MEDIUM RISK"
        st.warning(
            f"🟡 {risk_level} — Customer should be monitored."
        )

    else:

        risk_level = "LOW RISK"
        st.success(
            f"🟢 {risk_level} — Customer is less likely to churn."
        )


    # =====================================================
    # BUSINESS RECOMMENDATION
    # =====================================================

    st.subheader("💡 Recommended Action")

    if churn_probability >= 70:

        st.write(
            "🚨 High-risk customer. Consider offering a "
            "retention discount, contract upgrade, or "
            "personalized support."
        )

    elif churn_probability >= 40:

        st.write(
            "⚠️ Medium-risk customer. Consider targeted "
            "offers, customer support, or encouraging a "
            "longer-term contract."
        )

    else:

        st.write(
            "✅ Low-risk customer. Continue providing good "
            "service and monitor the customer over time."
        )


    # =====================================================
    # CUSTOMER SUMMARY
    # =====================================================

    st.divider()

    st.subheader("📋 Customer Summary")

    summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

    with summary_col1:
        st.metric(
            "Tenure",
            f"{tenure} months"
        )

    with summary_col2:
        st.metric(
            "Monthly Charges",
            f"${monthly_charges:.2f}"
        )

    with summary_col3:
        st.metric(
            "Contract",
            contract
        )

    with summary_col4:
        st.metric(
            "Internet Service",
            internet_service
        )


    # =====================================================
    # CHURN PROBABILITY CHART
    # =====================================================

    st.subheader("📈 Churn Probability")

    probability_data = pd.DataFrame(
        {
            "Risk": ["Churn", "Stay"],
            "Probability": [
                churn_probability,
                100 - churn_probability
            ]
        }
    )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.metric(
            "Churn Probability",
            f"{churn_probability:.2f}%"
        )

    with chart_col2:
        st.metric(
            "Stay Probability",
            f"{100 - churn_probability:.2f}%"
        )

    st.bar_chart(
        probability_data.set_index("Risk")
    )

# =========================================================
# KEY INSIGHTS
# =========================================================

st.divider()

st.subheader("💡 Key Business Insights")

insight_col1, insight_col2, insight_col3 = st.columns(3)

with insight_col1:

    st.info(
        """
        **📅 Customer Tenure**

        Customers with shorter tenure tend to have
        a higher likelihood of churn.
        """
    )

with insight_col2:

    st.info(
        """
        **💰 Monthly Charges**

        Customers with higher monthly charges show
        a greater tendency toward churn.
        """
    )

with insight_col3:

    st.info(
        """
        **📄 Contract Type**

        Month-to-month customers generally have
        higher churn compared with longer-term contracts.
        """
    )
# =========================================================
# ABOUT THE MODEL
# =========================================================

st.divider()

st.subheader("🤖 About the Model")

model_col1, model_col2 = st.columns(2)

with model_col1:

    st.markdown(
        """
        **Logistic Regression**

        Logistic Regression is a classification algorithm
        used to estimate the probability of a customer
        belonging to a particular class.

        In this project, the model predicts two outcomes:

        - 🟢 Customer is likely to stay
        - 🔴 Customer is likely to churn
        """
    )

with model_col2:

    st.markdown(
        """
        **Model Evaluation**

        The model was evaluated using multiple performance
        metrics:

        - **Accuracy:** 80.38%
        - **Churn Recall:** 57%
        - **Churn F1-Score:** 61%

        These metrics help evaluate how well the model
        identifies customers who may churn.
        """
    )
# =========================================================
# PROJECT STATUS
# =========================================================

st.divider()

status_col1, status_col2, status_col3 = st.columns(3)

with status_col1:
    st.metric(
        "Model",
        "Logistic Regression"
    )

with status_col2:
    st.metric(
        "Accuracy",
        "80.38%"
    )

with status_col3:
    st.metric(
        "Application",
        "Streamlit"
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Customer Churn Prediction | "
    "Machine Learning Project | "
    "Built with Python & Streamlit"
)