import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time
import random

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Dynamic AI Dashboard", layout="wide", page_icon="🌙")

# --- LEAD RESEARCHER INFO ---
st.sidebar.markdown(f"""
### 🔬 Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*Dynamic Ethics Stress Testing*

**System Status:** 🟢 Active
""")

menu = st.sidebar.radio("Main Menu", [
    "1. Registration & Intake", 
    "2. LIVE DYNAMIC OT SIMULATION", # Modul Utama yang dikemaskini
    "3. AI Loyalty Predictor", 
    "4. Financial & Audit Reports"
])

# --- 2. SESSION STATE ---
if 'sim_running' not in st.session_state:
    st.session_state.sim_running = False
if 'logs' not in st.session_state:
    st.session_state.logs = []

# ---------------------------------------------------------
# PAGE 1: INTAKE (RETAINED)
# ---------------------------------------------------------
if menu == "1. Registration & Intake":
    st.title("🚑 Accident Intake: Sarah J. Abdullah")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Identification")
        st.text_input("Name", "Sarah J. Abdullah")
        st.text_input("Passport", "UK-8822990")
    with col2:
        st.subheader("Value Passport")
        st.radio("Modesty Requirement", ["High (Strict)", "Moderate", "Life-First"])
    st.button("Register & Sync")

# ---------------------------------------------------------
# PAGE 2: LIVE DYNAMIC OT SIMULATION (THE CORE DYNAMIC MODULE)
# ---------------------------------------------------------
elif menu == "2. LIVE DYNAMIC OT SIMULATION":
    st.title("🔴 Live Surgical Stress Simulator (Real-Time)")
    st.info("💡 Monitor how the ESCA+ Model reacts to sudden clinical crises (Oxygen Drop/Bleeding).")

    # Layout Dashboard
    col_vitals, col_visual = st.columns([2, 2])
    col_log, col_ethics = st.columns([2, 1])

    # Placeholders untuk update data tanpa refresh page
    placeholder_vitals = col_vitals.empty()
    placeholder_visual = col_visual.empty()
    placeholder_log = col_log.empty()
    placeholder_ethics = col_ethics.empty()

    if not st.session_state.sim_running:
        if st.button("🚀 START LIVE SURGERY SIMULATION"):
            st.session_state.sim_running = True
            st.rerun()
    else:
        if st.button("⏹️ STOP SIMULATION"):
            st.session_state.sim_running = False
            st.rerun()

        # --- SIMULATION LOOP ---
        vitals = {"HR": 85, "O2": 98, "BloodLoss": 0, "Aurat": 100}
        
        for i in range(1, 11): # Simulasi 10 fasa dinamik
            time.sleep(2) # Setiap 2 saat keadaan berubah
            
            # Logic Perubahan Keadaan (Dinamik)
            event_msg = "Procedure proceeding normally..."
            status_color = "green"
            
            if i == 4:
                vitals["O2"] = 82 # Oxygen Drop!
                vitals["HR"] = 110
                event_msg = "⚠️ ALERT: Oxygen levels dropping! Anesthesiologist intervention required."
                status_color = "orange"
            elif i == 7:
                vitals["BloodLoss"] = 500 # Bleeding!
                vitals["HR"] = 135
                vitals["O2"] = 75
                event_msg = "🚨 CRISIS: Severe arterial bleeding detected! Robotic Precision Mode Active."
                status_color = "red"
            elif i > 7:
                vitals["HR"] -= 5 # Recovery
                vitals["O2"] += 5
                event_msg = "✅ Crisis Controlled. Hemostasis achieved."
                status_color = "green"

            # 1. Update Vitals Display (Gauges)
            with placeholder_vitals:
                st.subheader(f"Step {i}: Clinical Status")
                c1, c2 = st.columns(2)
                c1.metric("Oxygen (SpO2)", f"{vitals['O2']}%", "-3%" if vitals['O2'] < 90 else "Stable")
                c2.metric("Heart Rate", f"{vitals['HR']} BPM", "+20" if vitals['HR'] > 100 else "Normal")
                st.write(f"**Event:** {event_msg}")

            # 2. Update Visual (Radar/Ethics Balance)
            with placeholder_visual:
                st.subheader("ESCA+ Ethics Balance")
                # Jika bleeding, Clinical Competence naik, tapi Spiritual Sensitivity mungkin tercabar
                fig = go.Figure(go.Scatterpolar(
                    r=[95, 80 if vitals['O2'] > 85 else 60, 100, 90, 85],
                    theta=['Clinical', 'Spiritual', 'Ethical', 'Integrity', 'Agency'],
                    fill='toself'
                ))
                fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

            # 3. Update Ethics Monitor
            with placeholder_ethics:
                st.subheader("Modesty Watch")
                st.metric("Aurat Protection", f"{vitals['Aurat']}%", "Secured")
                if vitals['O2'] < 85:
                    st.warning("Ethics Note: Minimal exposure maintained during O2 crisis.")

            # 4. Update Logs
            ts = datetime.now().strftime('%H:%M:%S')
            st.session_state.logs.insert(0, f"[{ts}] {event_msg}")
            with placeholder_log:
                st.subheader("Real-Time Surgical Log")
                st.write(st.session_state.logs[:5])

        st.success("🏁 Simulation Finished. Patient is stable and moved to ICU.")
        st.session_state.sim_running = False

# ---------------------------------------------------------
# PAGE 3: AI LOYALTY (RETAINED)
# ---------------------------------------------------------
elif menu == "3. AI Loyalty Predictor":
    st.title("🤖 AI Loyalty Prediction")
    score = st.slider("Average ESCA Score", 0, 100, 85)
    st.metric("Loyalty Probability", f"{score}%")
    st.progress(score/100)

# ---------------------------------------------------------
# PAGE 4: FINANCIAL (RETAINED)
# ---------------------------------------------------------
else:
    st.title("💰 Ethical Billing")
    st.table(pd.DataFrame({"Item": ["Surgery", "ICU", "Ethics Audit"], "Cost (RM)": [15000, 2500, 0]}))

st.sidebar.write(f"© 2025 Mohd Khairul Ridhuan Bin Mohd Fadzil")
