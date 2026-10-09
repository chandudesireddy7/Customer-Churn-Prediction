import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
import os
from datetime import datetime

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# GLASS-NEOMORPHISM DESIGN SYSTEM
# =========================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }

    /* Soft Neomorphic Canvas */
    .stApp {
        background: linear-gradient(145deg, #EBF1F8 0%, #F4F8FC 50%, #E8F0F8 100%);
        color: #0F172A;
    }

    /* Top Brand Hero Banner (Frosted Glass + Neomorphic Depth) */
    .neo-glass-banner {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.92) 0%, rgba(37, 99, 235, 0.88) 100%);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1.5px solid rgba(255, 255, 255, 0.5);
        border-radius: 24px;
        padding: 2rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 12px 12px 28px rgba(163, 177, 198, 0.45),
                    -10px -10px 24px rgba(255, 255, 255, 0.9);
        color: #FFFFFF !important;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 1.5rem;
    }

    .banner-title {
        font-family: 'Outfit', sans-serif;
        font-size: 2.35rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: #FFFFFF !important;
        margin: 0;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }

    .banner-meaning {
        background: rgba(255, 255, 255, 0.12);
        border-left: 3px solid #93C5FD;
        border-radius: 8px;
        padding: 0.6rem 0.9rem;
        margin-top: 0.75rem;
        font-size: 0.88rem;
        color: #EFF6FF !important;
        max-width: 820px;
        line-height: 1.55;
    }

    /* Stat Pills inside Banner */
    .neo-banner-pill {
        background: rgba(255, 255, 255, 0.18);
        border: 1px solid rgba(255, 255, 255, 0.45);
        border-radius: 18px;
        padding: 0.85rem 1.5rem;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: inset 2px 2px 5px rgba(255, 255, 255, 0.3),
                    4px 4px 10px rgba(0, 0, 0, 0.15);
        color: #FFFFFF !important;
    }

    .neo-banner-pill-val {
        font-family: 'Outfit', sans-serif;
        font-size: 1.75rem;
        font-weight: 800;
        color: #FFFFFF !important;
    }

    .neo-banner-pill-lbl {
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #DBEAFE !important;
    }

    /* Section Header Block */
    .section-header-box {
        margin-top: 1rem;
        margin-bottom: 1.6rem;
        padding-bottom: 0.9rem;
        border-bottom: 2px solid rgba(203, 213, 225, 0.6);
    }

    .section-kicker {
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #2563EB;
        margin-bottom: 0.25rem;
    }

    .section-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.85rem;
        font-weight: 800;
        color: #1E3A8A;
        margin: 0 0 0.35rem 0;
    }

    .section-meaning-card {
        background: rgba(255, 255, 255, 0.65);
        border-left: 4px solid #2563EB;
        border-radius: 10px;
        padding: 0.75rem 1.1rem;
        margin-top: 0.5rem;
        font-size: 0.88rem;
        color: #334155;
        line-height: 1.5;
        box-shadow: 4px 4px 10px rgba(163, 177, 198, 0.2),
                    -4px -4px 10px rgba(255, 255, 255, 0.7);
    }

    /* Neomorphic Frosted Glass Card */
    .neo-glass-card {
        background: rgba(255, 255, 255, 0.65);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1.5px solid rgba(255, 255, 255, 0.85);
        border-radius: 22px;
        padding: 1.6rem;
        margin-bottom: 1.6rem;
        box-shadow: 10px 10px 24px rgba(163, 177, 198, 0.35),
                    -10px -10px 24px rgba(255, 255, 255, 0.9);
    }

    .neo-card-header {
        background: linear-gradient(135deg, #1E40AF 0%, #2563EB 100%);
        color: #FFFFFF !important;
        padding: 0.8rem 1.2rem;
        border-radius: 14px;
        font-family: 'Outfit', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 4px 4px 12px rgba(37, 99, 235, 0.3);
    }

    .card-meaning-text {
        font-size: 0.84rem;
        color: #475569;
        margin-bottom: 1.3rem;
        padding: 0.5rem 0.7rem;
        background: rgba(241, 245, 249, 0.7);
        border-radius: 8px;
        line-height: 1.45;
        border-left: 3px solid #3B82F6;
    }

    /* Metric Inset Boxes */
    .neo-metric-box {
        background: rgba(248, 250, 252, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 18px;
        padding: 1.3rem;
        text-align: left;
        box-shadow: 8px 8px 18px rgba(163, 177, 198, 0.3),
                    -8px -8px 18px rgba(255, 255, 255, 0.95);
    }

    .neo-metric-val {
        font-family: 'Outfit', sans-serif;
        font-size: 1.95rem;
        font-weight: 800;
        color: #1E3A8A;
    }

    .neo-metric-lbl {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #64748B;
        margin-bottom: 0.2rem;
    }

    .neo-metric-desc {
        font-size: 0.78rem;
        color: #475569;
        margin-top: 0.4rem;
        line-height: 1.35;
    }

    /* Customer Info Identity Badge */
    .customer-id-badge {
        background: rgba(30, 58, 138, 0.08);
        border: 1px solid rgba(37, 99, 235, 0.25);
        border-radius: 14px;
        padding: 0.8rem 1.2rem;
        margin-bottom: 1.2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    /* Status Result Banners */
    .neo-banner-critical {
        background: linear-gradient(135deg, rgba(185, 28, 28, 0.9) 0%, rgba(220, 38, 38, 0.92) 100%);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(254, 202, 202, 0.5);
        border-radius: 20px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.6rem;
        color: #FFFFFF !important;
        box-shadow: 8px 8px 20px rgba(220, 38, 38, 0.28),
                    -6px -6px 16px rgba(255, 255, 255, 0.8);
    }

    .neo-banner-critical * {
        color: #FFFFFF !important;
    }

    .neo-banner-moderate {
        background: linear-gradient(135deg, rgba(180, 83, 9, 0.9) 0%, rgba(245, 158, 11, 0.92) 100%);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(254, 240, 138, 0.5);
        border-radius: 20px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.6rem;
        color: #FFFFFF !important;
        box-shadow: 8px 8px 20px rgba(245, 158, 11, 0.28),
                    -6px -6px 16px rgba(255, 255, 255, 0.8);
    }

    .neo-banner-moderate * {
        color: #FFFFFF !important;
    }

    .neo-banner-low {
        background: linear-gradient(135deg, rgba(4, 120, 87, 0.9) 0%, rgba(16, 185, 129, 0.92) 100%);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(167, 243, 208, 0.5);
        border-radius: 20px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.6rem;
        color: #FFFFFF !important;
        box-shadow: 8px 8px 20px rgba(16, 185, 129, 0.28),
                    -6px -6px 16px rgba(255, 255, 255, 0.8);
    }

    .neo-banner-low * {
        color: #FFFFFF !important;
    }

    /* Neomorphic Inset Well for Action Cards */
    .neo-action-item {
        background: linear-gradient(135deg, #1E40AF 0%, #2563EB 100%);
        border: 1px solid rgba(255, 255, 255, 0.35);
        border-radius: 14px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.85rem;
        color: #FFFFFF !important;
        box-shadow: 5px 5px 14px rgba(37, 99, 235, 0.3),
                    -3px -3px 8px rgba(255, 255, 255, 0.8);
    }

    .neo-action-item * {
        color: #FFFFFF !important;
    }

    /* Sidebar Theme: Frosted Slate Glass */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
        border-right: 2px solid rgba(255, 255, 255, 0.1);
    }

    section[data-testid="stSidebar"] * {
        color: #F8FAFC;
    }

    /* Neomorphic Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 60%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        padding: 0.8rem 1.9rem !important;
        border-radius: 16px !important;
        border: 1.5px solid rgba(255, 255, 255, 0.45) !important;
        box-shadow: 6px 6px 16px rgba(37, 99, 235, 0.4),
                    -4px -4px 12px rgba(255, 255, 255, 0.85) !important;
        transition: all 0.25s ease !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 8px 8px 22px rgba(37, 99, 235, 0.55),
                    -4px -4px 14px rgba(255, 255, 255, 0.95) !important;
    }

    /* Force sidebar button text always white and visible */
    section[data-testid="stSidebar"] .stButton > button {
        color: #FFFFFF !important;
        font-size: 0.88rem !important;
        font-weight: 700 !important;
        padding: 0.55rem 0.9rem !important;
    }

    section[data-testid="stSidebar"] .stButton > button p,
    section[data-testid="stSidebar"] .stButton > button span,
    section[data-testid="stSidebar"] .stButton > button div {
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# CACHED RESOURCE LOADING & PERSISTENT HISTORY FILE
# =========================================================
base_dir = os.path.dirname(__file__)
HISTORY_FILE = os.path.join(base_dir, "prediction_history.csv")

@st.cache_resource
def load_model_assets():
    model_path = os.path.join(base_dir, "churn_model.pkl")
    scaler_path = os.path.join(base_dir, "scaler.pkl")
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error(f"Required model assets not found in {base_dir}")
        st.stop()
    return joblib.load(model_path), joblib.load(scaler_path)

@st.cache_data
def load_telco_records():
    csv_path = os.path.join(base_dir, "WA_Fn-UseC_-Telco-Customer-Churn.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
        return df
    return None

model, scaler = load_model_assets()
telco_df = load_telco_records()
EXPECTED_FEATURES = list(scaler.feature_names_in_)

# Load persistent history if exists
def get_saved_history():
    if os.path.exists(HISTORY_FILE):
        try:
            return pd.read_csv(HISTORY_FILE).to_dict("records")
        except Exception:
            return []
    return []

def save_to_history_file(records):
    try:
        pd.DataFrame(records).to_csv(HISTORY_FILE, index=False)
    except Exception:
        pass

# =========================================================
# SESSION STATE NAVIGATION & FORM VALUES
# =========================================================
PAGES = [
    "📝 Customer Details Input",
    "📊 Prediction & Risk Graphs",
    "📜 Prediction History",
    "📈 Population Analytics",
    "🧠 Model Explainability",
    "📁 Batch CSV Predictor"
]

if "current_page" not in st.session_state:
    st.session_state["current_page"] = PAGES[0]

if "last_prediction" not in st.session_state:
    st.session_state["last_prediction"] = None

if "prediction_history" not in st.session_state:
    st.session_state["prediction_history"] = get_saved_history()

# Default form field values
defaults = {
    "customer_id": "CUST-7842",
    "customer_name": "Sarah Jenkins",
    "gender": "Female",
    "senior": "No",
    "partner": "No",
    "dependents": "No",
    "tenure": 12,
    "phone": "Yes",
    "lines": "No",
    "internet": "Fiber optic",
    "security": "No",
    "backup": "No",
    "device": "No",
    "tech": "No",
    "tv": "Yes",
    "movies": "Yes",
    "contract": "Month-to-month",
    "paperless": "Yes",
    "payment": "Electronic check",
    "monthly": 85.0,
    "total": 1020.0
}

for k, v in defaults.items():
    if f"form_{k}" not in st.session_state:
        st.session_state[f"form_{k}"] = v

def apply_persona(preset_type):
    if preset_type == "🚨 High Churn Risk":
        st.session_state["form_customer_id"] = "CUST-9104"
        st.session_state["form_customer_name"] = "Alex Mercer"
        st.session_state["form_gender"] = "Female"
        st.session_state["form_senior"] = "Yes"
        st.session_state["form_partner"] = "No"
        st.session_state["form_dependents"] = "No"
        st.session_state["form_tenure"] = 2
        st.session_state["form_phone"] = "Yes"
        st.session_state["form_lines"] = "Yes"
        st.session_state["form_internet"] = "Fiber optic"
        st.session_state["form_security"] = "No"
        st.session_state["form_backup"] = "No"
        st.session_state["form_device"] = "No"
        st.session_state["form_tech"] = "No"
        st.session_state["form_tv"] = "Yes"
        st.session_state["form_movies"] = "Yes"
        st.session_state["form_contract"] = "Month-to-month"
        st.session_state["form_paperless"] = "Yes"
        st.session_state["form_payment"] = "Electronic check"
        st.session_state["form_monthly"] = 98.5
        st.session_state["form_total"] = 197.0
    elif preset_type == "🛡️ Loyal VIP Customer":
        st.session_state["form_customer_id"] = "CUST-3210"
        st.session_state["form_customer_name"] = "David Sterling"
        st.session_state["form_gender"] = "Male"
        st.session_state["form_senior"] = "No"
        st.session_state["form_partner"] = "Yes"
        st.session_state["form_dependents"] = "Yes"
        st.session_state["form_tenure"] = 65
        st.session_state["form_phone"] = "Yes"
        st.session_state["form_lines"] = "No"
        st.session_state["form_internet"] = "DSL"
        st.session_state["form_security"] = "Yes"
        st.session_state["form_backup"] = "Yes"
        st.session_state["form_device"] = "Yes"
        st.session_state["form_tech"] = "Yes"
        st.session_state["form_tv"] = "No"
        st.session_state["form_movies"] = "No"
        st.session_state["form_contract"] = "Two year"
        st.session_state["form_paperless"] = "No"
        st.session_state["form_payment"] = "Credit card (automatic)"
        st.session_state["form_monthly"] = 55.0
        st.session_state["form_total"] = 3575.0
    elif preset_type == "⚖️ Moderate Risk":
        st.session_state["form_customer_id"] = "CUST-5521"
        st.session_state["form_customer_name"] = "Emma Watson"
        st.session_state["form_gender"] = "Female"
        st.session_state["form_senior"] = "No"
        st.session_state["form_partner"] = "No"
        st.session_state["form_dependents"] = "No"
        st.session_state["form_tenure"] = 16
        st.session_state["form_phone"] = "Yes"
        st.session_state["form_lines"] = "No"
        st.session_state["form_internet"] = "Fiber optic"
        st.session_state["form_security"] = "No"
        st.session_state["form_backup"] = "Yes"
        st.session_state["form_device"] = "No"
        st.session_state["form_tech"] = "No"
        st.session_state["form_tv"] = "No"
        st.session_state["form_movies"] = "No"
        st.session_state["form_contract"] = "One year"
        st.session_state["form_paperless"] = "Yes"
        st.session_state["form_payment"] = "Bank transfer (automatic)"
        st.session_state["form_monthly"] = 80.0
        st.session_state["form_total"] = 1280.0

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown(
        """
        <div style="padding: 1.2rem 0.5rem; text-align: center; border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="background: linear-gradient(135deg, #1E40AF, #3B82F6); width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.6rem; margin: 0 auto 0.6rem auto; box-shadow: 4px 4px 14px rgba(37, 99, 235, 0.4);">🔮</div>
            <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.35rem; font-weight: 800; color: #FFFFFF; margin: 0;">Customer Churn</h2>
            <div style="font-size: 0.78rem; color: #60A5FA; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; margin-top: 0.15rem;">Prediction Studio</div>
            <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 0.4rem; line-height: 1.3;">
                <em>Used to predict subscriber cancellations before contracts expire.</em>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-size: 0.72rem; font-weight: 800; color: #94A3B8; letter-spacing: 0.1em; text-transform: uppercase;">NAVIGATION MENU</div>', unsafe_allow_html=True)

    cur_idx = PAGES.index(st.session_state["current_page"]) if st.session_state["current_page"] in PAGES else 0
    selected_page = st.radio(
        "Navigation Options:",
        PAGES,
        index=cur_idx,
        key="nav_radio_bar",
        help="Select any section to navigate across the platform."
    )
    # Only trigger navigation when the user manually clicks the radio,
    # not when a programmatic rerun fires (both keys must differ)
    if selected_page != st.session_state["current_page"]:
        st.session_state["current_page"] = selected_page
        st.rerun()

    st.markdown("---")
    st.markdown('<div style="font-size: 0.72rem; font-weight: 800; color: #60A5FA; letter-spacing: 0.1em; text-transform: uppercase;">TEST PERSONAS</div>', unsafe_allow_html=True)
    st.caption("Autofill sample profiles:")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        if st.button("🚨 High Risk", use_container_width=True, help="Autofills a high-risk profile: Month-to-month contract, fiber optic, electronic check, no tech support."):
            apply_persona("🚨 High Churn Risk")
            st.session_state["current_page"] = "📝 Customer Details Input"
            st.session_state["nav_radio_bar"] = "📝 Customer Details Input"
            st.rerun()
    with col_p2:
        if st.button("🛡️ Loyal VIP", use_container_width=True, help="Autofills a loyal profile: 5+ years tenure, two-year contract, auto-pay, bundled security suite."):
            apply_persona("🛡️ Loyal VIP Customer")
            st.session_state["current_page"] = "📝 Customer Details Input"
            st.session_state["nav_radio_bar"] = "📝 Customer Details Input"
            st.rerun()

    if st.button("⚖️ Moderate Risk Profile", use_container_width=True, help="Autofills an intermediate scenario: 1-year contract, fiber optic, partial service bundle."):
        apply_persona("⚖️ Moderate Risk")
        st.session_state["current_page"] = "📝 Customer Details Input"
        st.session_state["nav_radio_bar"] = "📝 Customer Details Input"
        st.rerun()

    st.markdown("---")
    hist_count = len(st.session_state["prediction_history"])
    st.markdown(
        '<div style="font-size: 0.72rem; font-weight: 800; color: #60A5FA; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.4rem;">📜 PREDICTION HISTORY</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div style="background: rgba(30, 58, 138, 0.4); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 14px; padding: 0.9rem; margin-bottom: 0.5rem;">
            <div style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin: 0.2rem 0;">🗂️ {hist_count} Records Logged</div>
            <div style="font-size: 0.75rem; color: #CBD5E1; margin-top: 0.25rem;">Full audit log of all predictions made in this session and past sessions.</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("📜 Open History Log", use_container_width=True, help="Navigate to the full Prediction History tab to review all past churn predictions."):
        st.session_state["current_page"] = "📜 Prediction History"
        st.session_state["nav_radio_bar"] = "📜 Prediction History"
        st.rerun()



# =========================================================
# TOP HERO BANNER (GLASS-NEOMORPHISM + CONTEXTUAL MEANING)
# =========================================================
st.markdown(
    """
    <div class="neo-glass-banner">
        <div>
            <h1 class="banner-title">Customer Churn Prediction</h1>
            <div class="banner-meaning">
                <strong>📖 Meaning & Purpose:</strong> <em>Customer churn</em> represents the rate at which subscribers discontinue or cancel their recurring telecom services. This platform applies machine learning to estimate each customer's departure likelihood, allowing businesses to execute proactive retention offers before cancellation happens.
            </div>
        </div>
        <div style="display: flex; gap: 0.9rem;">
            <div class="neo-banner-pill">
                <div class="neo-banner-pill-val">80.4%</div>
                <div class="neo-banner-pill-lbl">Model Accuracy</div>
            </div>
            <div class="neo-banner-pill">
                <div class="neo-banner-pill-val">7,043</div>
                <div class="neo-banner-pill-lbl">Historical Records</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SECTION 1: CUSTOMER DETAILS INPUT
# =========================================================
if st.session_state["current_page"] == "📝 Customer Details Input":
    st.markdown(
        """
        <div class="section-header-box">
            <div class="section-kicker">STEP 1: CONFIGURATION</div>
            <h2 class="section-title">Enter Customer Account Information</h2>
            <div class="section-meaning-card">
                <strong>📖 Purpose:</strong> This intake form captures the customer's identifier, subscriber name, demographic variables, subscribed services, and contract billing details. Hover over the <strong>? (question mark)</strong> beside any option to inspect why that attribute was selected and how it influences churn risk.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Customer Identity Card
    st.markdown(
        """
        <div class="neo-glass-card" style="margin-bottom: 1.4rem;">
            <div class="neo-card-header">🆔 Customer Identity Details</div>
            <div class="card-meaning-text">
                <strong>Meaning:</strong> Records the unique subscriber identifier and customer name for tracking predictions and logging in the persistent audit history.
            </div>
        """,
        unsafe_allow_html=True
    )
    id_col1, id_col2 = st.columns(2, gap="medium")
    with id_col1:
        st.session_state["form_customer_id"] = st.text_input(
            "Customer Account ID",
            value=st.session_state["form_customer_id"],
            help="Why it was used: Unique account reference code used to track the customer across billing databases and audit histories."
        )
    with id_col2:
        st.session_state["form_customer_name"] = st.text_input(
            "Customer Full Name",
            value=st.session_state["form_customer_name"],
            help="Why it was used: Identifies the primary account holder for personalized outreach and customer success retention campaigns."
        )
    st.markdown("</div>", unsafe_allow_html=True)

    col_c1, col_c2, col_c3 = st.columns(3, gap="medium")

    with col_c1:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">👤 Account & Demographics</div>
                <div class="card-meaning-text">
                    <strong>Meaning:</strong> Demographic variables uncover household size and age groups that correlate with long-term telecom plan stability.
                </div>
            """,
            unsafe_allow_html=True
        )
        g_idx = 0 if st.session_state["form_gender"] == "Female" else 1
        st.session_state["form_gender"] = st.selectbox(
            "Customer Gender",
            ["Female", "Male"],
            index=g_idx,
            help="Why it was used: Captures subscriber gender to evaluate whether demographic segments show differing churn propensities."
        )
        
        s_idx = 0 if st.session_state["form_senior"] == "No" else 1
        st.session_state["form_senior"] = st.selectbox(
            "Senior Citizen Status",
            ["No", "Yes"],
            index=s_idx,
            help="Why it was used: Identifies customers aged 65+. Seniors typically possess fixed incomes and specific service usage patterns affecting contract longevity."
        )
        
        p_idx = 0 if st.session_state["form_partner"] == "No" else 1
        st.session_state["form_partner"] = st.selectbox(
            "Partner / Spouse",
            ["No", "Yes"],
            index=p_idx,
            help="Why it was used: Indicates if the subscriber is partnered. Multi-person households generally exhibit lower churn due to shared utility reliance."
        )
        
        d_idx = 0 if st.session_state["form_dependents"] == "No" else 1
        st.session_state["form_dependents"] = st.selectbox(
            "Dependents",
            ["No", "Yes"],
            index=d_idx,
            help="Why it was used: Tracks if the customer has dependent family members (e.g., children). Subscribers with dependents prioritize uninterrupted home connectivity."
        )
        
        st.session_state["form_tenure"] = st.slider(
            "Account Tenure (Months)",
            min_value=0, max_value=72,
            value=int(st.session_state["form_tenure"]),
            help="Why it was used: Number of consecutive months subscribed. Customers within their first 12 months exhibit the highest cancellation risk."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_c2:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">🌐 Telecom & Internet Services</div>
                <div class="card-meaning-text">
                    <strong>Meaning:</strong> Core and add-on subscriptions. Service depth creates switching costs that prevent customers from migrating to competitors.
                </div>
            """,
            unsafe_allow_html=True
        )
        ph_idx = 0 if st.session_state["form_phone"] == "Yes" else 1
        st.session_state["form_phone"] = st.selectbox(
            "Phone Service",
            ["Yes", "No"],
            index=ph_idx,
            help="Why it was used: Primary voice telephone line subscription. Used to identify landline vs broadband-only households."
        )
        
        l_opts = ["No", "Yes", "No phone service"] if st.session_state["form_phone"] == "Yes" else ["No phone service"]
        l_idx = l_opts.index(st.session_state["form_lines"]) if st.session_state["form_lines"] in l_opts else 0
        st.session_state["form_lines"] = st.selectbox(
            "Multiple Lines",
            l_opts,
            index=l_idx,
            help="Why it was used: Indicates whether multiple extensions or phone lines are connected, reflecting family-plan tier adoption."
        )
        
        net_opts = ["Fiber optic", "DSL", "No"]
        net_idx = net_opts.index(st.session_state["form_internet"]) if st.session_state["form_internet"] in net_opts else 0
        st.session_state["form_internet"] = st.selectbox(
            "Internet Service Type",
            net_opts,
            index=net_idx,
            help="Why it was used: Primary broadband technology. Fiber optic users pay more and exhibit higher churn if technical support is inadequate."
        )
        
        sec_opts = ["No", "Yes", "No internet service"]
        sec_idx = sec_opts.index(st.session_state["form_security"]) if st.session_state["form_security"] in sec_opts else 0
        st.session_state["form_security"] = st.selectbox(
            "Online Security Suite",
            sec_opts,
            index=sec_idx,
            help="Why it was used: Anti-virus and firewall protection. Subscribers with security add-ons churn 50% less due to high perceived protection value."
        )
        
        bak_idx = sec_opts.index(st.session_state["form_backup"]) if st.session_state["form_backup"] in sec_opts else 0
        st.session_state["form_backup"] = st.selectbox(
            "Online Cloud Backup",
            sec_opts,
            index=bak_idx,
            help="Why it was used: Cloud storage for personal files. Storing personal data creates high migration inertia that deters carrier switching."
        )
        
        dev_idx = sec_opts.index(st.session_state["form_device"]) if st.session_state["form_device"] in sec_opts else 0
        st.session_state["form_device"] = st.selectbox(
            "Device Protection",
            sec_opts,
            index=dev_idx,
            help="Why it was used: Equipment and router replacement insurance. Lowers customer friction and dissatisfaction when hardware malfunctions."
        )
        
        tech_idx = sec_opts.index(st.session_state["form_tech"]) if st.session_state["form_tech"] in sec_opts else 0
        st.session_state["form_tech"] = st.selectbox(
            "Tech Support Add-on",
            sec_opts,
            index=tech_idx,
            help="Why it was used: Dedicated technical support tier. Lack of accessible tech support is a top direct cause of service cancellation."
        )
        
        tv_idx = sec_opts.index(st.session_state["form_tv"]) if st.session_state["form_tv"] in sec_opts else 0
        st.session_state["form_tv"] = st.selectbox(
            "Streaming TV",
            sec_opts,
            index=tv_idx,
            help="Why it was used: IPTV streaming television service. Increases overall household engagement and average monthly bill size."
        )
        
        mov_idx = sec_opts.index(st.session_state["form_movies"]) if st.session_state["form_movies"] in sec_opts else 0
        st.session_state["form_movies"] = st.selectbox(
            "Streaming Movies",
            sec_opts,
            index=mov_idx,
            help="Why it was used: Premium on-demand movie entertainment package. Deepens customer integration into the carrier's digital ecosystem."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_c3:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">💳 Contract Terms & Billing</div>
                <div class="card-meaning-text">
                    <strong>Meaning:</strong> Financial commitment terms. Contract duration and payment friction are the two strongest mathematical drivers of churn.
                </div>
            """,
            unsafe_allow_html=True
        )
        ct_opts = ["Month-to-month", "One year", "Two year"]
        ct_idx = ct_opts.index(st.session_state["form_contract"]) if st.session_state["form_contract"] in ct_opts else 0
        st.session_state["form_contract"] = st.selectbox(
            "Contract Duration",
            ct_opts,
            index=ct_idx,
            help="Why it was used: Commitment agreement term. Month-to-month users have no cancellation fees and exhibit over 40% churn compared to <3% on 2-year plans."
        )
        
        pay_opts = ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
        pay_idx = pay_opts.index(st.session_state["form_payment"]) if st.session_state["form_payment"] in pay_opts else 0
        st.session_state["form_payment"] = st.selectbox(
            "Payment Method",
            pay_opts,
            index=pay_idx,
            help="Why it was used: Billing channel. Electronic checks require manual monthly action and lead to higher churn, whereas auto-pay locks in retention."
        )
        
        pap_idx = 0 if st.session_state["form_paperless"] == "Yes" else 1
        st.session_state["form_paperless"] = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"],
            index=pap_idx,
            help="Why it was used: E-billing adoption. Correlates with tech-savvy subscribers who are more active in comparing competitor market pricing."
        )
        
        st.session_state["form_monthly"] = st.number_input(
            "Monthly Charges ($)",
            min_value=15.0, max_value=150.0,
            value=float(st.session_state["form_monthly"]), step=1.0,
            help="Why it was used: Recurring monthly invoice fee. Higher monthly charges increase customer price sensitivity and churn likelihood."
        )
        
        est_tot = max(round(st.session_state["form_tenure"] * st.session_state["form_monthly"], 2), 18.0)
        tot_val = float(st.session_state["form_total"] if st.session_state["form_total"] > 0 else est_tot)
        st.session_state["form_total"] = st.number_input(
            "Total Charges ($)",
            min_value=0.0, max_value=10000.0,
            value=tot_val, step=10.0,
            help="Why it was used: Cumulative lifetime revenue from the customer. Reflects customer relationship depth and historical investment."
        )
        if st.session_state["form_tenure"] > 0:
            st.caption(f"💡 Calculated spend for {st.session_state['form_tenure']} months is approx ${est_tot:,.2f}")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    b_c1, b_c2, b_c3 = st.columns([1, 2, 1])
    with b_c2:
        if st.button("🔮 Calculate Churn Risk & Redirect to Graphs Page ➡️", use_container_width=True, help="Executes the Logistic Regression model, saves to audit history, and immediately redirects to the interactive prediction and risk graphs."):
            cust_dict = {
                "SeniorCitizen": 1 if st.session_state["form_senior"] == "Yes" else 0,
                "tenure": st.session_state["form_tenure"],
                "MonthlyCharges": st.session_state["form_monthly"],
                "TotalCharges": st.session_state["form_total"],
                "gender_Male": 1 if st.session_state["form_gender"] == "Male" else 0,
                "Partner_Yes": 1 if st.session_state["form_partner"] == "Yes" else 0,
                "Dependents_Yes": 1 if st.session_state["form_dependents"] == "Yes" else 0,
                "PhoneService_Yes": 1 if st.session_state["form_phone"] == "Yes" else 0,
                "MultipleLines_No phone service": 1 if st.session_state["form_lines"] == "No phone service" else 0,
                "MultipleLines_Yes": 1 if st.session_state["form_lines"] == "Yes" else 0,
                "InternetService_Fiber optic": 1 if st.session_state["form_internet"] == "Fiber optic" else 0,
                "InternetService_No": 1 if st.session_state["form_internet"] == "No" else 0,
                "OnlineSecurity_No internet service": 1 if st.session_state["form_security"] == "No internet service" else 0,
                "OnlineSecurity_Yes": 1 if st.session_state["form_security"] == "Yes" else 0,
                "OnlineBackup_No internet service": 1 if st.session_state["form_backup"] == "No internet service" else 0,
                "OnlineBackup_Yes": 1 if st.session_state["form_backup"] == "Yes" else 0,
                "DeviceProtection_No internet service": 1 if st.session_state["form_device"] == "No internet service" else 0,
                "DeviceProtection_Yes": 1 if st.session_state["form_device"] == "Yes" else 0,
                "TechSupport_No internet service": 1 if st.session_state["form_tech"] == "No internet service" else 0,
                "TechSupport_Yes": 1 if st.session_state["form_tech"] == "Yes" else 0,
                "StreamingTV_No internet service": 1 if st.session_state["form_tv"] == "No internet service" else 0,
                "StreamingTV_Yes": 1 if st.session_state["form_tv"] == "Yes" else 0,
                "StreamingMovies_No internet service": 1 if st.session_state["form_movies"] == "No internet service" else 0,
                "StreamingMovies_Yes": 1 if st.session_state["form_movies"] == "Yes" else 0,
                "Contract_One year": 1 if st.session_state["form_contract"] == "One year" else 0,
                "Contract_Two year": 1 if st.session_state["form_contract"] == "Two year" else 0,
                "PaperlessBilling_Yes": 1 if st.session_state["form_paperless"] == "Yes" else 0,
                "PaymentMethod_Credit card (automatic)": 1 if st.session_state["form_payment"] == "Credit card (automatic)" else 0,
                "PaymentMethod_Electronic check": 1 if st.session_state["form_payment"] == "Electronic check" else 0,
                "PaymentMethod_Mailed check": 1 if st.session_state["form_payment"] == "Mailed check" else 0
            }
            inp_df = pd.DataFrame([cust_dict])[EXPECTED_FEATURES]
            scaled_v = scaler.transform(inp_df)
            prob = float(model.predict_proba(scaled_v)[0][1] * 100)
            pred = int(model.predict(scaled_v)[0])
            
            risk_tier = "CRITICAL" if prob >= 70 else ("MODERATE" if prob >= 40 else "LOW")
            timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Store current prediction
            st.session_state["last_prediction"] = {
                "customer_id": st.session_state["form_customer_id"],
                "customer_name": st.session_state["form_customer_name"],
                "prob": prob,
                "pred": pred,
                "risk_tier": risk_tier,
                "timestamp": timestamp_str,
                "details": dict(cust_dict)
            }

            # Append to persistent history
            history_entry = {
                "Timestamp": timestamp_str,
                "Customer ID": st.session_state["form_customer_id"],
                "Customer Name": st.session_state["form_customer_name"],
                "Churn Probability (%)": round(prob, 1),
                "Risk Tier": risk_tier,
                "Predicted Outcome": "Churn" if pred == 1 else "Stay (Loyal)",
                "Tenure (Mos)": st.session_state["form_tenure"],
                "Monthly Bill ($)": st.session_state["form_monthly"],
                "Contract": st.session_state["form_contract"],
                "Internet": st.session_state["form_internet"]
            }
            st.session_state["prediction_history"].insert(0, history_entry)
            save_to_history_file(st.session_state["prediction_history"])

            st.session_state["current_page"] = "📊 Prediction & Risk Graphs"
            st.session_state["nav_radio_bar"] = "📊 Prediction & Risk Graphs"
            st.rerun()

# =========================================================
# SECTION 2: PREDICTION & RISK GRAPHS PAGE
# =========================================================
elif st.session_state["current_page"] == "📊 Prediction & Risk Graphs":
    st.markdown(
        """
        <div class="section-header-box">
            <div class="section-kicker">STEP 2: DIAGNOSTICS & VISUALIZATIONS</div>
            <h2 class="section-title">Prediction Results & Risk Assessment Graphs</h2>
            <div class="section-meaning-card">
                <strong>📖 Purpose:</strong> Displays the machine learning probability score, danger tier classification, visual gauge charts, and tailored retention countermeasures generated specifically for this account.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.session_state["last_prediction"] is None:
        cust_dict = {
            "SeniorCitizen": 1 if st.session_state["form_senior"] == "Yes" else 0,
            "tenure": st.session_state["form_tenure"],
            "MonthlyCharges": st.session_state["form_monthly"],
            "TotalCharges": st.session_state["form_total"],
            "gender_Male": 1 if st.session_state["form_gender"] == "Male" else 0,
            "Partner_Yes": 1 if st.session_state["form_partner"] == "Yes" else 0,
            "Dependents_Yes": 1 if st.session_state["form_dependents"] == "Yes" else 0,
            "PhoneService_Yes": 1 if st.session_state["form_phone"] == "Yes" else 0,
            "MultipleLines_No phone service": 1 if st.session_state["form_lines"] == "No phone service" else 0,
            "MultipleLines_Yes": 1 if st.session_state["form_lines"] == "Yes" else 0,
            "InternetService_Fiber optic": 1 if st.session_state["form_internet"] == "Fiber optic" else 0,
            "InternetService_No": 1 if st.session_state["form_internet"] == "No" else 0,
            "OnlineSecurity_No internet service": 1 if st.session_state["form_security"] == "No internet service" else 0,
            "OnlineSecurity_Yes": 1 if st.session_state["form_security"] == "Yes" else 0,
            "OnlineBackup_No internet service": 1 if st.session_state["form_backup"] == "No internet service" else 0,
            "OnlineBackup_Yes": 1 if st.session_state["form_backup"] == "Yes" else 0,
            "DeviceProtection_No internet service": 1 if st.session_state["form_device"] == "No internet service" else 0,
            "DeviceProtection_Yes": 1 if st.session_state["form_device"] == "Yes" else 0,
            "TechSupport_No internet service": 1 if st.session_state["form_tech"] == "No internet service" else 0,
            "TechSupport_Yes": 1 if st.session_state["form_tech"] == "Yes" else 0,
            "StreamingTV_No internet service": 1 if st.session_state["form_tv"] == "No internet service" else 0,
            "StreamingTV_Yes": 1 if st.session_state["form_tv"] == "Yes" else 0,
            "StreamingMovies_No internet service": 1 if st.session_state["form_movies"] == "No internet service" else 0,
            "StreamingMovies_Yes": 1 if st.session_state["form_movies"] == "Yes" else 0,
            "Contract_One year": 1 if st.session_state["form_contract"] == "One year" else 0,
            "Contract_Two year": 1 if st.session_state["form_contract"] == "Two year" else 0,
            "PaperlessBilling_Yes": 1 if st.session_state["form_paperless"] == "Yes" else 0,
            "PaymentMethod_Credit card (automatic)": 1 if st.session_state["form_payment"] == "Credit card (automatic)" else 0,
            "PaymentMethod_Electronic check": 1 if st.session_state["form_payment"] == "Electronic check" else 0,
            "PaymentMethod_Mailed check": 1 if st.session_state["form_payment"] == "Mailed check" else 0
        }
        inp_df = pd.DataFrame([cust_dict])[EXPECTED_FEATURES]
        scaled_v = scaler.transform(inp_df)
        prob = float(model.predict_proba(scaled_v)[0][1] * 100)
        pred = int(model.predict(scaled_v)[0])
        st.session_state["last_prediction"] = {
            "customer_id": st.session_state["form_customer_id"],
            "customer_name": st.session_state["form_customer_name"],
            "prob": prob,
            "pred": pred,
            "risk_tier": "CRITICAL" if prob >= 70 else ("MODERATE" if prob >= 40 else "LOW"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "details": dict(cust_dict)
        }

    c_id = st.session_state["last_prediction"].get("customer_id", "CUST-7842")
    c_name = st.session_state["last_prediction"].get("customer_name", "Sarah Jenkins")
    churn_prob = st.session_state["last_prediction"]["prob"]
    pred = st.session_state["last_prediction"]["pred"]

    # Customer Identity Header Badge
    st.markdown(
        f"""
        <div class="customer-id-badge">
            <div style="display: flex; gap: 1.2rem; align-items: center;">
                <span style="font-weight: 800; color: #1E3A8A; font-size: 1.05rem;">🆔 {c_id}</span>
                <span style="font-size: 1.05rem; font-weight: 700; color: #334155;">👤 {c_name}</span>
            </div>
            <div style="font-size: 0.82rem; color: #64748B;">
                Scored on: <strong>{st.session_state['last_prediction'].get('timestamp', 'Just now')}</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Status Alert Banner
    if churn_prob >= 70:
        b_class = "neo-banner-critical"
        header_title = "🚨 CRITICAL RISK: Customer is Highly Likely to Churn"
        header_msg = f"The model calculates an imminent <strong>{churn_prob:.1f}%</strong> churn probability for <strong>{c_name}</strong>. Immediate proactive retention outreach required."
        tag_color = "#DC2626"
    elif churn_prob >= 40:
        b_class = "neo-banner-moderate"
        header_title = "⚠️ ELEVATED RISK: Customer Exhibits Churn Vulnerability"
        header_msg = f"The model calculates a <strong>{churn_prob:.1f}%</strong> churn probability for <strong>{c_name}</strong>. Proactive plan optimizations recommended."
        tag_color = "#F59E0B"
    else:
        b_class = "neo-banner-low"
        header_title = "✅ LOW RISK: Customer is Likely to Remain Loyal"
        header_msg = f"The model calculates only a <strong>{churn_prob:.1f}%</strong> churn probability for <strong>{c_name}</strong>. Account shows high loyalty indicators."
        tag_color = "#059669"

    st.markdown(
        f"""
        <div class="{b_class}">
            <div style="font-family: 'Outfit', sans-serif; font-size: 1.45rem; font-weight: 800; color: #FFFFFF !important; margin-bottom: 0.35rem;">
                {header_title}
            </div>
            <div style="color: #FFFFFF !important; font-size: 0.95rem;">{header_msg}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Graphs: Speedometer & Probability Comparison
    g_col1, g_col2 = st.columns([1.1, 1], gap="medium")

    with g_col1:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">⚡ Radial Speedometer Churn Gauge</div>
                <div class="card-meaning-text">
                    <strong>Meaning:</strong> Speedometer dial visualizing churn likelihood from 0% (Loyal Safe Zone) to 100% (Imminent Churn Danger Zone).
                </div>
            """,
            unsafe_allow_html=True
        )
        fig_speed = go.Figure(go.Indicator(
            mode="gauge+number",
            value=churn_prob,
            number={'suffix': "%", 'font': {'size': 44, 'family': 'Outfit', 'color': '#1E3A8A'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
                'bar': {'color': tag_color, 'thickness': 0.28},
                'bgcolor': "#E2E8F0",
                'borderwidth': 1,
                'bordercolor': "#CBD5E1",
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(5, 150, 105, 0.25)'},
                    {'range': [40, 70], 'color': 'rgba(245, 158, 11, 0.25)'},
                    {'range': [70, 100], 'color': 'rgba(220, 38, 38, 0.25)'}
                ],
                'threshold': {'line': {'color': "#DC2626", 'width': 3}, 'thickness': 0.8, 'value': 50}
            }
        ))
        fig_speed.update_layout(
            height=270,
            margin=dict(l=20, r=20, t=20, b=10),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_speed, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with g_col2:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">📊 Retention vs Departure Comparison</div>
                <div class="card-meaning-text">
                    <strong>Meaning:</strong> Direct balance between the customer's likelihood of renewing vs cancelling within the active billing cycle.
                </div>
            """,
            unsafe_allow_html=True
        )
        prob_chart_df = pd.DataFrame({
            "Outcome": ["Stay (Loyal)", "Churn Risk"],
            "Probability": [100 - churn_prob, churn_prob]
        })
        fig_b = px.bar(
            prob_chart_df,
            x="Probability",
            y="Outcome",
            orientation='h',
            text=[f"{100-churn_prob:.1f}%", f"{churn_prob:.1f}%"],
            color="Outcome",
            color_discrete_map={"Stay (Loyal)": "#2563EB", "Churn Risk": "#DC2626"}
        )
        fig_b.update_layout(
            height=210,
            showlegend=False,
            margin=dict(l=0, r=10, t=10, b=10),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, range=[0, 100], title="Probability (%)", color="#64748B"),
            yaxis=dict(title="", color="#0F172A")
        )
        fig_b.update_traces(textposition='inside', textfont=dict(color='white', size=13, family='Outfit'))
        st.plotly_chart(fig_b, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Diagnostic Triggers & Strategic Action Plan
    st.markdown("<br>", unsafe_allow_html=True)
    d_c1, d_c2 = st.columns(2, gap="medium")

    with d_c1:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">🔍 Identified Critical Risk Drivers</div>
                <div class="card-meaning-text">
                    <strong>Meaning:</strong> Pinpoints the exact features in this customer's account driving up their statistical risk of departure.
                </div>
            """,
            unsafe_allow_html=True
        )
        triggers = []
        if st.session_state["form_contract"] == "Month-to-month":
            triggers.append(("Month-to-Month Contract", "No contract lock-in; month-to-month subscribers represent 42% historical churn."))
        if st.session_state["form_internet"] == "Fiber optic":
            triggers.append(("Fiber Optic Line", "High price sensitivity and aggressive competitor promotions lead to service defection."))
        if st.session_state["form_payment"] == "Electronic check":
            triggers.append(("Electronic Check Billing", "Unautomated payment methods require active monthly effort and correlate with churn spikes."))
        if st.session_state["form_tenure"] <= 12:
            triggers.append((f"Early Customer Window ({st.session_state['form_tenure']} mos)", "Customer is within the high-risk first-year onboarding cycle."))
        if st.session_state["form_tech"] != "Yes" and st.session_state["form_internet"] != "No":
            triggers.append(("No Tech Support", "Subscribers without dedicated tech support churn twice as often during outages."))
        if st.session_state["form_monthly"] >= 75:
            triggers.append((f"High Monthly Charges (${st.session_state['form_monthly']:.2f})", "Premium billing creates heightened cancellation sensitivity."))

        if not triggers:
            st.success(f"✨ Zero critical vulnerability drivers identified for {c_name}. Profile exhibits high customer retention stability.")
        else:
            for t_title, t_desc in triggers:
                st.markdown(
                    f"""
                    <div style="background: #FEF2F2; border-left: 4px solid #DC2626; border-radius: 10px; padding: 0.85rem 1.1rem; margin-bottom: 0.75rem;">
                        <div style="font-weight: 700; color: #991B1B; font-size: 0.92rem;">⚠️ {t_title}</div>
                        <div style="font-size: 0.84rem; color: #475569; margin-top: 0.2rem;">{t_desc}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        st.markdown("</div>", unsafe_allow_html=True)

    with d_c2:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">💡 Actionable Retention Strategies</div>
                <div class="card-meaning-text">
                    <strong>Meaning:</strong> Prescribed retention campaigns engineered specifically to intercept and resolve this customer's risk factors.
                </div>
            """,
            unsafe_allow_html=True
        )
        if churn_prob >= 70:
            st.markdown(
                f"""
                <div class="neo-action-item">
                    <div style="font-weight: 800; font-size: 0.95rem;">1. Immediate Retention Outreach to {c_name}</div>
                    <div style="font-size: 0.84rem; opacity: 0.95; margin-top: 0.25rem;">Initiate priority phone call from senior loyalty specialist within 24 hours.</div>
                </div>
                <div class="neo-action-item">
                    <div style="font-weight: 800; font-size: 0.95rem;">2. Annual Commitment Discount</div>
                    <div style="font-size: 0.84rem; opacity: 0.95; margin-top: 0.25rem;">Offer 20% discount on 1-year or 2-year contract lock-in with rate guarantee.</div>
                </div>
                <div class="neo-action-item">
                    <div style="font-weight: 800; font-size: 0.95rem;">3. Free Premium Suite</div>
                    <div style="font-size: 0.84rem; opacity: 0.95; margin-top: 0.25rem;">Bundle complimentary Tech Support & Cloud Backup for 6 billing cycles.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        elif churn_prob >= 40:
            st.markdown(
                f"""
                <div class="neo-action-item">
                    <div style="font-weight: 800; font-size: 0.95rem;">1. Auto-Pay Transition Bonus for {c_name}</div>
                    <div style="font-size: 0.84rem; opacity: 0.95; margin-top: 0.25rem;">Provide $15 bill credit upon enrolling in automatic credit card or ACH payment.</div>
                </div>
                <div class="neo-action-item">
                    <div style="font-weight: 800; font-size: 0.95rem;">2. Proactive Satisfaction Survey</div>
                    <div style="font-size: 0.84rem; opacity: 0.95; margin-top: 0.25rem;">Send concierge email checking internet stability with one-click resolution link.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="neo-action-item">
                    <div style="font-weight: 800; font-size: 0.95rem;">1. Anniversary Loyalty Rewards for {c_name}</div>
                    <div style="font-size: 0.84rem; opacity: 0.95; margin-top: 0.25rem;">Acknowledge continuous subscription with speed boost or movie streaming tokens.</div>
                </div>
                <div class="neo-action-item">
                    <div style="font-weight: 800; font-size: 0.95rem;">2. Expansion Opportunity</div>
                    <div style="font-size: 0.84rem; opacity: 0.95; margin-top: 0.25rem;">Candidate is primed for smart device add-ons or additional connected family lines.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown("</div>", unsafe_allow_html=True)

    # Navigation buttons
    st.markdown("<br>", unsafe_allow_html=True)
    nav_btn_c1, nav_btn_c2 = st.columns(2, gap="medium")
    with nav_btn_c1:
        if st.button("⬅️ Edit Customer Details & Re-Calculate", use_container_width=True, help="Returns to Step 1 to modify customer attributes and calculate new predictions."):
            st.session_state["current_page"] = "📝 Customer Details Input"
            st.session_state["nav_radio_bar"] = "📝 Customer Details Input"
            st.rerun()
    with nav_btn_c2:
        if st.button("📜 View Audit Log in Prediction History ➡️", use_container_width=True, help="Navigates to the historical predictions tab to review past scores."):
            st.session_state["current_page"] = "📜 Prediction History"
            st.session_state["nav_radio_bar"] = "📜 Prediction History"
            st.rerun()

# =========================================================
# SECTION 3: PREDICTION HISTORY (NEW DEDICATED TAB)
# =========================================================
elif st.session_state["current_page"] == "📜 Prediction History":
    st.markdown(
        """
        <div class="section-header-box">
            <div class="section-kicker">AUDIT TRAIL & LOGS</div>
            <h2 class="section-title">Customer Churn Prediction History</h2>
            <div class="section-meaning-card">
                <strong>📖 Purpose:</strong> Dedicated historical ledger recording all individual customer predictions evaluated by this system. Enables customer success teams to audit past risk classifications, track subscriber scores over time, and export records for CRM integration.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    history_records = st.session_state["prediction_history"]

    if not history_records:
        st.info("ℹ️ No predictions have been recorded yet. Navigate to **📝 Customer Details Input** and generate a prediction to populate your history log.")
    else:
        hist_df = pd.DataFrame(history_records)

        # Summary KPIs
        tot_logged = len(hist_df)
        crit_logged = (hist_df["Risk Tier"] == "CRITICAL").sum()
        mod_logged = (hist_df["Risk Tier"] == "MODERATE").sum()
        low_logged = (hist_df["Risk Tier"] == "LOW").sum()
        avg_prob = hist_df["Churn Probability (%)"].mean()

        h_kpi1, h_kpi2, h_kpi3, h_kpi4 = st.columns(4, gap="medium")
        with h_kpi1:
            st.markdown(
                f"""
                <div class="neo-metric-box">
                    <div class="neo-metric-lbl">Total Scored</div>
                    <div class="neo-metric-val">{tot_logged}</div>
                    <div class="neo-metric-desc">Total customer audits logged in history.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with h_kpi2:
            st.markdown(
                f"""
                <div class="neo-metric-box">
                    <div class="neo-metric-lbl">Critical Risk (>= 70%)</div>
                    <div class="neo-metric-val" style="color: #DC2626;">{crit_logged}</div>
                    <div class="neo-metric-desc">Customers flagged for immediate intervention.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with h_kpi3:
            st.markdown(
                f"""
                <div class="neo-metric-box">
                    <div class="neo-metric-lbl">Moderate Risk (40-69%)</div>
                    <div class="neo-metric-val" style="color: #F59E0B;">{mod_logged}</div>
                    <div class="neo-metric-desc">Subscribers requiring proactive plan check-ins.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with h_kpi4:
            st.markdown(
                f"""
                <div class="neo-metric-box">
                    <div class="neo-metric-lbl">Mean Churn Probability</div>
                    <div class="neo-metric-val">{avg_prob:.1f}%</div>
                    <div class="neo-metric-desc">Average churn likelihood across evaluated accounts.</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Search / Filter Bar
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">🔍 Filter & Search Prediction Logs</div>
                <div class="card-meaning-text">
                    <strong>Meaning:</strong> Query historical predictions by Customer Name, Customer Account ID, or Risk Tier.
                </div>
            """,
            unsafe_allow_html=True
        )
        f_col1, f_col2 = st.columns([2, 1])
        with f_col1:
            search_query = st.text_input("Search by Customer Name or ID:", "", help="Filter records matching subscriber name or ID.")
        with f_col2:
            tier_filter = st.selectbox("Filter by Risk Tier:", ["All", "CRITICAL", "MODERATE", "LOW"], help="Filter by risk classification level.")

        filtered_df = hist_df.copy()
        if search_query:
            filtered_df = filtered_df[
                filtered_df["Customer Name"].str.contains(search_query, case=False, na=False) |
                filtered_df["Customer ID"].str.contains(search_query, case=False, na=False)
            ]
        if tier_filter != "All":
            filtered_df = filtered_df[filtered_df["Risk Tier"] == tier_filter]

        st.dataframe(filtered_df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Download & Clear Buttons
        h_btn1, h_btn2 = st.columns([1, 1], gap="medium")
        with h_btn1:
            csv_bytes = hist_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Export Full Audit History (CSV)",
                data=csv_bytes,
                file_name="customer_churn_prediction_history.csv",
                mime="text/csv",
                use_container_width=True,
                help="Exports the entire audit trail of customer predictions as a CSV spreadsheet."
            )
        with h_btn2:
            if st.button("🗑️ Clear Audit History", use_container_width=True, help="Wipes all historical customer predictions from the current session and file."):
                st.session_state["prediction_history"] = []
                if os.path.exists(HISTORY_FILE):
                    os.remove(HISTORY_FILE)
                st.success("Audit history has been cleared.")
                st.rerun()

# =========================================================
# SECTION 4: POPULATION ANALYTICS
# =========================================================
elif st.session_state["current_page"] == "📈 Population Analytics":
    st.markdown(
        """
        <div class="section-header-box">
            <div class="section-kicker">DATASET INTELLIGENCE</div>
            <h2 class="section-title">Telco Customer Cohort Trends</h2>
            <div class="section-meaning-card">
                <strong>📖 Purpose:</strong> Macro-level exploratory data analysis illustrating historical subscriber distributions, churn frequency across contract terms, and customer tenure patterns across 7,043 accounts.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if telco_df is not None:
        tot_records = len(telco_df)
        churn_cnt = (telco_df['Churn'] == 'Yes').sum()
        churn_pct = (churn_cnt / tot_records) * 100
        avg_mo = telco_df['MonthlyCharges'].mean()
        avg_ten = telco_df['tenure'].mean()

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(
                f"""
                <div class="neo-metric-box">
                    <div class="neo-metric-lbl">Total Records</div>
                    <div class="neo-metric-val">{tot_records:,}</div>
                    <div class="neo-metric-desc">Total customer portfolio size analyzed.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with m2:
            st.markdown(
                f"""
                <div class="neo-metric-box">
                    <div class="neo-metric-lbl">Baseline Churn</div>
                    <div class="neo-metric-val" style="color: #DC2626;">{churn_pct:.1f}%</div>
                    <div class="neo-metric-desc">Historical portfolio percentage that canceled service.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with m3:
            st.markdown(
                f"""
                <div class="neo-metric-box">
                    <div class="neo-metric-lbl">Avg Monthly Bill</div>
                    <div class="neo-metric-val">${avg_mo:.2f}</div>
                    <div class="neo-metric-desc">Mean invoice charge per subscriber per month.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with m4:
            st.markdown(
                f"""
                <div class="neo-metric-box">
                    <div class="neo-metric-lbl">Average Tenure</div>
                    <div class="neo-metric-val">{avg_ten:.1f} <span style="font-size: 1rem; color: #64748B;">mos</span></div>
                    <div class="neo-metric-desc">Mean customer lifetime longevity before departure.</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        ch_c1, ch_c2 = st.columns(2, gap="medium")

        with ch_c1:
            st.markdown(
                """
                <div class="neo-glass-card">
                    <div class="neo-card-header">📄 Contract Type vs Churn Count</div>
                    <div class="card-meaning-text">
                        <strong>Meaning:</strong> Demonstrates that month-to-month contracts experience vastly higher cancellations than multi-year agreements.
                    </div>
                """,
                unsafe_allow_html=True
            )
            c_data = telco_df.groupby(['Contract', 'Churn']).size().reset_index(name='Count')
            fig_c = px.bar(
                c_data,
                x='Contract',
                y='Count',
                color='Churn',
                barmode='group',
                color_discrete_map={'No': '#2563EB', 'Yes': '#DC2626'}
            )
            fig_c.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_c, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with ch_c2:
            st.markdown(
                """
                <div class="neo-glass-card">
                    <div class="neo-card-header">⏳ Customer Tenure Curve</div>
                    <div class="card-meaning-text">
                        <strong>Meaning:</strong> Highlights churn clustering in the earliest months of customer tenure, proving onboarding retention importance.
                    </div>
                """,
                unsafe_allow_html=True
            )
            fig_t = px.histogram(
                telco_df,
                x="tenure",
                color="Churn",
                marginal="box",
                nbins=30,
                color_discrete_map={'No': '#2563EB', 'Yes': '#DC2626'}
            )
            fig_t.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_t, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        ch_c3, ch_c4 = st.columns(2, gap="medium")
        with ch_c3:
            st.markdown(
                """
                <div class="neo-glass-card">
                    <div class="neo-card-header">🌐 Internet Service Churn Volume</div>
                    <div class="card-meaning-text">
                        <strong>Meaning:</strong> Shows churn frequency across broadband technologies, showing higher fiber defection due to pricing.
                    </div>
                """,
                unsafe_allow_html=True
            )
            net_d = telco_df.groupby(['InternetService', 'Churn']).size().reset_index(name='Count')
            fig_n = px.bar(
                net_d,
                x='InternetService',
                y='Count',
                color='Churn',
                color_discrete_map={'No': '#2563EB', 'Yes': '#DC2626'}
            )
            fig_n.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_n, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with ch_c4:
            st.markdown(
                """
                <div class="neo-glass-card">
                    <div class="neo-card-header">💳 Churn Share by Payment Method</div>
                    <div class="card-meaning-text">
                        <strong>Meaning:</strong> Demonstrates that automated payments (credit card/ACH) protect retention versus manual electronic checks.
                    </div>
                """,
                unsafe_allow_html=True
            )
            p_d = telco_df[telco_df['Churn'] == 'Yes']['PaymentMethod'].value_counts().reset_index()
            p_d.columns = ['PaymentMethod', 'ChurnCount']
            fig_p = px.pie(
                p_d,
                names='PaymentMethod',
                values='ChurnCount',
                hole=0.45,
                color_discrete_sequence=['#DC2626', '#F59E0B', '#2563EB', '#1E40AF']
            )
            fig_p.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_p, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# SECTION 5: MODEL EXPLAINABILITY
# =========================================================
elif st.session_state["current_page"] == "🧠 Model Explainability":
    st.markdown(
        """
        <div class="section-header-box">
            <div class="section-kicker">ALGORITHMIC TRANSPARENCY</div>
            <h2 class="section-title">Logistic Regression Decision Weights</h2>
            <div class="section-meaning-card">
                <strong>📖 Purpose:</strong> Deconstructs the mathematical coefficients assigned to each feature. Positive weights increase churn risk, while negative weights protect retention.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    coef_df = pd.DataFrame({
        "Feature": EXPECTED_FEATURES,
        "Coefficient": model.coef_[0]
    }).sort_values("Coefficient", ascending=True)

    coef_df["CleanFeature"] = coef_df["Feature"].str.replace("_", " ").str.replace("Yes", "").str.strip()
    coef_df["Impact"] = np.where(coef_df["Coefficient"] > 0, "Increases Churn Risk", "Protects Retention")

    st.markdown(
        """
        <div class="neo-glass-card">
            <div class="neo-card-header">📊 Feature Importance Waterfall</div>
            <div class="card-meaning-text">
                <strong>Meaning:</strong> Visualizes the relative strength of each variable on the final churn classification log-odds.
            </div>
        """,
        unsafe_allow_html=True
    )
    fig_w = px.bar(
        coef_df,
        x="Coefficient",
        y="CleanFeature",
        color="Impact",
        orientation="h",
        color_discrete_map={"Increases Churn Risk": "#DC2626", "Protects Retention": "#2563EB"},
        height=720
    )
    fig_w.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(title="", tickfont=dict(size=11, color="#0F172A")),
        xaxis=dict(title="Model Coefficient (Log-Odds Impact)", gridcolor="#E2E8F0"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_w, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    sp_c1, sp_c2, sp_c3 = st.columns(3, gap="medium")
    with sp_c1:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">⚙️ Architecture Specs</div>
                <div style="font-size: 0.9rem; color: #334155; line-height: 1.8;">
                    <strong>Classifier:</strong> Logistic Regression<br>
                    <strong>Scaler:</strong> StandardScaler<br>
                    <strong>Features:</strong> 30 one-hot encodings<br>
                    <strong>Target:</strong> Churn (0: Stay, 1: Churn)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with sp_c2:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">🎯 Model Benchmarks</div>
                <div style="font-size: 0.9rem; color: #334155; line-height: 1.8;">
                    <strong>Accuracy:</strong> 80.38%<br>
                    <strong>Churn Recall:</strong> 57.0%<br>
                    <strong>F1-Score:</strong> 61.0%<br>
                    <strong>ROC-AUC:</strong> 0.84
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with sp_c3:
        st.markdown(
            """
            <div class="neo-glass-card">
                <div class="neo-card-header">📌 Key Takeaways</div>
                <div style="font-size: 0.9rem; color: #334155; line-height: 1.8;">
                    <strong>Highest Risk:</strong> Fiber optic, electronic check.<br>
                    <strong>Strongest Loyalty:</strong> Two-year contract, high tenure.<br>
                    <strong>Threshold:</strong> 50% probability classification.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# SECTION 6: BATCH CSV PREDICTOR
# =========================================================
elif st.session_state["current_page"] == "📁 Batch CSV Predictor":
    st.markdown(
        """
        <div class="section-header-box">
            <div class="section-kicker">BULK INFERENCE</div>
            <h2 class="section-title">Batch Customer CSV Predictor</h2>
            <div class="section-meaning-card">
                <strong>📖 Purpose:</strong> Batch scoring engine enabling telecom analysts to upload spreadsheets with hundreds of subscriber records, calculate probabilities simultaneously, and export prioritized intervention files.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    b_mode = st.radio(
        "Select Data Source:",
        ["Test Batch (50 Telco Customers)", "Upload Custom CSV"],
        horizontal=True,
        help="Why it was used: Choose whether to run inference on sample historical records or upload a live telecom spreadsheet."
    )
    batch_df = None

    if b_mode == "Test Batch (50 Telco Customers)":
        if telco_df is not None:
            batch_df = telco_df.sample(min(50, len(telco_df)), random_state=42).copy()
        else:
            st.warning("Telco CSV dataset missing.")
    else:
        uploaded_f = st.file_uploader(
            "Upload CSV formatted with Telco columns",
            type=["csv"],
            help="Why it was used: File uploader expecting standard Telco fields to execute bulk predictions."
        )
        if uploaded_f is not None:
            batch_df = pd.read_csv(uploaded_f)

    if batch_df is not None:
        st.caption(f"Loaded {len(batch_df)} customer rows.")
        if st.button("⚡ Score Batch Records", use_container_width=True, help="Executes inference for all loaded customer records."):
            with st.spinner("Scoring customer batch..."):
                rows = []
                for _, row in batch_df.iterrows():
                    rec = {
                        "SeniorCitizen": 1 if row.get("SeniorCitizen") in [1, "1", "Yes"] else 0,
                        "tenure": float(row.get("tenure", 12)),
                        "MonthlyCharges": float(row.get("MonthlyCharges", 70.0)),
                        "TotalCharges": float(row.get("TotalCharges", 800.0)),
                        "gender_Male": 1 if row.get("gender") == "Male" else 0,
                        "Partner_Yes": 1 if row.get("Partner") == "Yes" else 0,
                        "Dependents_Yes": 1 if row.get("Dependents") == "Yes" else 0,
                        "PhoneService_Yes": 1 if row.get("PhoneService") == "Yes" else 0,
                        "MultipleLines_No phone service": 1 if row.get("MultipleLines") == "No phone service" else 0,
                        "MultipleLines_Yes": 1 if row.get("MultipleLines") == "Yes" else 0,
                        "InternetService_Fiber optic": 1 if row.get("InternetService") == "Fiber optic" else 0,
                        "InternetService_No": 1 if row.get("InternetService") == "No" else 0,
                        "OnlineSecurity_No internet service": 1 if row.get("OnlineSecurity") == "No internet service" else 0,
                        "OnlineSecurity_Yes": 1 if row.get("OnlineSecurity") == "Yes" else 0,
                        "OnlineBackup_No internet service": 1 if row.get("OnlineBackup") == "No internet service" else 0,
                        "OnlineBackup_Yes": 1 if row.get("OnlineBackup") == "Yes" else 0,
                        "DeviceProtection_No internet service": 1 if row.get("DeviceProtection") == "No internet service" else 0,
                        "DeviceProtection_Yes": 1 if row.get("DeviceProtection") == "Yes" else 0,
                        "TechSupport_No internet service": 1 if row.get("TechSupport") == "No internet service" else 0,
                        "TechSupport_Yes": 1 if row.get("TechSupport") == "Yes" else 0,
                        "StreamingTV_No internet service": 1 if row.get("StreamingTV") == "No internet service" else 0,
                        "StreamingTV_Yes": 1 if row.get("StreamingTV") == "Yes" else 0,
                        "StreamingMovies_No internet service": 1 if row.get("StreamingMovies") == "No internet service" else 0,
                        "StreamingMovies_Yes": 1 if row.get("StreamingMovies") == "Yes" else 0,
                        "Contract_One year": 1 if row.get("Contract") == "One year" else 0,
                        "Contract_Two year": 1 if row.get("Contract") == "Two year" else 0,
                        "PaperlessBilling_Yes": 1 if row.get("PaperlessBilling") == "Yes" else 0,
                        "PaymentMethod_Credit card (automatic)": 1 if row.get("PaymentMethod") == "Credit card (automatic)" else 0,
                        "PaymentMethod_Electronic check": 1 if row.get("PaymentMethod") == "Electronic check" else 0,
                        "PaymentMethod_Mailed check": 1 if row.get("PaymentMethod") == "Mailed check" else 0
                    }
                    rows.append(rec)

                feats_df = pd.DataFrame(rows)[EXPECTED_FEATURES]
                scaled_b = scaler.transform(feats_df)
                preds = model.predict(scaled_b)
                probs = model.predict_proba(scaled_b)[:, 1] * 100

                scored_df = batch_df.copy()
                scored_df["Predicted_Churn"] = ["Yes" if p == 1 else "No" for p in preds]
                scored_df["Churn_Risk_Prob_%"] = np.round(probs, 1)
                scored_df["Risk_Category"] = [
                    "CRITICAL" if p >= 70 else ("MODERATE" if p >= 40 else "LOW")
                    for p in probs
                ]

                st.markdown("<br>", unsafe_allow_html=True)
                bc1, bc2, bc3 = st.columns(3)
                bc1.metric("Scored Accounts", len(scored_df))
                bc2.metric("Flagged Churners", (scored_df['Predicted_Churn'] == 'Yes').sum())
                bc3.metric("Critical Risk", (scored_df['Risk_Category'] == 'CRITICAL').sum())

                cols_display = [c for c in ["customerID", "Predicted_Churn", "Churn_Risk_Prob_%", "Risk_Category", "tenure", "MonthlyCharges", "Contract"] if c in scored_df.columns]
                st.dataframe(scored_df[cols_display], use_container_width=True)

                csv_b = scored_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "📥 Export Scored CSV Report",
                    data=csv_b,
                    file_name="customer_churn_scored_report.csv",
                    mime="text/csv",
                    use_container_width=True,
                    help="Downloads the scored dataset with predicted churn outcomes and probability scores."
                )

# =========================================================
# FOOTER
# =========================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="border-top: 2px solid rgba(203, 213, 225, 0.6); padding: 1.8rem 0; text-align: center; color: #64748B; font-size: 0.88rem;">
        <div style="font-weight: 700; color: #1E40AF; margin-bottom: 0.25rem;">
            Customer Churn Prediction &bull; Enterprise Machine Learning Analytics
        </div>
        <div>
            Engineered with Scikit-Learn, Streamlit & Plotly &bull; Glassmorphic & Neomorphic Design System
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
