import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Platinum AI Dashboard", layout="wide", page_icon="🌙")

# --- LEAD RESEARCHER & SYSTEM INFO ---
st.sidebar.markdown(f"""
### 🔬 Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*Reframing Islamic Medical Tourism*

**Institution:** Ampang Specialist Center
**System Status:** 🟢 Live
**Server Time:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
""")

lang = st.sidebar.selectbox("🌐 Select Language", ["English", "Bahasa Melayu", "العربية"])
st.sidebar.divider()

# --- APP NAVIGATION ---
menu = st.sidebar.radio("Main Menu", [
    "1. Good Samaritan & Intake", 
    "2. Medical Team & Live Surgery", 
    "3. Clinical Command Center", 
    "4. Spiritual & Ritual Support",
    "5. AI Patient Loyalty Predictor", # Modul AI Baru
    "6. Financial & Audit Reports"
])

# --- SESSION STATE (Database Sim) ---
if 'patient_status' not in st.session_state:
    st.session_state.patient_status = "Unidentified"
if 'surgery_step' not in st.session_state:
    st.session_state.surgery_step = 0
if 'agency_decisions' not in st.session_state:
    st.session_state.agency_decisions = []
if 'esca_scores' not in st.session_state:
    st.session_state.esca_scores = {"Clinical": 93, "Spiritual": 83, "Ethical": 99, "Integrity": 90, "Agency": 87}

# ---------------------------------------------------------
# PAGE 1: GOOD SAMARITAN & INTAKE
# ---------------------------------------------------------
if menu == "1. Good Samaritan & Intake":
    st.title("🚑 Accident Intake & Good Samaritan Protocol")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Witness/Samaritan Registration")
        st.text_input("Witness Name")
        st.text_input("Witness Contact")
        st.success("Legal Notice: Under Ethical Justice, witnesses are protected from victim liabilities.")
    with col2:
        st.subheader("Patient Identification")
        st.text_input("Full Name (If known)", value="Sarah J. Abdullah")
        st.selectbox("Citizenship", ["Malaysian", "International (Tourist)"], index=1)
        st.text_input("Passport / IC Number", value="UK-8822990")
    
    st.divider()
    st.subheader("🛡️ ESCA+ Value Passport (Initial Setup)")
    c1, c2, c3 = st.columns(3)
    c1.radio("Gender Preference", ["Same Gender", "No Preference", "Flexible (Darurah)"])
    c2.multiselect("Dietary Needs", ["Halal-Certified", "Vegan", "Vegetarian"])
    c3.toggle("High Modesty Protocol (Extra Draping)")
    st.button("Finalize Intake")

# ---------------------------------------------------------
# PAGE 2: MEDICAL TEAM & LIVE SURGERY
# ---------------------------------------------------------
elif menu == "2. Medical Team & Live Surgery":
    st.title("👨‍⚕️ Medical Team & Live Procedure Monitor")
    
    t1, t2 = st.columns(2)
    with t1:
        st.subheader("Medical Specialists")
        st.info("**Primary Surgeon:** Dr. Adam Syarif (MBBS Malaya, FRCS London)")
        st.info("**Anesthesiologist:** Dr. Siti Hajar (MD USM, MMed Anaesth)")
    
    with t2:
        st.subheader("Live Surgery Progress (OT-04)")
        steps = ["Pre-op", "Incision", "Main Procedure", "Closure", "Recovery"]
        st.session_state.surgery_step = st.slider("Current Stage", 0, 4, st.session_state.surgery_step)
        st.progress((st.session_state.surgery_step + 1) / 5)
        st.write(f"**Status:** {steps[st.session_state.surgery_step]}")
        st.checkbox("Aurat Modesty Draping Applied", value=True)
        st.checkbox("Halal Pharma Supplies Used", value=True)

