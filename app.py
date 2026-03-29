import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURATION & RESEARCHER INFO ---
st.set_page_config(page_title="ESCA+ Platinum AI Dashboard", layout="wide", page_icon="🌙")

st.sidebar.markdown(f"""
### 🔬 Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*Reframing Islamic Medical Tourism*

**System Status:** 🟢 Live
**Server Time:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
""")

lang = st.sidebar.selectbox("🌐 Select Language", ["English", "Bahasa Melayu", "العربية"])
st.sidebar.divider()

# --- 2. SESSION STATE (Database Initialization) ---
if 'patient_status' not in st.session_state:
    st.session_state.patient_status = "Unidentified"
if 'surgery_step' not in st.session_state:
    st.session_state.surgery_step = 2 
if 'agency_decisions' not in st.session_state:
    st.session_state.agency_decisions = []
if 'esca_scores' not in st.session_state:
    st.session_state.esca_scores = {"Clinical": 93, "Spiritual": 83, "Ethical": 99, "Integrity": 90, "Agency": 87}

# --- 3. MAIN NAVIGATION ---
menu = st.sidebar.radio("Main Menu", [
    "1. Good Samaritan & Intake", 
    "2. Medical Team & Live OT Simulation", 
    "3. Clinical Command Center", 
    "4. Spiritual & Ritual Support",
    "5. AI Patient Loyalty Predictor", 
    "6. Financial & Audit Reports"
])

# --- 4. LOGIC PAGES ---

# PAGE 1: GOOD SAMARITAN & INTAKE
if menu == "1. Good Samaritan & Intake":
    st.title("🚑 Accident Intake & Good Samaritan Protocol")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Witness/Samaritan Registration")
        st.text_input("Witness Name", placeholder="Enter name of person who brought patient")
        st.text_input("Witness Contact", placeholder="Phone number")
        st.success("Legal Notice: Under Ethical Justice, witnesses are protected from victim liabilities.")
    with col2:
        st.subheader("Patient Identification")
        st.text_input("Full Name (If known)", value="Sarah J. Abdullah")
        st.selectbox("Citizenship", ["Malaysian", "International (Tourist)"], index=1)
        st.text_input("Passport / IC Number", value="UK-8822990")
    
    st.divider()
    st.subheader("🛡️ ESCA+ Value Passport Setup")
    c1, c2, c3 = st.columns(3)
    c1.radio("Gender Preference", ["Same Gender", "No Preference", "Flexible (Darurah)"])
    c2.multiselect("Dietary Needs", ["Halal-Certified", "Vegan", "Vegetarian"])
    c3.toggle("High Modesty Protocol (Extra Draping)")
    if st.button("Finalize Intake & Sync with HIS"):
        st.success("Intake Process Complete. Patient AX-2024 is now active.")

