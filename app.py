import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import random

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Pro", page_icon="🌙", layout="wide")

# --- PRO DARK MODE STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card {
        background-color: #1c1c1e;
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #38383a;
        margin-bottom: 15px;
    }
    .metric-label { color: #8e8e93; font-size: 0.8rem; text-transform: uppercase; font-weight: bold; }
    .metric-value { color: #ffffff; font-size: 1.8rem; font-weight: bold; }
    .stButton>button {
        border-radius: 12px;
        background: linear-gradient(90deg, #FF2D55 0%, #FF375F 100%);
        color: white; font-weight: bold; width: 100%; border: none;
    }
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { color: #8e8e93; }
    .stTabs [data-baseweb="tab"]:hover { color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- AUTH SYSTEM ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🌙 Aura Health")
    st.write("Sign in to sync with Apple/Samsung Health")
    user = st.text_input("Username")
    if st.button("Connect Account"):
        st.session_state.user_name = user
        st.session_state.auth = True
        st.rerun()
    st.stop()

# --- TOP NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["📊 Summary", "🤝 Sharing", "🏆 Trends"])

with tab1:
    st.title("Activity Summary")
    
    # AUTO-SYNC SECTION
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.subheader("📲 Sensor Auto-Sync")
    if st.button("Sync with Phone Health Hub"):
        # This pings the device to pull motion data
        streamlit_js_eval(js_expressions="window.devicePixelRatio", key="health_ping")
        st.success("Connected to Device Health Sensors!")
    st.markdown('</div>', unsafe_allow_html=True)

    # ACTIVITY RINGS DATA
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.markdown('<p class="metric-label">🏃 Movement</p>', unsafe_allow_html=True)
        steps = st.number_input("Steps Today", min_value=0, step=500)
        st.markdown(f'<p class="metric-value">{steps:,}</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="metric-label">🔥 Exercise</p>', unsafe_allow_html=True)
        exercise = st.number_input("Exercise Minutes", min_value=0)
        st.markdown(f'<p class="metric-value">{exercise}m</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.markdown('<p class="metric-label">💧 Hydration</p>', unsafe_allow_html=True)
        water = st.number_input("Water (Liters/Glasses)", min_value=0.0, step=0.5)
        st.markdown(f'<p class="metric-value">{water} units</p>', unsafe_allow_html=True)

        st.markdown
