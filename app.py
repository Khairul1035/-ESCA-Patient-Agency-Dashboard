import streamlit as st
import pandas as pd
import time
from datetime import datetime
import plotly.express as px

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Industrial Dashboard", layout="wide", page_icon="🏥")

# --- LEAD RESEARCHER & SYSTEM INFO ---
st.sidebar.markdown(f"""
### 🔬 Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*Reframing Islamic Medical Tourism*

**System Status:** 🟢 Live
**Server Time:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
""")

# Language Selection
lang = st.sidebar.selectbox("🌐 Select Language / Pilih Bahasa", ["English", "Bahasa Melayu", "العربية"])

st.sidebar.divider()

# --- APP NAVIGATION ---
menu = st.sidebar.radio("Main Menu", ["Registration & Intake", "Clinical Command Center", "Patient Agency Log", "Financial & Audit"])

# --- SESSION STATE (Mock Database) ---
if 'patient_data' not in st.session_state:
    st.session_state.patient_data = {
        "name": "Sarah J. Abdullah",
        "id": "P-992837",
        "citizenship": "United Kingdom",
        "passport_ic": "UK-8822990",
        "admission_date": datetime.now().strftime('%d/%m/%Y %H:%M'),
        "urgency": "High (Red Zone)",
        "agency_decisions": []
    }

# ---------------------------------------------------------
# PAGE 1: REGISTRATION & INTAKE
# ---------------------------------------------------------
if menu == "Registration & Intake":
    st.title("📋 Patient Intake & Value Passport")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Personal Identification")
        name = st.text_input("Full Name", value=st.session_state.patient_data["name"])
        citizenship = st.selectbox("Citizenship", ["Malaysian", "International (Tourist)"], index=1)
        id_num = st.text_input("IC / Passport Number", value=st.session_state.patient_data["passport_ic"])
        country = st.text_input("Country of Origin", value="United Kingdom")
        
    with col2:
        st.subheader("Admission Details")
        st.write(f"**Date & Time of Intake:** {st.session_state.patient_data['admission_date']}")
        st.selectbox("Triage Level", ["Red (Critical)", "Yellow (Semi-Critical)", "Green (Non-Urgent)"], index=0)
        st.text_input("Insurance Provider", value="Allianz Global Care")

    st.divider()
    st.subheader("🛡️ ESCA+ Value Passport (Patient Agency)")
    st.info("Ask the patient or guardian to select their preferred care values.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        gender = st.radio("Clinical Gender Preference", ["Same Gender", "No Preference", "Flexible (Darurah)"])
    with c2:
        diet = st.multiselect("Dietary Requirements", ["Halal-Certified", "Vegan", "Vegetarian", "No Beef"])
    with c3:
        modesty = st.toggle("Activate High Modesty Protocol (Extra Draping)")

    if st.button("Finalize Registration"):
        st.success("Patient registered and Value Passport synced to Hospital HIS.")

# ---------------------------------------------------------
# PAGE 2: CLINICAL COMMAND CENTER
# ---------------------------------------------------------
elif menu == "Clinical Command Center":
    st.title("👨‍⚕️ Real-Time Clinical Monitor")
    
    st.warning(f"🚨 **EMERGENCY ALERT:** Patient {st.session_state.patient_data['name']} requires immediate intervention.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Clinical Vitals (HIS Integration)")
        vitals = pd.DataFrame({
            "Metric": ["Heart Rate (BPM)", "Blood Pressure", "SpO2 (%)", "Temp (°C)"],
            "Current": [115, "90/60", 92, 37.2],
            "Status": ["High", "Low", "Critical", "Normal"]
        })
        st.table(vitals)
        
        st.subheader("Decision Support: The 'Darurah' Resolver")
        st.error("**Conflict Identified:** Patient prefers same-gender care, but current available specialist is Male (Dr. Adam).")
        
        if st.button("🚨 TRIGGER EMERGENCY DARURAH OVERRIDE"):
            timestamp = datetime.now().strftime('%H:%M:%S')
            st.session_state.patient_data["agency_decisions"].append({
                "time": timestamp,
                "event": "Darurah Override Triggered",
                "details": "Surgery proceeded with Male Dr due to life-saving urgency."
            })
            st.success(f"Darurah Protocol activated at {timestamp}. All clinical actions logged for audit.")

    with col2:
        st.subheader("ESCA+ Domain Status")
        st.progress(0.9, text="Clinical Competence")
        st.progress(0.7, text="Spiritual Sensitivity")
        st.progress(1.0, text="Ethical Justice")

# ---------------------------------------------------------
# PAGE 3: PATIENT AGENCY LOG
# ---------------------------------------------------------
elif menu == "Patient Agency Log":
    st.title("📜 Patient Agency & Interaction Log")
    st.write("This log tracks every decision made by the patient or guardian for transparency.")
    
    if st.session_state.patient_data["agency_decisions"]:
        df_log = pd.DataFrame(st.session_state.patient_data["agency_decisions"])
        st.table(df_log)
    else:
        st.write("No decisions logged yet.")
        
    st.divider()
    st.subheader("Post-Procedure Integrity Check")
    st.checkbox("Aurat/Modesty was maintained during surgery")
    st.checkbox("Patient was informed of 'Darurah' override post-stabilization")
    st.text_area("Guardian Comments")

# ---------------------------------------------------------
# PAGE 4: FINANCIAL & AUDIT (Corrected Version)
# ---------------------------------------------------------
else:
    st.title("💰 Ethical Justice: Billing & Audit")
    
    # Corrected column naming: c1 and c2
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Real-Time Billing")
        bill_type = "International Rate" if st.session_state.patient_data["citizenship"] == "International (Tourist)" else "Malaysian Rate"
        st.write(f"**Billing Category:** {bill_type}")
        
        costs = {
            "Item": ["Emergency Surgery", "ICU Ward (Daily)", "Halal Anesthesia", "ESCA+ Spiritual Care"],
            "Amount (RM)": [12000, 2500, 800, 0] 
        }
        st.table(pd.DataFrame(costs))
        
    with c2: # FIXED: Changed from col2 to c2
        st.subheader("Institutional Integrity Report")
        fig = px.pie(values=[90, 10], names=['Compliant', 'Non-Compliant'], title="Hospital Integrity Score")
        st.plotly_chart(fig)
        
    st.button("Generate Compliance Certificate for MHTC/JAKIM")
