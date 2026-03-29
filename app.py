import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Hospital Alpha | ESCA+ Platinum Dashboard", layout="wide", page_icon="🏥")

# --- 2. SESSION STATE & COUNTERS ---
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 1248 # Mock Initial Count
if 'scan_complete' not in st.session_state:
    st.session_state.scan_complete = False
if 'sim_running' not in st.session_state:
    st.session_state.sim_running = False

# --- 3. SIDEBAR: LEAD RESEARCHER PROFILE ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
st.sidebar.header("Lead Researcher")
st.sidebar.subheader("MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL")

with st.sidebar.expander("🎓 Academic & Technical Expertise"):
    st.write("""
    - **Business Management**
    - **Islamic Studies**
    - **Corporate Sustainability**
    - **Self-Taught Machine Learning**
    - **Artificial Intelligence**
    - **Human-Computer Interaction (HCI)**
    """)

st.sidebar.divider()
st.sidebar.write(f"📈 **Project Visitors:** `{st.session_state.visitor_count + 1}`")
st.sidebar.write(f"📅 **Date:** {datetime.now().strftime('%d %B %Y')}")
st.sidebar.write(f"⏰ **Time:** {datetime.now().strftime('%H:%M:%S')}")
st.sidebar.divider()

menu = st.sidebar.radio("Navigation Menu", [
    "Dashboard Overview",
    "1. Accident Triage & Intake", 
    "2. Advanced OT: AI Scan & Surgery", 
    "3. Surgical Team Transparency", 
    "4. AI Loyalty Prediction", 
    "5. Financial & Ethical Audit"
])

# --- 4. TEAM DATA (Transparency Module) ---
surgical_team = {
    "Lead Surgeon": {
        "Name": "Dr. Adam Syarif",
        "Education": "MBBS (Malaya), FRCS (London, UK)",
        "Expertise": "Cardiothoracic Trauma & Robotic Surgery",
        "Experience": "18 Years"
    },
    "Anesthesiologist": {
        "Name": "Dr. Siti Hajar",
        "Education": "MD (USM), MMed (Anaesthesiology)",
        "Expertise": "Critical Care & Shariah-Compliant Pain Management",
        "Experience": "12 Years"
    },
    "Support Team": [
        {"Role": "Scrub Nurse", "Name": "Nurse Aishah", "Expertise": "Sterile Field & OT Logistics"},
        {"Role": "Circulating Nurse", "Name": "Nurse Farida", "Expertise": "Patient Safety Monitor"},
        {"Role": "Perfusionist", "Name": "Mr. Zaid", "Expertise": "Extracorporeal Circulation Specialist"},
        {"Role": "Shariah Consultant", "Name": "Ustaz Hamdan", "Expertise": "Bioethics & Maqasid Al-Shariah"}
    ]
}

# --- 5. GLOBAL HEADER & DISCLAIMER ---
st.markdown("<h1 style='text-align: center; color: #004d99;'>HOSPITAL ALPHA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Reframing Islamic Medical Tourism through the ESCA+ Model</p>", unsafe_allow_html=True)
st.warning("⚠️ **DISCLAIMER:** This dashboard is for **EDUCATION PURPOSE ONLY**. All clinical data and simulations are generated for research demonstration.")

# --- 6. PAGE LOGIC ---

# PAGE 0: OVERVIEW
if menu == "Dashboard Overview":
    st.title("System Overview")
    st.write("Welcome to the Hospital Alpha Ethics Command Center. This project integrates Business Management principles with AI and Islamic Bioethics.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Clinical Compliance", "98.5%", "JCI Standard")
    col2.metric("Shariah Alignment", "100%", "JAKIM/MHTC")
    col3.metric("System Uptime", "99.99%", "Real-time")
    st.image("https://img.freepik.com/free-vector/modern-medical-infographic-template_23-2148154674.jpg", caption="The ESCA+ Framework Architecture")

# PAGE 1: TRIAGE
elif menu == "1. Accident Triage & Intake":
    st.header("🚑 Emergency Intake: Accident Response (MRR2 Scenario)")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Good Samaritan Protocol")
        st.text_input("Witness Name", placeholder="Identity of person who assisted")
        st.info("Legal Protection Active: Samaritan is shielded from liability under Hospital Alpha's Ethical Justice policy.")
    with c2:
        st.subheader("Patient Digital Twin Setup")
        st.text_input("Temporary ID", "AX-2024-SAM")
        st.selectbox("Citizenship", ["Malaysian Citizen", "International Medical Tourist"], index=1)
    
    st.divider()
    st.subheader("🛡️ ESCA+ Value Passport")
    v1, v2, v3 = st.columns(3)
    v1.radio("Modesty Requirement", ["High (Shariah)", "Moderate", "Clinical Priority"])
    v2.multiselect("Dietary/Pharma", ["Halal-Pharma", "Vegan-Friendly", "No Porcine Derivatives"])
    v3.toggle("Spiritual Liaison Required (Ustaz/Chaplain)")
    st.button("Sync to Alpha-HIS Database")

