import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import random

# --- 1. CONFIGURATION & RESEARCHER INFO ---
st.set_page_config(page_title="ESCA+ Platinum AI Dashboard", layout="wide", page_icon="🌙")

st.sidebar.markdown(f"""
### 🔬 Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*AI-Driven Ethics Stress Simulation*

**System Status:** 🟢 Active
**Server Time:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
""")

lang = st.sidebar.selectbox("🌐 UI Language", ["English", "Bahasa Melayu", "العربية"])
st.sidebar.divider()

# --- 2. SESSION STATE (Database Initialization) ---
if 'sim_running' not in st.session_state:
    st.session_state.sim_running = False
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'esca_scores' not in st.session_state:
    st.session_state.esca_scores = {"Clinical": 93, "Spiritual": 83, "Ethical": 99, "Integrity": 90, "Agency": 87}

# --- 3. MAIN NAVIGATION ---
menu = st.sidebar.radio("Main Menu", [
    "1. Good Samaritan & Intake", 
    "2. LIVE DYNAMIC OT SIMULATOR", # Advanced Dynamic AI
    "3. Medical Team Profiles", 
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
        st.text_input("Witness Name", placeholder="Who brought the patient?")
        st.success("Legal Notice: Good Samaritans are protected from victim liabilities.")
    with col2:
        st.subheader("Patient Identification")
        st.text_input("Full Name", value="Sarah J. Abdullah")
        st.selectbox("Citizenship", ["Malaysian", "International (Tourist)"], index=1)
    st.divider()
    st.subheader("🛡️ ESCA+ Value Passport Setup")
    c1, c2 = st.columns(2)
    c1.radio("Gender Preference", ["Same Gender", "No Preference", "Flexible (Darurah)"])
    c2.toggle("High Modesty Protocol (Extra Draping)")
    if st.button("Finalize Intake"): st.success("Intake Process Complete.")

# PAGE 2: LIVE DYNAMIC OT SIMULATOR (FIXED DUPLICATE ID ERROR)
elif menu == "2. LIVE DYNAMIC OT SIMULATOR":
    st.title("🔴 Live Surgical Stress Simulator (Real-Time)")
    st.info("💡 Watch the ESCA+ Model react to Oxygen Drops and Severe Bleeding.")

    if not st.session_state.sim_running:
        if st.button("🚀 START LIVE SURGERY SIMULATION"):
            st.session_state.sim_running = True
            st.session_state.logs = [] # Clear old logs
            st.rerun()
    else:
        if st.button("⏹️ STOP SIMULATION"):
            st.session_state.sim_running = False
            st.rerun()

        # Layout placeholders to prevent ID duplication
        col_v, col_chart = st.columns([2, 2])
        v_metric = col_v.empty()
        v_log = st.empty()
        v_chart = col_chart.empty()

        # Simulation Loop
        vitals = {"HR": 85, "O2": 98, "BloodLoss": 0, "Ethics": 95}
        
        for i in range(1, 11):
            time.sleep(1.5)
            msg = "Procedure proceeding normally..."
            
            # Crisis Logic
            if i == 4:
                vitals["O2"] = 82
                vitals["HR"] = 112
                msg = "⚠️ OXYGEN DROP! Anesthesiologist adjusting vent..."
            elif i == 7:
                vitals["BloodLoss"] = 500
                vitals["HR"] = 140
                vitals["O2"] = 75
                msg = "🚨 ARTERIAL BLEEDING! Robotic Hemostasis Active."
                vitals["Ethics"] = 70 # Stress on Spiritual Sensitivity
            elif i > 7:
                vitals["O2"] += 5
                vitals["HR"] -= 10
                msg = "✅ Crisis Managed. Vital signs stabilizing."

            # Update Vitals (Gauges)
            with v_metric.container():
                st.subheader(f"Phase {i}: Clinical Status")
                m1, m2, m3 = st.columns(3)
                m1.metric("SpO2", f"{vitals['O2']}%", "-3%" if vitals['O2'] < 90 else "Stable")
                m2.metric("Heart Rate", f"{vitals['HR']} BPM", "+25" if vitals['HR'] > 110 else "Normal")
                m3.metric("Ethics Integrity", f"{vitals['Ethics']}%")
                st.warning(f"**Current Action:** {msg}")

            # Update Chart (Fixed Duplicate ID by using unique key or placeholder)
            with v_chart.container():
                st.subheader("ESCA+ Ethics Balance")
                categories = ['Clinical', 'Spiritual', 'Ethical', 'Integrity', 'Agency']
                # Dynamic Radar values
                radar_vals = [98 if i > 6 else 90, vitals['Ethics'], 100, 95, 90]
                fig = go.Figure(go.Scatterpolar(r=radar_vals, theta=categories, fill='toself'))
                fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
                st.plotly_chart(fig, use_container_width=True, key=f"sim_chart_{i}")

            # Update Log
            st.session_state.logs.insert(0, f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
            v_log.write(st.session_state.logs[:5])

        st.success("🏁 Surgery Complete. Patient moved to Recovery.")
        st.session_state.sim_running = False

# PAGE 3: MEDICAL TEAM PROFILES (Biodata Re-added)
elif menu == "3. Medical Team Profiles":
    st.title("👨‍⚕️ Assigned Medical Team")
    st.write("Clinical Competence & Expertise Profiles")
    c1, c2 = st.columns(2)
    with c1:
        st.info("👨‍⚕️ **Primary Surgeon:** Dr. Adam Syarif\n\n**Education:** MBBS (Malaya), FRCS (London)\n\n**Specialty:** Cardiothoracic Surgery")
    with c2:
        st.info("👩‍⚕️ **Anesthesiologist:** Dr. Siti Hajar\n\n**Education:** MD (USM), MMed (Anaesth)\n\n**Expertise:** Critical Care Ethics")
    st.divider()
    st.subheader("Support Team")
    st.caption("Nurse Aishah (Scrub), Mr. Zaid (Perfusionist), Ustaz Hamdan (Shariah Lead)")

# PAGE 4: SPIRITUAL & RITUAL SUPPORT
elif menu == "4. Spiritual & Ritual Support":
    st.title("🌙 Spiritual & Ritual Assistance")
    t1, t2 = st.columns(2)
    t1.subheader("Prayer Times (Ampang)")
    t1.table(pd.DataFrame({"Prayer": ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"], "Time": ["05:58", "13:22", "16:35", "19:25", "20:34"]}))
    t2.subheader("Fatwa Reference")
    q = t2.text_input("Ask about medical ethics (e.g. insulin)")
    if q: t2.info("Search result: Permissible (Harus) in emergency situations.")

# PAGE 5: AI PATIENT LOYALTY PREDICTOR
elif menu == "5. AI Patient Loyalty Predictor":
    st.title("🤖 AI Loyalty Prediction Engine")
    score = st.slider("Current ESCA Score (%)", 0, 100, 88)
    loyalty = (score * 0.95) # Simple AI Model
    st.metric("Predicted Loyalty Probability", f"{round(loyalty, 2)}%")
    st.progress(loyalty/100)
    if loyalty > 85: st.success("Recommendation: High Potential Advocate.")

# PAGE 6: FINANCIAL & AUDIT REPORTS
else:
    st.title("💰 Financial Transparency & Ethical Audit")
    c1, c2 = st.columns(2)
    c1.subheader("Transparent Billing")
    c1.table(pd.DataFrame({"Item": ["Surgery", "ICU", "Spiritual Care"], "Cost (RM)": [15000, 2500, 0]}))
    c2.subheader("Integrity Audit")
    fig_pie = px.pie(values=[95, 5], names=['Compliant', 'Non-Compliant'], title="Integrity Index")
    c2.plotly_chart(fig_pie)
    st.button("📄 Generate Compliance Certificate")

st.sidebar.divider()
st.sidebar.write(f"© 2025 Mohd Khairul Ridhuan Bin Mohd Fadzil")