# PAGE 2: MEDICAL TEAM & LIVE OT SIMULATION (UPDATED WITH VIDEO & TEAM)
elif menu == "2. Medical Team & Live OT Simulation":
    st.title("🔴 Operation Theater (OT) Live Digital Link")
    st.info("💡 Education Purpose: Real-time simulation of cardiothoracic procedure for patient Sarah J. Abdullah.")
    
    # --- Live Video & Status Section ---
    col_vid, col_stat = st.columns([2, 1])
    
    with col_vid:
       # Gantikan dengan link baru di bawah (Animasi Bypass Jantung 3D - Embed Friendly)
    st.video("https://www.youtube.com/watch?v=5UeS7M2i0Q8") 
    st.info("🔒 Secure Link: This feed is encrypted and restricted to authorized guardians only.")

    with col_stat:
        st.subheader("📊 Real-Time Status")
        st.metric("Surgical Phase", "Internal Repair", "70% Complete")
        st.write("**Current Action:** Suturing of the left ventricular wall.")
        st.write("**Safety Status:** 🟢 All systems nominal.")
        st.divider()
        st.metric("Heart Rate", "88 BPM", "Stable")
        st.metric("Oxygen (SpO2)", "98%", "Normal")
        st.metric("Aurat Protection", "Active", "100% Covered")

    st.divider()

    # --- Medical Team Board ---
    st.subheader("👥 The Surgical Team (On-Duty)")
    col_team1, col_team2 = st.columns(2)
    with col_team1:
        st.markdown("""
        **Medical Specialists:**
        *   👨‍⚕️ **Lead Surgeon:** Dr. Adam Syarif (MBBS, FRCS London)
        *   👨‍⚕️ **Assisting Surgeon:** Dr. Johan Ariff (MD, MSurg)
        *   👩‍⚕️ **Anesthesiologist:** Dr. Siti Hajar (Critical Care Specialist)
        """)
    with col_team2:
        st.markdown("""
        **Nursing & Support Team:**
        *   👩‍⚕️ **Scrub Nurse:** Nurse Aishah (OT Specialist)
        *   👩‍⚕️ **Circulating Nurse:** Nurse Farida (Patient Care)
        *   👨‍⚕️ **Perfusionist:** Mr. Zaid (Heart-Lung Machine)
        *   🌙 **Shariah Officer:** Ustaz Hamdan (On-Call Consultant)
        """)

    st.divider()

    # --- Surgery Simulation Steps ---
    st.subheader("⏱️ Live Procedure Tracking & ESCA+ Compliance")
    surgery_steps = [
        {"step": "Patient Positioning & Aurat Draping", "status": "Completed ✅", "esca": "Spiritual Sensitivity"},
        {"step": "Anesthesia Induction (Halal-Pharma)", "status": "Completed ✅", "esca": "Institutional Integrity"},
        {"step": "Surgical Incision", "status": "In Progress 🔵", "esca": "Clinical Competence"},
        {"step": "Internal Tissue Repair", "status": "Pending ⏳", "esca": "Clinical Competence"},
        {"step": "Closure & Cleaning", "status": "Pending ⏳", "esca": "Dignity Preservation"}
    ]

    for i, s in enumerate(surgery_steps):
        with st.expander(f"Phase {i+1}: {s['step']}", expanded=(i == 2)):
            col_s1, col_s2 = st.columns(2)
            col_s1.write(f"**Status:** {s['status']}")
            col_s2.write(f"**ESCA+ Domain:** {s['esca']}")

# PAGE 3: CLINICAL COMMAND CENTER
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

# PAGE 4: SPIRITUAL & RITUAL SUPPORT
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

# PAGE 5: AI PATIENT LOYALTY PREDICTOR
elif menu == "5. AI Patient Loyalty Predictor":
    st.title("🤖 ESCA+ AI Predictive Engine")
    st.write("Predicting **Patient Loyalty** based on ESCA+ domain performance.")
    col1, col2 = st.columns([1, 2])
    with col1:
        s_clin = st.slider("Clinical Competence", 0, 100, st.session_state.esca_scores["Clinical"])
        s_spir = st.slider("Spiritual Sensitivity", 0, 100, st.session_state.esca_scores["Spiritual"])
        s_ethi = st.slider("Ethical Justice", 0, 100, st.session_state.esca_scores["Ethical"])
        loyalty_score = (s_clin * 0.25) + (s_spir * 0.15) + (s_ethi * 0.30) + (100 * 0.30) 
    with col2:
        fig_g = go.Figure(go.Indicator(mode = "gauge+number", value = loyalty_score, title = {'text': "Loyalty Probability (%)"},
                     gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "darkblue"},
                     'steps': [{'range': [0, 50], 'color': "red"}, {'range': [85, 100], 'color': "green"}]}))
        st.plotly_chart(fig_g)

# PAGE 6: FINANCIAL & AUDIT REPORTS
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
    st.write(f"© 2025 Mohd Khairul Ridhuan Bin Mohd Fadzil")
