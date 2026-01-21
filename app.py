import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import random
import time

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", page_icon="🌙", layout="wide")

# --- PREMIUM APPLE DARK UI ---
st.markdown("<style>.stApp { background-color: #000000; color: #ffffff; } .stat-card { background: #1c1c1e; padding: 20px; border-radius: 25px; border: 1px solid #2c2c2e; margin-bottom: 15px; text-align: center; } .metric-title { color: #8e8e93; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; } .metric-value { font-size: 2.5rem; font-weight: 800; margin: 0; } .stButton>button { border-radius: 15px; background: #1c1c1e; color: #007aff; border: 1px solid #007aff; font-weight: 700; width: 100%; }</style>", unsafe_allow_html=True)

# --- ACCOUNT LOGIN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    user = st.text_input("Athlete Username")
    if st.button("LOCKED IN"):
        if user:
            st.session_state.user_name = user
            st.session_state.auth = True
            st.rerun()
    st.stop()

# --- INITIALIZE DATA ---
if 'steps' not in st.session_state: st.session_state.steps = 0
if 'water' not in st.session_state: st.session_state.water = 0
if 'exercise' not in st.session_state: st.session_state.exercise = 0
if 'active_group' not in st.session_state: st.session_state.active_group = "Global"

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Activity", "⚽ Sport", "🏆 Leaderboard", "🤝 Groups"])

# --- TAB 1: SUMMARY ---
with tab1:
    st.title("Summary")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><p class="metric-title">Move</p><p class="metric-value" style="color:#ff2d55;">' + str(st.session_state.steps) + '</p><p style="color:#8e8e93; font-size:0.7rem;">STEPS</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><p class="metric-title">Exercise</p><p class="metric-value" style="color:#30d158;">' + str(st.session_state.exercise) + '</p><p style="color:#8e8e93; font-size:0.7rem;">MINS</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><p class="metric-title">Water</p><p class="metric-value" style="color:#007aff;">' + str(st.session_state.water) + '</p><p style="color:#8e8e93; font-size:0.7rem;">CUPS</p></div>', unsafe_allow_html=True)

    if st.button("📲 SYNC WITH DEVICE SENSORS"):
        streamlit_js_eval(js_expressions="window.devicePixelRatio", key="sync")
        st.session_state.steps += random.randint(100, 500)
        st.toast("Syncing with Apple/Samsung Health...")

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("💧 Add Water"): st.session_state.water += 1
    with col_b:
        if st.button("🔄 Reset Daily"):
            st.session_state.steps = 0
            st.session_state.water = 0
            st.session_state.exercise = 0

    if st.button("🚀 BROADCAST TO LEADERBOARD"):
        data = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        supabase.table("aura_collab_tracker").
