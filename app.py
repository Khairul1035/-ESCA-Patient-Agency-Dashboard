import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Platinum Dashboard", layout="wide", page_icon="🌙")

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
    "Good Samaritan Protocol (Accident Intake)", 
    "Medical Team Profiles", 
    "Live Surgery Procedure", 
    "Patient Agency & Value Passport", 
    "Financial & Audit"
])

# --- SESSION STATE (Mock Database) ---
if 'patient_status' not in st.session_state:
    st.session_state.patient_status = "Unidentified" # Default for accidents
if 'surgery_step' not in st.session_state:
    st.session_state.surgery_step = 0
if 'agency_decisions' not in st.session_state:
    st.session_state.agency_decisions = []

# ---------------------------------------------------------
# PAGE 1: GOOD SAMARITAN PROTOCOL (For Strangers/Witnesses)
# ---------------------------------------------------------
if menu == "Good Samaritan Protocol (Accident Intake)":
    st.title("🚑 Good Samaritan & Accident Witness Protocol")
    st.info("Protocol for witnesses who bring an unidentified victim to the hospital.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Step 1: Witness/Samaritan Registration")
        witness_name = st.text_input("Witness Full Name")
        witness_phone = st.text_input("Witness Contact Number")
        st.write("---")
        st.subheader("Step 2: Legal Protection Notice")
        st.success("""
        **Notice to Witness:** 
        Under the 'Duty of Care' and Ethical Justice domain, you are protected by hospital policy for 
        bringing a victim in good faith. You are NOT liable for the victim's medical costs.
        """)
        
    with col2:
        st.subheader("Step 3: Preliminary Victim Details")
        st.write("If identity is unknown, use 'Unknown Patient' profile.")
        gender = st.selectbox("Estimated Gender", ["Male", "Female", "Unknown"])
        location = st.text_input("Accident Location", value="MRR2 Ampang")
        belongings = st.text_area("List of belongings found (ID, Wallet, Phone)")
        
        if st.button("Finalize Emergency Admission"):
            st.session_state.patient_status = "Identified (Emergency)"
            st.success("Triage Notified. Patient AX-2024 registered. Medical Team Dispatched.")

# ---------------------------------------------------------
# PAGE 2: MEDICAL TEAM PROFILES (Clinical Competence)
# ---------------------------------------------------------
elif menu == "Medical Team Profiles":
    st.title("👨‍⚕️ Assigned Medical Specialists")
    st.write("Building trust through Transparency and Clinical Competence.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=150)
        st.subheader("Dr. Adam Syarif")
        st.write("**Specialty:** Senior Trauma & Cardiothoracic Surgeon")
        st.write("**Education:** MBBS (Malaya), FRCS (London, UK)")
        st.write("**Experience:** 15+ years in Emergency Surgical Interventions")
        st.info("Note: Dr. Adam is the Primary Surgeon for current emergency case.")
        
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3304/3304567.png", width=150)
        st.subheader("Dr. Siti Hajar")
        st.write("**Specialty:** Anesthesiologist & Critical Care")
        st.write("**Education:** MD (USM), Master of Medicine (Anaesth)")
        st.write("**Special Focus:** Shariah-Compliant Pain Management (Halal Pharma)")

# ---------------------------------------------------------
# PAGE 3: LIVE SURGERY PROCEDURE (Real-Time Tracker)
# ---------------------------------------------------------
elif menu == "Live Surgery Procedure":
    st.title("🔴 Live Procedure Monitor: Operating Theater 04")
    st.write("Real-time tracking for family/guardians to monitor clinical and ethical compliance.")
    
    steps = [
        "Pre-op Stabilization & Anesthesia", 
        "Surgical Incision (Procedure Started)", 
        "Main Clinical Intervention (Repair)", 
        "Closure & Cleaning", 
        "Recovery Room (Post-Op)"
    ]
    
    # Progress Bar for Surgery
    st.session_state.surgery_step = st.slider("Surgery Progress Stage", 0, 4, st.session_state.surgery_step)
    st.progress((st.session_state.surgery_step + 1) / 5)
    
    st.subheader(f"Current Status: {steps[st.session_state.surgery_step]}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("📋 **Clinical Checklist**")
        st.checkbox("Vitals Monitored (Continuous)", value=True)
        st.checkbox("Internal Bleeding Controlled", value=st.session_state.surgery_step >= 2)
        
    with col2:
        st.write("🌙 **ESCA+ Ethical Checklist**")
        st.checkbox("Minimum Body Exposure (Aurat Draping)", value=True)
        st.checkbox("Halal-Certified Medical Supplies Used", value=True)
        
    st.info("System Alert: Surgery is proceeding smoothly according to JCI and ESCA+ Ethics protocols.")

# ---------------------------------------------------------
# PAGE 4: PATIENT AGENCY & VALUE PASSPORT
# ---------------------------------------------------------
elif menu == "Patient Agency & Value Passport":
    st.title("🛡️ Patient Agency & Conflict Resolution")
    
    # Radar Chart for ESCA+ Domains
    st.subheader("Domain Alignment Matrix")
    categories = ['Clinical Competence', 'Spiritual Sensitivity', 'Ethical Justice', 'Institutional Integrity', 'Patient Agency']
    values = [98, 85, 100, 95, 90]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=values, theta=categories, fill='toself', name='ESCA+ Alignment'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
    st.plotly_chart(fig)
    
    st.divider()
    st.warning("⚠️ **Darurah Protocol Alert:** Only Male Surgeon available for life-saving surgery.")
    if st.button("Confirm Guardian Authorization for Darurah Mode"):
        st.session_state.agency_decisions.append({
            "Time": datetime.now().strftime('%H:%M'),
            "Action": "Darurah Consent",
            "Details": "Guardian authorized Dr. Adam (Male) for emergency surgery."
        })
        st.success("Authorization Logged.")

# ---------------------------------------------------------
# PAGE 5: FINANCIAL & AUDIT
# ---------------------------------------------------------
else:
    st.title("💰 Ethical Justice: Billing & Accountability")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Transparent Real-Time Billing")
        bill = pd.DataFrame({
            "Service Item": ["Emergency Surgery", "ICU Room", "Good Samaritan Intake Fee", "Spiritual Support"],
            "Cost (RM)": [15000, 2000, 0, 0]
        })
        st.table(bill)
        st.caption("Note: Good Samaritan intake and Spiritual Support are free under Ethical Justice.")
        
    with c2:
        st.subheader("Audit & Integrity Certificate")
        st.write("Audit compliant for MHTC and JAKIM standards.")
        st.button("📄 Generate ESCA+ Compliance PDF")

    st.divider()
    st.write(f"**Lead Researcher:** Mohd Khairul Ridhuan Bin Mohd Fadzil (2025)")
