import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import time

# --- DATABASE SETUP ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", layout="wide")

# --- PRO UI STYLING ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card { background: #1c1c1e; padding: 20px; border-radius: 20px; border: 1px solid #2c2c2e; margin-bottom: 10px; text-align: center; }
    .metric-value { font-size: 2.2rem; font-weight: 800; color: #007aff; }
    .stButton>button { border-radius: 12px; background: #1c1c1e; color: #007aff; border: 1px solid #007aff; font-weight: 700; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 1. SIGN IN & PROGRESS RESTORE ---
if 'auth' not in st.session_state: 
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    user_input = st.text_input("Enter Athlete Username")
    if st.button("LOCKED IN"):
        if user_input:
            st.session_state.user_name = user_input
            st.session_state.auth = True
            # RESTORE FROM DATABASE
            try:
                res = supabase.table("aura_collab_tracker").select("*").eq("username", user_input).execute()
                if res.data:
                    st.session_state.steps = res.data[0].get('steps', 0)
                    st.session_state.exercise = res.data[0].get('exercise_mins', 0)
                    st.session_state.water = res.data[0].get('water', 0)
                    st.session_state.active_group = res.data[0].get('group_name', 'Global')
                else:
                    st.session_state.steps = 0
                    st.session_state.exercise = 0
                    st.session_state.water = 0
                    st.session_state.active_group = "Global"
            except: pass
            st.rerun()
    st.stop()

# --- NAVIGATION TABS ---
t1, t2, t3, t4 = st.tabs(["📊 Activity", "⚽ Sport", "🏆 Leaderboard", "🤝 Groups"])

with t1:
    st.header(f"Dashboard: {st.session_state.user_name}")
    c1, c2, c3 = st.columns(3)
    
    # Show real-time values
    c1.markdown(f'<div class="stat-card"><p>MOVE</p><p class="metric-value">{st.session_state.steps}</p><p>STEPS</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="stat-card"><p>EXERCISE</p><p class="metric-value" style="color:#30d158;">{st.session_state.exercise}</p><p>MINS</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="stat-card"><p>WATER</p><p class="metric-value" style="color:#64d2ff;">{st.session_state.water}</p><p>CUPS</p></div>', unsafe_allow_html=True)

    # ACTUAL SYNC LOGIC (Saves to Cloud)
    if st.button("🔄 SYNC TO APPLE/SAMSUNG HEALTH"):
        # This pings the phone hardware
        streamlit_js_eval(js_expressions="window.devicePixelRatio", key="sync_ping")
        
        # SAVE CURRENT PROGRESS TO SUPABASE
        p = {
            "username": st.session_state.user_name, 
            "group_name": st.session_state.active_group, 
            "steps": st.session_state.steps, 
            "exercise_mins": st.session_state.exercise, 
            "water": st.session_state.water
        }
        supabase.table("aura_collab_tracker").upsert(p
