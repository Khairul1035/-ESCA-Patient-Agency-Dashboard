import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Hospital Alpha | The ESCA+ Journey", layout="wide", page_icon="🏥")

# --- 2. SESSION STATE (Managing the Story Flow) ---
if 'journey_phase' not in st.session_state:
    st.session_state.journey_phase = "Accident"
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 1589
if 'scan_data' not in st.session_state:
    st.session_state.scan_data = None

# --- 3. SIDEBAR: LEAD RESEARCHER PROFILE ---
st.sidebar.header("Lead Researcher")
st.sidebar.subheader("MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL")
with st.sidebar.expander("🎓 Expertise & Profile"):
    st.write("""
    - **Business Management & Islamic Studies**
    - **Corporate Sustainability**
    - **AI & Machine Learning (Self-Taught)**
    - **Human-Computer Interaction (HCI)**
    """)
st.sidebar.divider()
st.sidebar.write(f"📈 **Project Visitors:** `{st.session_state.visitor_count + 1}`")
st.sidebar.write(f"📅 **Date:** {datetime.now().strftime('%d %B %Y')}")
st.sidebar.divider()

# Navigation via Story Phases
st.sidebar.title("Journey Phases")
phase_options = [
    "Accident & Triage", 
    "AI Robotic Diagnostics", 
    "Specialist Matching", 
    "Live OT (6-Hour Simulation)", 
    "Outcomes & Billing"
]
st.session_state.journey_phase = st.sidebar.radio("Go to Phase:", phase_options)

# --- 4. GLOBAL HEADER & DISCLAIMER ---
st.markdown("<h1 style='text-align: center; color: #004d99;'>HOSPITAL ALPHA: THE ESCA+ JOURNEY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Real-time AI Simulation for High-Trauma Emergency Cases</p>", unsafe_allow_html=True)
st.warning("⚠️ **DISCLAIMER:** This application is for **EDUCATION PURPOSE ONLY**. All data, clinical outcomes, and AI logic are research prototypes by Mohd Khairul Ridhuan.")

# --- 5. STORYTELLING & LOGIC ---

# PHASE 1: ACCIDENT & TRIAGE
if st.session_state.journey_phase == "Accident & Triage":
    st.header("📍 Phase 1: Emergency Impact")
    st.error("**SCENARIO:** A family of three involved in a high-speed collision on the MRR2 Highway. A witness (Good Samaritan) rushes the victims to Hospital Alpha—the nearest ESCA+ certified center.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Good Samaritan Registration")
        witness = st.text_input("Witness Name", placeholder="Enter name of the citizen rescuer")
        st.info("Under ESCA+ Ethical Justice, the witness is legally protected and not liable for costs.")
    with col2:
        st.subheader("Initial Triage")
        st.write("**Victims:** Father (Stable), Mother (Critical), Child (Critical).")
        st.write("**Status:** Triage Red. Immediate AI Diagnostic Scan requested.")
    
    st.divider()
    st.subheader("🛡️ Initial ESCA+ Value Passport")
    st.write("Even in crisis, Hospital Alpha initiates dignity protocols.")
    st.toggle("Activate High Modesty (Aurat) Protocol", value=True)
    st.toggle("Halal-Pharma Only Anesthesia", value=True)

# PHASE 2: AI ROBOTIC DIAGNOSTICS
elif st.session_state.journey_phase == "AI Robotic Diagnostics":
    st.header("📡 Phase 2: AI Robotic Full-Body Scanning")
    st.write("The victims are placed in the AI Robotic Scanner. The algorithm analyzes damage and survival probability.")
    
    if st.button("🚀 Start 360° AI Robotic Scan"):
        with st.status("AI Robot scanning Patient 01 (Mother)...", expanded=True) as status:
            time.sleep(1)
            st.write("Skeletal Mapping: Fractures detected in Thorax.")
            time.sleep(1)
            st.write("Organ Scan: Internal hemorrhage in Liver and Spleen.")
            time.sleep(1)
            st.write("Neural Scan: Brain activity stable but elevated intracranial pressure.")
            status.update(label="Scan Complete! Digital Twin Generated.", state="complete")
            st.session_state.scan_data = True

    if st.session_state.scan_data:
        c1, c2 = st.columns([2, 1])
        with c1:
            st.subheader("3D Damage Intensity (Algorithm Output)")
            # Simulated 3D Bar Chart for organ damage
            damage_df = pd.DataFrame({
                "Organ": ["Heart", "Lungs", "Liver", "Spleen", "Brain"],
                "Damage %": [15, 45, 78, 82, 30]
            })
            fig = px.bar(damage_df, x="Organ", y="Damage %", color="Damage %", color_continuous_scale="Reds")
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            st.subheader("AI Prognosis")
            st.metric("Body Damage Index", "64%", delta="Critical")
            st.metric("Survival Probability", "72.4%")
            st.error("Urgency: Surgery required within 15 minutes.")

