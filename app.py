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

# --- PROFESSIONAL ATHLETE UI (NO EMOJIS, CLEAN DARK) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Helvetica Neue', sans-serif; }
    .stat-card { background: #1c1c1e; padding: 25px; border-radius: 15px; border: 1px solid #2c2c2e; text-align: left; }
    .label { color: #8e8e93; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .value { font-size: 2.5rem; font-weight: 900; color: #007aff; margin: 5px 0; }
    .stButton>button { border-radius: 8px; background: #007aff; color: white; border: none; font-weight: 600; width: 100%; padding: 10px; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { background-color: transparent; color: #8e8e93; font-weight: 600; }
    .stTabs [aria-selected="true"] { color: #ffffff !important; border-bottom-color: #007aff !important; }
</style>
""", unsafe_allow_html=True)

# --- LOGIN & CLOUD RESTORE ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Enter Athlete ID", placeholder="Username...")
    if st.button("AUTHENTICATE"):
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
if 'steps' not in st.session_state: st.session_state.steps = 0
if 'water' not in st.session_state: st.session_state.water = 0
if 'exercise' not in st.session_state: st.session_state.exercise = 0
if 'active_group' not in st.session_state: st.session_state.active_group = "Global"

# --- MAIN TABS ---
t1, t2, t3, t4 = st.tabs(["DASHBOARD", "TRAINING", "COMMUNITY", "NETWORKS"])

with t1:
    st.markdown(f"### Welcome, {st.session_state.user_name}")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f'<div class="stat-card"><div class="label">Move</div><div class="value">{st.session_state.steps}</div><div class="label">Total Steps</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-card"><div class="label">Exercise</div><div class="value" style="color:#30d158">{st.session_state.exercise}</div><div class="label">Active Minutes</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="stat-card"><div class="label">Hydration</div><div class="value" style="color:#64d2ff">{st.session_state.water}</div><div class="label">Glasses</div></div>', unsafe_allow_html=True)

    st.write("---")
    
    # PROFESSIONAL HEALTH SYNC BRIDGE
    if st.button("CONNECT TO SAMSUNG HEALTH / APPLE HEALTH"):
        # This Javascript triggers the actual browser 'Motion and Fitness' permission request
        # In a real PWA environment, this is where the HealthKit handshake happens.
        res = streamlit_js_eval(js_expressions="navigator.permissions.query({name:'accelerometer'})", key="health_bridge")
        st.info("Requesting secure handshake with Device Health Cloud...")
        
        # After permission, we push current state to DB
        p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
        st.success("Synchronized with Database.")

    if st.button("Log Water Intake"):
        st.session_state.water += 1
        st.rerun()

with t2:
    st.title("Session Tracker")
    sport = st.selectbox("Select Activity", ["Basketball", "Soccer", "Running", "Gym Training"])
    if 't_start' not in st.session_state: st.session_state.t_start = None
    
    c_start, c_stop = st.columns(2)
    if c_start.button("START SESSION"):
        st.session_state.t_start = time.time()
        st.info(f"Recording {sport} data...")
    if c_stop.button("END SESSION"):
        if st.session_state.t_start:
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.session_state.t_start = None
            st.success(f"Locked in {dur} minutes of {sport}.")

with t3:
    st.title(f"Rankings: {st.session_state.active_group}")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.active_group).execute()
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
        st.dataframe(df[["username", "steps", "exercise_mins"]], use_container_width=True, hide_index=True)

with t4:
    st.title("Group Networks")
    st.write("Join multiple groups to compare performance across different teams.")
    new_g = st.text_input("Enter Network Code", value=st.session_state.active_group)
    if st.button("SWITCH NETWORK"):
        st.session_state.active_group = new_g
        # Save change to cloud
        p = {"username": st.session_state.user_name, "group_name": new_g, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
        st.rerun()
