import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# --- 1. CONFIGURATION & RESEARCHER INFO ---
st.set_page_config(page_title="ESCA+ Platinum AI Dashboard", layout="wide", page_icon="🌙")

st.sidebar.markdown(f"""
### 🔬 Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*Reframing Islamic Medical Tourism*

**System Status:** 🟢 Live
**Server Time:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
""")

lang = st.sidebar.selectbox("🌐 UI Language", ["English", "Bahasa Melayu", "العربية"])
st.sidebar.divider()

# --- 2. SESSION STATE (Database Initialization) ---
if 'scan_complete' not in st.session_state:
    st.session_state.scan_complete = False
if 'agency_decisions' not in st.session_state:
    st.session_state.agency_decisions = []
if 'esca_scores' not in st.session_state:
    st.session_state.esca_scores = {"Clinical": 93, "Spiritual": 83, "Ethical": 99, "Integrity": 90, "Agency": 87}

# --- 3. MAIN NAVIGATION ---
menu = st.sidebar.radio("Main Menu", [
    "1. Good Samaritan & Intake", 
    "2. Advanced OT: AI Scan & Team", 
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
    with c1: st.radio("Gender Preference", ["Same Gender", "No Preference", "Flexible (Darurah)"])
    with c2: st.multiselect("Dietary Needs", ["Halal-Certified", "Vegan", "Vegetarian"])
    with c3: st.toggle("High Modesty Protocol (Extra Draping)")
    if st.button("Finalize Intake & Sync with HIS"):
        st.success("Intake Process Complete. Patient AX-2024 is now active.")

# PAGE 2: ADVANCED OT: AI SCAN & TEAM (RE-INTEGRATED & ENHANCED)
elif menu == "2. Advanced OT: AI Scan & Team":
    st.title("🤖 Advanced AI Robotic OT & Surgical Team")
    st.write("---")

    # Menggunakan TABS untuk mengelakkan dashboard nampak terlalu sesak (Excessive)
    tab_scan, tab_team, tab_live = st.tabs(["📡 AI Diagnostic Scan", "👥 Medical Team Profiles", "🔴 Live Procedure Log"])

    with tab_scan:
        st.subheader("AI Robotic Full-Body Diagnostic")
        if not st.session_state.scan_complete:
            if st.button("🚀 Start AI Body Scan"):
                with st.status("AI Robot scanning patient Sarah J. Abdullah...", expanded=True) as status:
                    st.write("Scanning skeletal structure...")
                    time.sleep(1)
                    st.write("Analyzing internal hemorrhaging...")
                    time.sleep(1)
                    st.write("Calculating survival probability...")
                    time.sleep(1)
                    status.update(label="Scan Complete!", state="complete", expanded=False)
                    st.session_state.scan_complete = True
                    st.rerun()
        else:
            col_diag, col_prog = st.columns([2, 1])
            with col_diag:
                # Visualisasi Damage
                d_val = [45, 12, 65, 5, 20]
                d_lab = ["Head", "Thorax", "Abdomen", "Spine", "Extremities"]
                fig_damage = px.bar(x=d_lab, y=d_val, labels={'x':'Region', 'y':'Damage %'}, 
                                    title="AI Organ Damage Intensity", color=d_val, color_continuous_scale='Reds')
                st.plotly_chart(fig_damage, use_container_width=True)
            with col_prog:
                st.metric("Survival Probability", "78.4%", delta="Stable")
                st.metric("Estimated Op Duration", "4H 20M")
                st.metric("Aurat Protection", "Active", "100% Covered")
            if st.button("🔄 New Scan"):
                st.session_state.scan_complete = False
                st.rerun()

    with tab_team:
        st.subheader("Assigned Surgical Experts")
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.info("👨‍⚕️ **Primary Surgeon:** Dr. Adam Syarif\n\n**Education:** MBBS (Malaya), FRCS (London, UK)\n\n**Specialty:** Cardiothoracic Trauma (15 yrs exp)")
            st.info("👩‍⚕️ **Anesthesiologist:** Dr. Siti Hajar\n\n**Education:** MD (USM), MMed (Anaesth)\n\n**Expertise:** Critical Care & Halal-Pharma Induction")
        with col_t2:
            st.info("👩‍⚕️ **Scrub Nurse:** Nurse Aishah (OT Specialist)")
            st.info("👨‍⚕️ **Perfusionist:** Mr. Zaid (Heart-Lung Machine)")
            st.info("🌙 **Shariah Lead:** Ustaz Hamdan (On-Call Ethical Consultant)")

    with tab_live:
        st.subheader("Real-Time Procedure Monitoring")
        log_data = {
            "Time": ["14:45", "14:55", "15:10", "15:25"],
            "Procedure Step": ["Incision Started", "Anesthesia Verified", "Liver Repair Active", "Bleeding Controlled"],
            "ESCA Domain": ["Clinical", "Integrity", "Clinical", "Clinical"]
        }
        st.table(pd.DataFrame(log_data))
        st.toast("Current Phase: Internal Organ Repair", icon="🏥")

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
        st.error("Conflict: Male Surgeon available (Emergency)")
        if st.button("TRIGGER DARURAH OVERRIDE"):
            ts = datetime.now().strftime('%H:%M:%S')
            st.session_state.agency_decisions.append({"time": ts, "event": "Darurah Consent", "details": "Authorized Male Dr"})
            st.warning(f"Authorized at {ts}")
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
        query = st.text_input("Search Fatwa (e.g., Insulin)")
        if query: st.info(f"Result for '{query}': Permissible (Harus) in emergency situations.")

# PAGE 5: AI PATIENT LOYALTY PREDICTOR
elif menu == "5. AI Patient Loyalty Predictor":
    st.title("🤖 ESCA+ AI Predictive Engine")
    s_clin = st.slider("Clinical Competence", 0, 100, st.session_state.esca_scores["Clinical"])
    s_spir = st.slider("Spiritual Sensitivity", 0, 100, st.session_state.esca_scores["Spiritual"])
    s_ethi = st.slider("Ethical Justice", 0, 100, st.session_state.esca_scores["Ethical"])
    loyalty_score = (s_clin * 0.25) + (s_spir * 0.15) + (s_ethi * 0.30) + (100 * 0.30) 
    
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
        bill = pd.DataFrame({"Item": ["Surgery", "ICU", "Good Samaritan Case Fee", "Spiritual Support"], "Cost (RM)": [15000, 2500, 0, 0]})
        st.table(bill)
    with c2:
        st.subheader("Audit Integrity Score")
        st.plotly_chart(px.pie(values=[95, 5], names=['Compliant', 'Non-Compliant'], title="Institutional Integrity Index"))
    st.button("📄 Generate ESCA+ Compliance Certificate")
    st.write(f"© 2025 Mohd Khairul Ridhuan Bin Mohd Fadzil")
