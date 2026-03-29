import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Hospital Alpha | ESCA+ Platinum Dashboard", layout="wide", page_icon="🏥")

# --- 2. SESSION STATE ---
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 1452
if 'scan_complete' not in st.session_state:
    st.session_state.scan_complete = False
if 'simulation_time_index' not in st.session_state:
    st.session_state.simulation_time_index = 0

# --- 3. SIDEBAR: LEAD RESEARCHER PROFILE ---
st.sidebar.header("Lead Researcher")
st.sidebar.subheader("MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL")
with st.sidebar.expander("🎓 Expertise Profile"):
    st.write("""
    - **Business Management & Islamic Studies**
    - **Corporate Sustainability**
    - **AI & Machine Learning (Self-Taught)**
    - **Human-Computer Interaction (HCI)**
    """)
st.sidebar.divider()
st.sidebar.write(f"📈 **Project Visitors:** `{st.session_state.visitor_count + 1}`")
st.sidebar.write(f"📅 **Date:** {datetime.now().strftime('%d %B %Y')}")
st.sidebar.write(f"⏰ **Real-time:** {datetime.now().strftime('%H:%M:%S')}")
st.sidebar.divider()

menu = st.sidebar.radio("Navigation Menu", [
    "Dashboard Overview",
    "1. Accident Triage & Intake", 
    "2. Advanced OT: 6-Hour Live Simulation", # Redesigned
    "3. Surgical Team Transparency", 
    "4. AI Loyalty Prediction", 
    "5. Financial & Ethical Audit"
])

# --- 4. GLOBAL HEADER & DISCLAIMER ---
st.markdown("<h1 style='text-align: center; color: #004d99;'>HOSPITAL ALPHA</h1>", unsafe_allow_html=True)
st.warning("⚠️ **DISCLAIMER:** For **EDUCATION PURPOSE ONLY**. All clinical simulations are research-based prototypes by Mohd Khairul Ridhuan.")

# --- 5. SIMULATION DATA GENERATOR (6 Hours, 10-min intervals = 36 steps) ---
def generate_surgery_log():
    start_time = datetime.strptime("09:00", "%H:%M")
    logs = []
    events = [
        ("Normal", "Monitor Vitals", "Approved", "Steady state"),
        ("Tachycardia", "Increase Beta-Blocker", "Modified by Dr", "Clinical risk: BP too low for AI suggestion"),
        ("Minor Bleeding", "Use Bio-Sealant (Porcine-based)", "REJECTED by Dr", "Ethical Conflict: Halal alternative requested"),
        ("Normal", "Maintain Anesthesia", "Approved", "Spiritual Modesty Draping Verified"),
        ("Oxygen Drop", "Manual Ventilation Support", "Approved", "Dr took over Robotic vent control"),
        ("Suturing", "Automated Robotic Stitch", "Approved", "Precision within 0.1mm")
    ]
    for i in range(37): # 0 to 6 hours
        current_time = (start_time + timedelta(minutes=i*10)).strftime("%H:%M")
        status, ai_rec, dr_dec, note = events[i % len(events)]
        logs.append({
            "Time": current_time,
            "Patient Status": status,
            "AI Robot Advice": ai_rec,
            "Doctor Decision": dr_dec,
            "Clinical-Ethical Notes": note
        })
    return pd.DataFrame(logs)

# --- 6. PAGE LOGIC ---

if menu == "Dashboard Overview":
    st.title("System Overview")
    st.write("Integrating AI diagnostics with the ESCA+ Ethics Model. Designed for high-transparency Islamic Medical Tourism.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Clinical Competence", "98%", "JCI Verified")
    col2.metric("Spiritual Sensitivity", "100%", "Halal-Pharma")
    col3.metric("Ethical Justice", "99%", "Transparent Billing")

elif menu == "2. Advanced OT: 6-Hour Live Simulation":
    st.header("🤖 Advanced OT: 6-Hour Surgical Timeline")
    st.info("💡 Tracking the interaction between AI Robotic Advice and Doctor's Human Oversight (Every 10 Minutes).")
    
    # 3D Scan Placeholder (Removed the fruit picture!)
    if not st.session_state.scan_complete:
        if st.button("🚀 Run AI 3D Robotic Scan"):
            with st.status("Scanning anatomy... creating Digital Twin..."):
                time.sleep(2)
            st.session_state.scan_complete = True
            st.rerun()
    else:
        # Timeline Slider for the 6-hour surgery
        st.subheader("⏱️ Surgical Timeline Control")
        time_idx = st.select_slider("Select time-stamp to view procedure detail (09:00 - 15:00)", options=range(37), value=st.session_state.simulation_time_index)
        st.session_state.simulation_time_index = time_idx
        
        full_log = generate_surgery_log()
        current_log = full_log.iloc[time_idx]
        
        # Displaying the "Critical Interaction" Dashboard
        c1, c2, c3 = st.columns([1, 2, 2])
        
        with c1:
            st.metric("Timeline", f"{current_log['Time']}")
            st.write(f"**Patient Status:** {current_log['Patient Status']}")
        
        with c2:
            st.error(f"🤖 **AI Advice:** {current_log['AI Robot Advice']}")
            st.success(f"👨‍⚕️ **Dr. Decision:** {current_log['Doctor Decision']}")
            
        with c3:
            st.info(f"📝 **Note:** {current_log['Clinical-Ethical Notes']}")
            
        st.divider()
        
        # Live Vitals Simulation for that specific time
        v1, v2, v3 = st.columns(3)
        v1.metric("SpO2", "98%" if time_idx % 4 != 0 else "89%", delta="-9%" if time_idx % 4 == 0 else "Normal")
        v2.metric("HR", f"{80 + time_idx} BPM")
        v3.metric("Aurat Status", "100% Covered", "Protected")

        # Display full log up to current time
        st.subheader("📜 Detailed Surgical Log (Cumulative)")
        st.dataframe(full_log.head(time_idx + 1), use_container_width=True)

elif menu == "3. Surgical Team Transparency":
    st.header("👥 Surgical & Support Personnel")
    st.write("Under the ESCA+ Model, transparency of personnel is vital for Patient Agency.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Medical Specialists")
        st.info("**Lead Surgeon:** Dr. Adam Syarif\n- MBBS (Malaya), FRCS (London)\n- Expertise: Cardiothoracic Robotic Surgery")
        st.info("**Anesthesiologist:** Dr. Siti Hajar\n- MD (USM), MMed (Anaesth)\n- Expertise: Halal-Pharma Induction")
    with col2:
        st.subheader("Support Team")
        st.write("- **Scrub Nurse:** Nurse Aishah (OT Specialist)")
        st.write("- **Circulating Nurse:** Nurse Farida (Patient Care)")
        st.write("- **Shariah Lead:** Ustaz Hamdan (Bioethics & Modesty Monitor)")

elif menu == "4. AI Loyalty Prediction":
    st.header("🤖 AI Patient Loyalty Engine")
    score = st.slider("Select ESCA+ Alignment Score (%)", 0, 100, 85)
    st.metric("Predicted Loyalty", f"{score * 0.95}%")
    st.progress(score/100)

else:
    st.header("💰 Financial & Ethical Audit")
    st.table(pd.DataFrame({"Service": ["AI Robotic Scan", "Surgery", "Audit"], "Cost (RM)": [5000, 15000, 0]}))

st.sidebar.divider()
st.sidebar.write(f"© 2025 **Mohd Khairul Ridhuan Bin Mohd Fadzil**")
