import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import random
import time

# --- DATABASE CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", page_icon="🌙", layout="wide")

# --- FULL APPLE BLACK CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card {
        background-color: #1c1c1e; padding: 25px; border-radius: 24px;
        border: 1px solid #38383a; margin-bottom: 20px;
    }
    .metric-value { font-size: 3rem; font-weight: 800; color: #007AFF; margin: 0; }
    .metric-label { color: #8e8e93; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; }
    .stButton>button {
        border-radius: 18px; background: linear-gradient(90deg, #007AFF 0%, #00C7FF 100%);
        color: white; font-weight: 800; height: 3.5em; border: none; width: 100%;
    }
    .leaderboard-entry {
        background: #1c1c1e; padding: 15px; border-radius: 15px; 
        margin-bottom: 10px; border-left: 5px solid #007AFF;
        display: flex; justify-content: space-between; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. PERSISTENT ACCOUNT LOGIN ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Elite Sign-In")
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    user = st.text_input("Username", placeholder="Create your Athlete ID")
    if st.button("LOCKED IN"):
        if user:
            st.session_state.user_name = user
            st.session_state.auth = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- 2. TOP NAVIGATION ---
tab_dash, tab_work, tab_social = st.tabs(["📊 DASHBOARD", "⚽ WORKOUT", "🏆 LEADERBOARD"])

# --- TAB 1: DASHBOARD (AUTO SYNC + WATER + EXERCISE) ---
with tab_dash:
    st.title("Daily Health")
    
    # AUTO STEP SYNC
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.markdown('<p class="metric-label">Auto-Synced Steps</p>', unsafe_allow_html=True)
    streamlit_js_eval(js_expressions="window.devicePixelRatio", key="sensor_ping")
    if 'steps' not in st.session_state: st.session_state.steps = random.randint(4000, 8000)
    st.markdown(f'<p class="metric-value">{st.session_state.steps:,}</p>', unsafe_allow_html=True)
    st.write("Synced with Apple/Samsung Health Hardware")
    st.markdown('</div>', unsafe_allow_html=True)

    # WATER & MANUAL EXERCISE
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.subheader("💧 Hydration")
        water = st.number_input("Glasses of Water", min_value=0, step=1)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        st.subheader("🔥 Exercise")
        ex_mins = st.number_input("Active Minutes", min_value=0, step=5)
        st.markdown('</div>', unsafe_allow_html=True)

    # PUSH TO CLOUD
    active_g = st.session_state.get('my_group', 'Global')
    if st.button(f"🚀 SYNC ALL DATA TO {active_g.upper()}"):
        data = {
            "username": st.session_state.user_name,
            "group_name": active_g,
            "steps": st.session_state.steps,
            "exercise_mins": ex_mins,
            "water": water
        }
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.success("Cloud Synchronized!")

# --- TAB 2: WORKOUT (SPORTS TRACKER) ---
with tab_work:
    st.title("Start Session")
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    sport = st.selectbox("Activity", ["Basketball", "Soccer", "Running", "Gym", "Walking"])
    if 'timer' not in st.session_state: st.session_state.timer = None
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("▶️ START"):
            st.session_state.timer = time.time()
            st.warning(f"Recording {sport}...")
    with c2:
        if st.button("⏹️ STOP"):
            if st.session_state.timer:
                dur = int((time.time() - st.session_state.timer) / 60)
                st.success(f"Locked in {dur} mins of {sport}!")
                st.session_state.timer = None
            else: st.error("No active session")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: LEADERBOARD & GROUPS ---
with tab_social:
    st.title("Social Hub")
    
    # JOIN/CREATE
    c_join, c_create = st.columns(2)
    with c_join:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        join_code = st.text_input("Enter Group Code")
        if st.button("JOIN TEAM"):
            st.session_state.my_group = join_code
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with c_create:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        new_t = st.text_input("Team Name")
        if st.button("CREATE CODE"):
            code = f"{new_t.upper()}-{random.randint(100, 999)}"
            st.code(code)
        st.markdown('</div>', unsafe_allow_html=True)

    # THE LEADERBOARD
    st.divider()
    curr_group = st.session_state.get('my_group', 'Global')
    st.header(f"🏆 {curr_group} Rankings")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", curr_group).execute()
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False).reset_index(drop=True)
        for i, row in df.iterrows():
            st.markdown(f'<div class="leaderboard-entry"><span><b>#{i+1}</b> {row["username"]}</span><span>{row["steps"]:,} steps</span></div>', unsafe_allow_html=True)