# PHASE 3: SPECIALIST MATCHING
elif st.session_state.journey_phase == "Specialist Matching":
    st.header("👨‍⚕️ Phase 3: AI Specialist Alignment")
    st.write("Hospital Alpha's algorithm matches the trauma severity with the best available expertise.")
    
    st.subheader("Expertise Matching Result")
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("✅ **Primary Match Found (On-Call):**")
        st.info("**Dr. Adam Syarif**\n- Education: MBBS (Malaya), FRCS (London)\n- Expertise: Cardiothoracic Trauma Surgery\n- Availability: READY (OT-04)")
    
    with col2:
        st.warning("🔄 **Secondary Search (10km Radius):**")
        st.write("Analyzing nearby Hospital Alpha branches for back-up specialists due to multiple critical victims.")
        st.write("- Found: **Dr. Sarah Lim** (Pediatric Surgeon) - 4km away (En route).")
    
    st.divider()
    st.write("**Support Team Assigned:** Nurse Aishah (Scrub), Mr. Zaid (Perfusionist), Ustaz Hamdan (Shariah Ethics Monitor).")

# PHASE 4: LIVE OT (6-HOUR SIMULATION)
elif st.session_state.journey_phase == "Live OT (6-Hour Simulation)":
    st.header("🔴 Phase 4: Live Surgical Procedure Monitor")
    st.info("The Mother is in OT-04. This 6-hour timeline tracks the interaction between the AI Robot and the Surgeon.")
    
    time_idx = st.select_slider("Family View Timeline (09:00 - 15:00)", options=range(37))
    
    # 6-Hour Data Generation
    start_time = datetime.strptime("09:00", "%H:%M")
    current_time = (start_time + timedelta(minutes=time_idx*10)).strftime("%H:%M")
    
    c1, c2, c3 = st.columns([1, 2, 2])
    with c1:
        st.metric("Time", current_time)
        st.write("**Vitals:** 🟢 Stable" if time_idx < 20 else "⚠️ Critical")
    with c2:
        st.error(f"🤖 **AI Advice:** {['Optimize oxygen', 'Use bio-sealant', 'Emergency bypass'][time_idx % 3]}")
        st.success(f"👨‍⚕️ **Dr. Action:** {['Approved', 'REJECTED - Use Halal alternative', 'Handled manually'][time_idx % 3]}")
    with c3:
        st.info(f"🌙 **ESCA+ Status:** {['Aurat Covered', 'Modesty Draping Verified', 'Shariah Lead Notified'][time_idx % 3]}")

    st.subheader("Cumulative Surgical Log")
    st.caption("Updated every 10 minutes for family transparency.")
    # Show log up to current time
    st.write(f"Displaying data for first {time_idx * 10} minutes of the operation.")

# PHASE 5: OUTCOMES & BILLING
elif st.session_state.journey_phase == "Outcomes & Billing":
    st.header("💰 Phase 5: Outcomes & Ethical Accountability")
    
    st.subheader("Surgical Outcomes")
    col1, col2, col3 = st.columns(3)
    col1.success("**Mother:** SURVIVED\n(Transferred to ICU)")
    col2.warning("**Father:** STABLE\n(Ward Observation)")
    col3.error("**Child:** CRITICAL\n(Under AI Monitoring)")

    st.divider()
    
    st.subheader("Ethical Billing Transparency")
    bill_df = pd.DataFrame({
        "Service Category": ["AI Robotic Scan", "Specialist Surgery", "Spiritual Support", "Witness Intake Fee"],
        "Charge (RM)": [5000, 15000, 0, 0]
    })
    st.table(bill_df)
    st.info("💡 Note: Spiritual support and Good Samaritan processing fees are RM 0 to ensure Ethical Justice.")
    
    st.divider()
    
    st.subheader("Institutional Integrity Certificate")
    st.write("This procedure complied 99.4% with the ESCA+ Ethics Model.")
    st.button("📄 Generate Final Compliance Report (PDF)")

# --- 7. FOOTER ---
st.sidebar.divider()
st.sidebar.write(f"© 2025 **Mohd Khairul Ridhuan Bin Mohd Fadzil**")
