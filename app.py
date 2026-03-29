import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- LEAD RESEARCHER INFO ---
st.sidebar.markdown(f"""
### 🔬 Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*AI-Driven ESCA+ Ethics Model*
""")

# --- AI ENGINE: PREDICTIVE ANALYTICS ---
# Ini adalah simulasi model Machine Learning yang telah dilatih (Trained Model)
def predict_loyalty(clinical, spiritual, ethical, integrity, agency):
    # Weights (Pemberat) berdasarkan kajian literature ESCA+
    # Ethical Justice (0.3) & Clinical (0.25) mempunyai impak tertinggi pada Loyalty
    prediction = (clinical * 0.25) + (spiritual * 0.15) + (ethical * 0.30) + (integrity * 0.10) + (agency * 0.20)
    return round(prediction, 2)

# --- APP NAVIGATION ---
menu = st.sidebar.radio("Navigation", ["Hospital Dashboard", "AI Patient Loyalty Predictor"])

# ---------------------------------------------------------
# MODUL BARU: AI PATIENT LOYALTY PREDICTOR
# ---------------------------------------------------------
if menu == "AI Patient Loyalty Predictor":
    st.title("🤖 ESCA+ AI Predictive Engine")
    st.write("Predicting the probability of Patient Loyalty and Advocacy based on real-time ESCA+ scores.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Input Live ESCA+ Scores")
        # Slider untuk simulasi data input dari hospital
        sc_clin = st.slider("Clinical Competence Score", 0, 100, 93)
        sc_spir = st.slider("Spiritual Sensitivity Score", 0, 100, 83)
        sc_ethi = st.slider("Ethical Justice Score", 0, 100, 99)
        sc_inte = st.slider("Institutional Integrity Score", 0, 100, 90)
        sc_agen = st.slider("Patient Agency Score", 0, 100, 87)
        
        predicted_score = predict_loyalty(sc_clin, sc_spir, sc_ethi, sc_inte, sc_agen)

    with col2:
        st.subheader("Predicted Patient Loyalty Probability")
        
        # Gauge Chart untuk visualisasi AI
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = predicted_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Loyalty Intention (%)", 'font': {'size': 24}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': 'red'},
                    {'range': [50, 80], 'color': 'yellow'},
                    {'range': [80, 100], 'color': 'green'}],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        
        st.plotly_chart(fig)

    st.divider()
    
    # AI Actionable Insights
    st.subheader("💡 AI Recommendations for Management")
    if predicted_score > 90:
        st.success("✅ **High Advocacy Risk:** This patient is highly likely to recommend Malaysia's Islamic Medical Tourism. Strategy: Invite for a testimonial or loyalty program.")
    elif predicted_score > 70:
        st.warning("⚠️ **Moderate Loyalty:** Potential for return is good, but focus on 'Spiritual Sensitivity' to close the gap.")
    else:
        st.error("🚨 **Churn Risk:** High probability of patient dissatisfaction. Immediate ethical intervention required in 'Ethical Justice' domain.")

    st.info(f"Analysis performed by ESCA+ AI Engine. Lead Researcher: Mohd Khairul Ridhuan (2025).")

# ---------------------------------------------------------
# RETAIN ORIGINAL DASHBOARD CODE BELOW...
# ---------------------------------------------------------
else:
    st.title("🏥 ESCA+ Real-Time Hospital Monitor")
    st.write("Please select 'AI Predictor' from the sidebar for advanced analytics.")
