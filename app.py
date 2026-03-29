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

# Support for Multi-language as per Medical Tourism Needs
lang = st.sidebar.selectbox("🌐 UI Language", ["English", "Bahasa Melayu", "العربية"])
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
    "2. OT Live Digital Simulation", # Updated
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
    with c1:
        st.radio("Gender Preference", ["Same Gender", "No Preference", "Flexible (Darurah)"])
    with c2:
        st.multiselect("Dietary Needs", ["Halal-Certified", "Vegan", "Vegetarian"])
    with c3:
        st.toggle("High Modesty Protocol (Extra Draping)")
    
    if st.button("Finalize Intake & Sync with HIS"):
        st.success("Intake Process Complete. Patient AX-2024 is now active.")

# PAGE 2: OT LIVE DIGITAL SIMULATION (No more unstable YouTube)
elif menu == "2. OT Live Digital Simulation":
    st.title("🔴 Operation Theater (OT) Live Status Link")
    st.info("💡 Note: For privacy & security, raw video feed is replaced by Digital Twin Tracking.")
    
    col_vis, col_stat = st.columns([2, 1])
    
    with col_vis:
        st.subheader("🖥️ Digital Twin Procedure Monitor")
        # Bina visualisasi grafik sebagai ganti video
        fig_sim = go.Figure()
        fig_sim.add_trace(go.Indicator(
            mode = "gauge+number",
            value = 75,
            title = {'text': "Procedure Progress (%)"},
            gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "darkred"}}
        ))
        fig_sim.update_layout(height=350)
        st.plotly_chart(fig_sim, use_container_width=True)
        st.write("**Visual Simulation Overlay:**")
        st.image("https://img.freepik.com/free-vector/medical-infographic-concept_23-2148403310.jpg?t=st=1720000000&exp=1720003600&hmac=3d7f", caption="Simulated Surgical Anatomy View")

    with col_stat:
        st.subheader("📊 Real-Time Vitals")
        st.metric("Heart Rate", "88 BPM", "Stable")
        st.metric("Oxygen (SpO2)", "98%", "Normal")
        st.metric("Aurat Status", "100% Covered", "Protected")
        st.divider()
        st.write("**Team in OT:**")
        st.caption("Surgeon: Dr. Adam Syarif")
        st.caption("Shariah Lead: Ustaz Hamdan")

    st.divider()
    st.subheader("⏱️ Live Step Tracking")
    surgery_steps = ["Pre-op Setup ✅", "Halal Anesthesia ✅", "Main Procedure 🔵", "Internal Closure ⏳"]
    st.write(" | ".join(surgery_steps))

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
        st.subheader("Conflict Resolver")
        st.error("Conflict: Male Surgeon vs Female Preference")
        if st.button("TRIGGER DARURAH OVERRIDE"):
            ts = datetime.now().strftime('%H:%M:%S')
            st.session_state.agency_decisions.append({"time": ts, "event": "Darurah Consent", "details": "Authorized Male Dr"})
            st.warning(f"Authorized at {ts}")
        st.table(pd.DataFrame(st.session_state.agency_decisions))

# PAGE 4: SPIRITUAL & RITUAL SUPPORT
elif menu == "4. Spiritual & Ritual Support":
    st.title("🌙 Spiritual Support")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Prayer Times (Ampang)")
        st.table(pd.DataFrame({"Prayer": ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"], "Time": ["05:58", "13:22", "16:35", "19:25", "20:34"]}))
    with c2: # Fixed NameError from previous version
        st.subheader("Shariah-Clinical Search")
        query = st.text_input("Search Fatwa (e.g., Insulin)")
        if query: st.info(f"Result: Permissible (Harus) in emergency.")

# PAGE 5: AI PATIENT LOYALTY PREDICTOR
elif menu == "5. AI Patient Loyalty Predictor":
    st.title("🤖 ESCA+ AI Predictor")
    s_clin = st.slider("Clinical Competence", 0, 100, 93)
    s_ethi = st.slider("Ethical Justice", 0, 100, 99)
    loyalty = (s_clin * 0.4) + (s_ethi * 0.6) # Formula prediction
    st.metric("Predicted Loyalty Probability", f"{loyalty}%")
    st.progress(loyalty/100)

# PAGE 6: FINANCIAL & AUDIT REPORTS
else:
    st.title("💰 Financial & Audit Reports")
    c1, c2 = st.columns(2) # Define c1, c2
    with c1:
        st.subheader("Ethical Billing")
        bill = pd.DataFrame({"Item": ["Surgery", "ICU", "Spiritual Care"], "Cost (RM)": [15000, 2500, 0]})
        st.table(bill)
    with c2: # Fixed col2 to c2
        st.subheader("Integrity Index")
        fig_p = px.pie(values=[95, 5], names=['Compliant', 'Non-Compliant'])
        st.plotly_chart(fig_p)

st.sidebar.write(f"© 2025 Mohd Khairul Ridhuan Bin Mohd Fadzil")
