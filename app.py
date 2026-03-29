import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Platinum AI-Robotic Dashboard", layout="wide", page_icon="🌙")

# --- LEAD RESEARCHER INFO ---
st.sidebar.markdown(f"""
### 🔬 Lead Researcher
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
*AI-Robotic Surgical Twin Model*

**System Status:** 🟢 Active
""")

menu = st.sidebar.radio("Main Menu", [
    "1. Registration & Intake", 
    "2. AI ROBOTIC OT: 3D SCAN & SURGERY", # Visi Terbaru
    "3. Medical Team Profiles", 
    "4. AI Loyalty Predictor", 
    "5. Financial & Audit Reports"
])

# --- 2. SESSION STATE ---
if 'scan_complete' not in st.session_state:
    st.session_state.scan_complete = False
if 'sim_running' not in st.session_state:
    st.session_state.sim_running = False

# ---------------------------------------------------------
# PAGE 1: REGISTRATION (RETAINED)
# ---------------------------------------------------------
if menu == "1. Registration & Intake":
    st.title("🚑 Patient Intake: Sarah J. Abdullah")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Demographics")
        st.text_input("Name", "Sarah J. Abdullah")
        st.text_input("Passport", "UK-8822990")
    with c2:
        st.subheader("ESCA+ Value Passport")
        st.toggle("High Modesty Protocol (Shariah-Compliant)")
    st.button("Finalize Intake")

# ---------------------------------------------------------
# PAGE 2: AI ROBOTIC OT (3D SCAN + DYNAMIC SURGERY)
# ---------------------------------------------------------
elif menu == "2. AI ROBOTIC OT: 3D SCAN & SURGERY":
    st.title("🤖 Advanced AI Robotic Operation Theater")
    st.info("💡 Concept: Automated 3D Head-to-Toe Scanning & AI-Assisted Surgical Mapping.")

    # TABS: Imbasan vs Pembedahan
    tab_scan, tab_op = st.tabs(["📡 AI 3D Full-Body Scan", "🔴 Dynamic Surgical Stress Test"])

    with tab_scan:
        if not st.session_state.scan_complete:
            if st.button("🚀 INITIATE ROBOTIC SCAN"):
                with st.status("AI Robot scanning patient Sarah J. Abdullah...", expanded=True) as status:
                    st.write("Initializing 3D Laser Mapping...")
                    time.sleep(1)
                    st.write("Scanning Thoracic Cavity... [Internal Bleeding Detected]")
                    time.sleep(1)
                    st.write("Analyzing Abdominal Organs... [Liver Laceration Confirmed]")
                    time.sleep(1)
                    status.update(label="Scan Complete! Digital Twin Generated.", state="complete")
                    st.session_state.scan_complete = True
                    st.rerun()
        else:
            col_3d, col_diag = st.columns([2, 1])
            
            with col_3d:
                st.subheader("👤 Digital Twin: 3D Anatomical Mapping")
                # Menggunakan Plotly 3D untuk meniru bentuk manusia dan kecederaan
                z = np.linspace(0, 10, 50)
                theta = np.linspace(0, 2*np.pi, 50)
                x = np.cos(theta)
                y = np.sin(theta)
                
                fig_3d = go.Figure()
                # Badan (Cylinder Sim)
                fig_3d.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='gray', width=2), name="Body Frame"))
                # Kawasan Cedera (Hotspots)
                fig_3d.add_trace(go.Scatter3d(x=[0], y=[0.5], z=[7], mode='markers', 
                                              marker=dict(size=20, color='red', opacity=0.8), name="Thoracic Injury"))
                fig_3d.add_trace(go.Scatter3d(x=[0.2], y=[0], z=[4], mode='markers', 
                                              marker=dict(size=15, color='orange', opacity=0.8), name="Liver Laceration"))
                
                fig_3d.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'), 
                                     margin=dict(r=0, l=0, b=0, t=0), height=500)
                st.plotly_chart(fig_3d, use_container_width=True)

            with col_diag:
                st.subheader("📑 AI Diagnostics")
                st.metric("Body Damage Index", "34%", delta="Critical")
                st.metric("Survival Probability", "78.4%")
                st.success("**AI Recommendation:** Proceed with Robotic-Assisted Median Sternotomy.")
                if st.button("🔄 Reset Scan"):
                    st.session_state.scan_complete = False
                    st.rerun()

    with tab_op:
        st.subheader("Live Surgical Stress Monitoring")
        if not st.session_state.sim_running:
            if st.button("🔴 START DYNAMIC SURGERY"):
                st.session_state.sim_running = True
                st.rerun()
        else:
            if st.button("⏹️ STOP SURGERY"):
                st.session_state.sim_running = False
                st.rerun()

            # Placeholders untuk real-time update
            v_met = st.empty()
            v_log = st.empty()
            
            # Simulation Loop (Dynamic Stress Test)
            for i in range(1, 11):
                time.sleep(1.5)
                hr = 85 + (i * 5) if i < 8 else 100 - i
                o2 = 98 - (i * 2) if i < 8 else 85 + i
                
                msg = "Performing internal repair..."
                if i == 5: msg = "⚠️ ALERT: Oxygen saturation dropping!"
                if i == 8: msg = "🚨 CRISIS: Sudden Hemorrhage detected!"
                
                with v_met.container():
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Heart Rate", f"{hr} BPM")
                    m2.metric("SpO2", f"{o2}%")
                    m3.metric("AI Precision", "99.2%")
                    st.warning(f"**Current Action:** {msg}")
                
                v_log.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
            
            st.success("🏁 Surgery successful. AI Robot closing incision.")

# ---------------------------------------------------------
# PAGE 3: TEAM PROFILES (RETAINED)
# ---------------------------------------------------------
elif menu == "3. Medical Team Profiles":
    st.title("👨‍⚕️ Assigned Surgical Experts")
    st.info("👨‍⚕️ **Lead Surgeon:** Dr. Adam Syarif (FRCS London)\n\n👩‍⚕️ **Anesthesiologist:** Dr. Siti Hajar (Critical Care Specialist)")

# ---------------------------------------------------------
# PAGE 4: AI LOYALTY (RETAINED)
# ---------------------------------------------------------
elif menu == "4. AI Loyalty Predictor":
    st.title("🤖 AI Loyalty Prediction")
    score = st.slider("ESCA Domain Alignment Score (%)", 0, 100, 88)
    st.metric("Advocacy Probability", f"{score * 0.9}%")

# ---------------------------------------------------------
# PAGE 5: FINANCIAL (RETAINED)
# ---------------------------------------------------------
else:
    st.title("💰 Ethical Billing & Transparency")
    st.table(pd.DataFrame({"Item": ["AI Robotic Fee", "Surgery", "Audit"], "Cost (RM)": [5000, 15000, 0]}))

st.sidebar.divider()
st.sidebar.write(f"© 2025 Mohd Khairul Ridhuan Bin Mohd Fadzil")
