# ---------------------------------------------------------
# PAGE 2: MEDICAL TEAM & LIVE SURGERY (ENHANCED SIMULATION)
# ---------------------------------------------------------
elif menu == "2. Medical Team & Live Surgery":
    st.title("🔴 Operation Theater (OT) Live Digital Link")
    st.write("---")
    
    # 1. Info Pesakit (Context: Ampang Accident Case)
    c1, c2, c3 = st.columns(3)
    c1.metric("Patient Name", "Sarah J. Abdullah")
    c2.metric("Procedure", "Emergency Cardiothoracic Surgery")
    c3.metric("OT Room", "OT-04 (Hybrid)")

    st.divider()

    # 2. OT TEAM BOARD (The Staffing)
    st.subheader("👥 The Surgical Team (On-Duty)")
    col_team1, col_team2 = st.columns(2)
    
    with col_team1:
        st.markdown("""
        **Medical Specialists:**
        *   👨‍⚕️ **Lead Surgeon:** Dr. Adam Syarif (MBBS, FRCS London)
        *   👩‍⚕️ **Assisting Surgeon:** Dr. Johan Ariff (MD, MSurg)
        *   👩‍⚕️ **Anesthesiologist:** Dr. Siti Hajar (Critical Care Specialist)
        """)
    
    with col_team2:
        st.markdown("""
        **Nursing & Support Team:**
        *   👩‍⚕️ **Scrub Nurse:** Nurse Aishah (OT Specialist)
        *   👩‍⚕️ **Circulating Nurse:** Nurse Farida (Patient Care)
        *   👨‍⚕️ **Perfusionist:** Mr. Zaid (Heart-Lung Machine)
        *   🌙 **Shariah Officer:** Ustaz Hamdan (On-Call Consultant)
        """)

    st.divider()

    # 3. LIVE PROCEDURE SIMULATOR (Step-by-Step)
    st.subheader("⏱️ Live Procedure Tracking & ESCA+ Compliance")
    
    # Simulation Logic
    surgery_steps = [
        {"step": "Patient Positioning & Aurat Draping", "status": "Completed ✅", "esca": "Spiritual Sensitivity (High)"},
        {"step": "Anesthesia Induction (Halal-Pharma)", "status": "Completed ✅", "esca": "Institutional Integrity"},
        {"step": "Surgical Incision", "status": "In Progress 🔵", "esca": "Clinical Competence"},
        {"step": "Internal Tissue Repair & Hemostasis", "status": "Pending ⏳", "esca": "Clinical Competence"},
        {"step": "Final Instrument & Gauze Count", "status": "Pending ⏳", "esca": "Clinical Competence (Safety)"},
        {"step": "Wound Closure & Post-Op Cleaning", "status": "Pending ⏳", "esca": "Dignity Preservation"}
    ]

    # Displaying the "Live" Log
    for i, s in enumerate(surgery_steps):
        with st.expander(f"Phase {i+1}: {s['step']}", expanded=(s['status'] == "In Progress 🔵")):
            col_s1, col_s2 = st.columns(2)
            col_s1.write(f"**Status:** {s['status']}")
            col_s2.write(f"**ESCA+ Domain:** {s['esca']}")
            if s['status'] == "In Progress 🔵":
                st.toast(f"Current Phase: {s['step']}", icon="🏥")
                st.spinner("Surgeon is performing critical intervention...")

    st.divider()

    # 4. REAL-TIME TELEMETRY (Visual Feedback)
    st.subheader("📊 Live Clinical Vitals & Ethical Status")
    v1, v2, v3 = st.columns(3)
    v1.metric("Heart Rate", "88 BPM", "Stable")
    v2.metric("Oxygen (SpO2)", "98%", "Normal")
    v3.metric("Aurat Protection", "Active", "100% Covered")
    
    st.info("💡 **Education Note:** This dashboard provides transparency for guardians while maintaining sterile environment and patient privacy.")
