import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import time

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", layout="wide")

# --- PRO UI ---
st.markdown("<style>.stApp { background-color: #000000; color: #ffffff; } .stat-card { background: #1c1c1e; padding: 15px; border-radius: 20px; border: 1px solid #2c2c2e; margin-bottom: 10px; text-align: center; } .metric-val { font-size: 1.8rem; font-weight: 800; color: #007aff; } .stButton>button { border-radius: 12px; background: #1c1c1e; color: #007aff; border: 1px solid #007aff; font-weight: 700; width: 100%; }</style>", unsafe_allow_html=True)

# --- 1. LOGIN & RESTORE ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    u_in = st.text_input("Athlete Username")
    if st.button("LOCKED IN"):
        if u_in:
            st.session_state.user_name = u_in
            st.session_state.auth = True
            try:
                r = supabase.table("aura_collab_tracker").select("*").eq("username", u_in).execute()
                if r.data:
                    st.session_state.steps = r.data[0].get('steps', 0)
                    st.session_state.exercise = r.data[0].get('exercise_mins', 0)
                    st.session_state.water = r.data[0].get('water', 0)
                    st.session_state.active_group = r.data[0].get('group_name', 'Global')
            except: pass
            st.rerun()
    st.stop()

# --- INIT DEFAULTS ---
for k, v in {"steps": 0, "water": 0, "exercise": 0, "active_group": "Global"}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- NAVIGATION ---
t1, t2, t3, t4 = st.tabs(["📊 Activity", "⚽ Sport", "🏆 Leaderboard", "🤝 Groups"])

with t1:
    st.header(f"Athlete: {st.session_state.user_name}")
    c1, c2, c3 = st