# ---------------------------------------------------------
# PAGE 3: CLINICAL COMMAND CENTER
# ---------------------------------------------------------
elif menu == "3. Clinical Command Center":
    st.title("⚖️ ESCA+ Alignment & Darurah Protocol")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Domain Balance (Radar Analysis)")
        categories = list(st.session_state.esca_scores.keys())
        values = list(st.session_state.esca_scores.values())
        fig = go.Figure(go.Scatterpolar(r=values, theta=categories, fill='toself'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
        st.plotly_chart(fig)
        
    with col2:
        st.subheader("Clinical Conflict Resolver")
        st.error("Conflict: Male Surgeon vs Female Preference (Emergency)")
        if st.button("TRIGGER DARURAH OVERRIDE"):
            ts = datetime.now().strftime('%H:%M:%S')
            st.session_state.agency_decisions.append({"time": ts, "event": "Darurah Consent", "details": "Authorized Dr. Adam (Male)"})
            st.warning(f"Authorized at {ts}")
        
        st.subheader("Audit Trail")
        st.table(pd.DataFrame(st.session_state.agency_decisions))

# ---------------------------------------------------------
# PAGE 4: SPIRITUAL & RITUAL SUPPORT
# ---------------------------------------------------------
elif menu == "4. Spiritual & Ritual Support":
    st.title("🌙 Spiritual & Clinical-Shariah Reference")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Prayer Times (Ampang)")
        st.table(pd.DataFrame({"Prayer": ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"], "Time": ["05:58", "13:22", "16:35", "19:25", "20:34"]}))
    with c2:
        st.subheader("Shariah-Clinical Search")
        query = st.text_input("Search Fatwa (e.g., Insulin, Anesthesia)")
        if query: st.info(f"Result for '{query}': Permissible (Harus) in emergency situations (Maqasid Al-Shariah).")

# ---------------------------------------------------------
# PAGE 5: AI PATIENT LOYALTY PREDICTOR (MODUL BARU)
# ---------------------------------------------------------
elif menu == "5. AI Patient Loyalty Predictor":
    st.title("🤖 ESCA+ AI Predictive Engine")
    st.write("Predicting **Patient Loyalty & Advocacy** based on ESCA+ domain performance.")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Adjust Current Scores")
        # Mengambil data dari session state untuk simulasi AI
        s_clin = st.slider("Clinical Competence", 0, 100, st.session_state.esca_scores["Clinical"])
        s_spir = st.slider("Spiritual Sensitivity", 0, 100, st.session_state.esca_scores["Spiritual"])
        s_ethi = st.slider("Ethical Justice", 0, 100, st.session_state.esca_scores["Ethical"])
        s_inte = st.slider("Institutional Integrity", 0, 100, st.session_state.esca_scores["Integrity"])
        s_agen = st.slider("Patient Agency", 0, 100, st.session_state.esca_scores["Agency"])
        
        # Weighted AI Inference (Based on Research Diagram 2)
        loyalty_score = (s_clin * 0.25) + (s_spir * 0.15) + (s_ethi * 0.30) + (s_inte * 0.10) + (s_agen * 0.20)

    with col2:
        st.subheader("Loyalty Propensity Gauge")
        fig_g = go.Figure(go.Indicator(
            mode = "gauge+number", value = loyalty_score,
            title = {'text': "Loyalty Probability (%)"},
            gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "darkblue"},
                     'steps': [{'range': [0, 50], 'color': "red"}, {'range': [50, 85], 'color': "yellow"}, {'range': [85, 100], 'color': "green"}]}))
        st.plotly_chart(fig_g)
        
        st.subheader("AI Recommendations")
        if loyalty_score > 85: st.success("✅ **High Loyalty Predicted:** Patient will advocate for your hospital. Recommendation: Enroll in Ambassador Program.")
        elif loyalty_score > 60: st.warning("⚠️ **Moderate Loyalty:** Focus on improving 'Spiritual Sensitivity' to increase retention.")
        else: st.error("🚨 **Churn Risk:** High risk of negative word-of-mouth. Immediate ethical follow-up needed.")

# ---------------------------------------------------------
# PAGE 6: FINANCIAL & AUDIT REPORTS
# ---------------------------------------------------------
else:
    st.title("💰 Financial Transparency & Audit Reports")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Ethical Billing (Transparent)")
        bill = pd.DataFrame({"Item": ["Surgery", "ICU", "Good Samaritan Case Fee", "Spiritual Care"], "Cost (RM)": [15000, 2500, 0, 0]})
        st.table(bill)
    with c2:
        st.subheader("Audit Integrity Score")
        fig_p = px.pie(values=[95, 5], names=['Compliant', 'Non-Compliant'], title="Institutional Integrity Index")
        st.plotly_chart(fig_p)
    
    st.button("📄 Generate ESCA+ Compliance Certificate")
    st.write(f"© 2025 Mohd Khairul Ridhuan Bin Mohd Fadzil | ESCA+ Research Translation")
