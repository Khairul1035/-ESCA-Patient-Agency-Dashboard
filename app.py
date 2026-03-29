import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Patient Agency Dashboard", layout="wide")

# --- LEAD RESEARCHER CREDIT ---
st.sidebar.markdown(f"""
## Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*Project: ESCA+ Ethics Model Translation*
""")

st.sidebar.divider()

# --- APP NAVIGATION ---
menu = st.sidebar.radio("Navigation", ["Patient/Guardian Portal", "Hospital Clinical Monitor", "Audit & Integrity Analytics"])

# --- MOCK DATA / SESSION STATE ---
if 'emergency_status' not in st.session_state:
    st.session_state.emergency_status = "In Progress"
if 'agency_consents' not in st.session_state:
    st.session_state.agency_consents = {}
if 'conflict_resolved' not in st.session_state:
    st.session_state.conflict_resolved = False

# ---------------------------------------------------------
# PAGE 1: PATIENT / GUARDIAN PORTAL (The "Agency" Input)
# ---------------------------------------------------------
if menu == "Patient/Guardian Portal":
    st.title("🏥 ESCA+ Patient Agency Portal")
    st.subheader("Scenario: Emergency Admission (Ampang Accident Case)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info("⚠️ **Emergency Alert:** Your family member (Patient ID: AX-992) is currently in the Triage Zone.")
        st.write("Please set your **Value-Based Preferences** below to guide our clinical team.")
        
        with st.expander("🛡️ Step 1: Set Your Value Passport", expanded=True):
            gender_pref = st.radio("Clinical Gender Preference:", 
                                  ["No Preference", "Strictly Same-Gender (Female for Female)", "Preferred Same-Gender (Flexible in Emergency)"])
            halal_pref = st.toggle("Require Halal-Certified Medication only (where available)")
            modesty_pref = st.toggle("Activate Maximum Modesty Protocol (Minimum physical exposure during procedures)")
            
            if st.button("Save Value Passport"):
                st.session_state.agency_consents['prefs'] = {
                    "gender": gender_pref,
                    "halal": halal_pref,
                    "modesty": modesty_pref
                }
                st.success("Values synced with Hospital HIS successfully!")

    with col2:
        st.metric(label="ESCA+ Alignment Score", value="94%", delta="Target: 100%")
        st.write("**Real-Time Status:**")
        st.status("Stabilizing Patient...")

    # Conflict Negotiation Simulation
    st.divider()
    st.header("⚖️ Real-Time Conflict Negotiation")
    st.warning("🚨 **CONFLICT DETECTED:** Clinical Urgency vs. Spiritual Sensitivity")
    st.write("**Issue:** Patient requested a Female Surgeon. Currently, only Dr. Adam (Male) is available for immediate life-saving surgery.")
    
    if not st.session_state.conflict_resolved:
        st.error("Action Required: Do you authorize 'Darurah' (Emergency Override) for Dr. Adam to proceed?")
        col_a, col_b = st.columns(2)
        if col_a.button("YES - PROCEED (Life First)"):
            st.session_state.conflict_resolved = True
            st.rerun()
        if col_b.button("NO - WAIT FOR FEMALE DR."):
            st.write("Alert: Clinical risk is increasing.")
    else:
        st.success("✅ **Conflict Resolved:** You authorized 'Darurah' Protocol at 14:22 PM. Surgery is in progress.")

# ---------------------------------------------------------
# PAGE 2: HOSPITAL CLINICAL MONITOR (Staff View)
# ---------------------------------------------------------
elif menu == "Hospital Clinical Monitor":
    st.title("👨‍⚕️ ESCA+ Clinical Command Center")
    st.write("Monitoring: **Zon Merah (Red Zone) - Hospital Ampang**")

    # Patient List
    data = {
        "Patient ID": ["AX-992 (Accident Case)", "BY-110", "CZ-441"],
        "Clinical Urgency": ["CRITICAL", "STABLE", "STABLE"],
        "ESCA+ Profile": ["High Sensitivity", "Standard", "Moderate"],
        "Current Protocol": ["Darurah Mode Active", "Standard SOP", "Modesty Watch"]
    }
    df = pd.DataFrame(data)
    st.table(df)

    st.subheader("Procedure Monitor: Operating Theater 04")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("📋 **Clinical Competence (JCI)**")
        st.checkbox("Patient ID Verified", value=True)
        st.checkbox("Sterilization Complete", value=True)
        st.progress(100)
        
    with col2:
        st.write("🌙 **Spiritual Sensitivity**")
        st.checkbox("Aurat/Modesty Covering Applied", value=True)
        st.checkbox("Halal-Anesthesia Verified", value=True)
        st.progress(85)
        
    with col3:
        st.write("⚖️ **Ethical Justice**")
        st.checkbox("Guardian Informed of Changes", value=True)
        st.checkbox("Consent Recorded via App", value=True)
        st.progress(100)

# ---------------------------------------------------------
# PAGE 3: AUDIT & INTEGRITY ANALYTICS (Admin View)
# ---------------------------------------------------------
else:
    st.title("📊 Institutional Integrity Analytics")
    st.write("Transparency Report for **MHTC / JAKIM / JCI Audits**")

    m1, m2, m3 = st.columns(3)
    m1.metric("Patient Agency Fulfillment", "92%")
    m2.metric("Emergency 'Darurah' Accuracy", "100%")
    m3.metric("Loyalty Intention Index", "4.8/5.0")

    st.subheader("Ethical Billing Transparency (Real-Time)")
    chart_data = pd.DataFrame({
        'Category': ['Clinical/Surgery', 'Spiritual Services', 'Admin/Wards'],
        'Cost (RM)': [15000, 0, 1200]
    })
    st.bar_chart(chart_data, x='Category', y='Cost (RM)')
    st.caption("Note: No surcharges were applied for Shariah-Compliant protocols (Ethical Justice).")

    st.subheader("Audit Log")
    st.code("""
    [14:10] Patient AX-992 Registered. Agency Profile: High Sensitivity.
    [14:15] Clinical Conflict: Gender preference vs Surgeon availability.
    [14:22] Guardian authorized Darurah Mode via ESCA+ Dashboard.
    [14:45] Surgery Started. Modesty draping verified by OT Supervisor.
    [16:00] Surgery Successful. Integrity Index: Pass.
    """)