# PAGE 2: ADVANCED OT
elif menu == "2. Advanced OT: AI Scan & Surgery":
    st.header("🤖 Robotic OT & AI Simulation")
    tab_scan, tab_surgery = st.tabs(["📡 3D Full-Body AI Scan", "🔴 Live Surgical Stress Monitor"])

    with tab_scan:
        if not st.session_state.scan_complete:
            if st.button("🚀 Initiate AI Body Scan"):
                with st.status("AI Robot scanning Patient... analyzing anatomy...", expanded=True) as s:
                    st.write("Head-to-toe laser mapping active...")
                    time.sleep(2)
                    st.write("Analyzing internal damage...")
                    time.sleep(1)
                    s.update(label="3D Scan Complete!", state="complete")
                    st.session_state.scan_complete = True
                    st.rerun()
        else:
            col_3d, col_met = st.columns([2, 1])
            with col_3d:
                # 3D Mapping Visualization
                z = np.random.standard_normal(100)
                fig_3d = go.Figure(data=[go.Scatter3d(x=np.random.randn(50), y=np.random.randn(50), z=np.random.randn(50), 
                                  mode='markers', marker=dict(size=5, color='red'))])
                fig_3d.update_layout(title="Anatomical Damage Hotspots (3D)", margin=dict(l=0,r=0,b=0,t=40))
                st.plotly_chart(fig_3d, use_container_width=True)
            with col_met:
                st.metric("Body Damage Index", "38.2%", delta="Critical")
                st.metric("Survival Probability", "79.1%")
                st.error("Target: Thoracic Cavity Repair Required")
            if st.button("Reset Scan"): st.session_state.scan_complete = False

    with tab_surgery:
        st.subheader("Dynamic Surgical Monitoring")
        if not st.session_state.sim_running:
            if st.button("🔴 Start Live Operation"): st.session_state.sim_running = True; st.rerun()
        else:
            if st.button("⏹ Stop Simulation"): st.session_state.sim_running = False; st.rerun()
            
            placeholder = st.empty()
            for i in range(1, 11):
                o2 = 98 - (i*2) if i > 5 else 98
                hr = 80 + (i*5)
                msg = "Crisis: Oxygen Drop!" if o2 < 90 else "Surgery in progress..."
                with placeholder.container():
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Heart Rate", f"{hr} BPM")
                    m2.metric("Oxygen (SpO2)", f"{o2}%", delta="-5%" if o2 < 90 else "Stable")
                    m3.metric("AI Precision", "99.9%")
                    st.warning(f"**Status:** {msg}")
                time.sleep(1)

# PAGE 3: TEAM TRANSPARENCY
elif menu == "3. Surgical Team Transparency":
    st.header("👥 Assigned Surgical & Support Team")
    st.write("Hospital Alpha ensures all patients know exactly who is handling their life and dignity.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Medical Specialists")
        st.info(f"👨‍⚕️ **{surgical_team['Lead Surgeon']['Name']}**\n\n*   **Education:** {surgical_team['Lead Surgeon']['Education']}\n*   **Expertise:** {surgical_team['Lead Surgeon']['Expertise']}\n*   **Experience:** {surgical_team['Lead Surgeon']['Experience']}")
        st.info(f"👩‍⚕️ **{surgical_team['Anesthesiologist']['Name']}**\n\n*   **Education:** {surgical_team['Anesthesiologist']['Education']}\n*   **Expertise:** {surgical_team['Anesthesiologist']['Expertise']}\n*   **Experience:** {surgical_team['Anesthesiologist']['Experience']}")
    
    with c2:
        st.subheader("Nursing & Support Personnel")
        for member in surgical_team["Support Team"]:
            st.write(f"**{member['Role']}:** {member['Name']} | *{member['Expertise']}*")
        st.divider()
        st.success("✅ Team alignment verified with ESCA+ Clinical Competence standards.")

# PAGE 4: AI LOYALTY
elif menu == "4. AI Loyalty Prediction":
    st.header("🤖 AI Predictive Loyalty Engine")
    s_clin = st.slider("Clinical Competence Score", 0, 100, 93)
    s_ethi = st.slider("Ethical Justice Score", 0, 100, 99)
    loyalty = (s_clin * 0.4) + (s_ethi * 0.6)
    
    fig_g = go.Figure(go.Indicator(mode = "gauge+number", value = loyalty, 
                                   title = {'text': "Loyalty Probability (%)"},
                                   gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "darkblue"}}))
    st.plotly_chart(fig_g)
    st.info("Logic: AI prioritizes Ethical Justice (Transparency/Billing) as the key driver for medical tourist retention.")

# PAGE 5: AUDIT
else:
    st.header("💰 Ethical Billing & Integrity Audit")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.subheader("Transparent Real-time Billing")
        bill = pd.DataFrame({"Item": ["AI Robot Surcharge", "Cardiothoracic Surgery", "Spiritual Care Support"], "Cost (RM)": [5000, 15000, 0]})
        st.table(bill)
        st.caption("Note: Under Hospital Alpha policy, Spiritual Support is provided free of charge.")
    with col_f2:
        st.subheader("Integrity Compliance Index")
        st.plotly_chart(px.pie(values=[95, 5], names=['Compliant', 'Variance'], hole=.3))

st.markdown("---")
st.write(f"© 2025 **Mohd Khairul Ridhuan Bin Mohd Fadzil** | Hospital Alpha Research Unit")
