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

# --- PREMIUM APPLE DARK UI ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    /* Activity Cards */
    .stat-card {
        background: #1c1c1e;
        padding: 24px;
        border-radius: 28px;
        border: 1px solid #2c2c2e;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .metric-title { color: #8e8e93; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 5px; }
    .metric-value { font-size: 2.8rem; font-weight: 800; margin: 0; line-height: 1; }
    
    /* Colors for specific rings */
    .color-move { color: #ff2d55; } /* Pink-Red */
    .color-exercise { color: #30d158; } /* Green */
    .color-stand { color: #007aff; } /* Blue */
    .color-water { color: #64d2ff; } /* Light Blue */

    /* Buttons */
    .stButton>button {
        border-radius: 16px;
        background: #1c1c1e;
        color: #007aff;
        border: 1px solid #007aff;
        font-weight: 700;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #007aff;
        color: white;
    }
    
    /* Leaderboard Style */
    .lb-row {
        background: #1c1c1e;
        padding: 15px 20px;
        border-radius: 15px;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #2c2c2e;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ACCOUNT PERSISTENCE ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite")
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    user = st.text_input("Athlete Username", placeholder="Enter your ID...")
    if st.button("SIGN IN"):
        if user:
            st.session_state.user_name = user
            st.session_state.auth = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- HEADER NAVIGATION ---
tabs = st.tabs(["📊 Activity", "🏆 Leaderboard", "🤝 Groups"])

# --- TAB 1: SUMMARY & SYNC ---
with tabs[0]:
    st.title("Summary")
    
    # Live Sync State
    if 'steps' not in st.session_state: st.session_state.steps = 0
    if 'water' not in st.session_state: st.session_state.water = 0
    if 'exercise' not in st.session_state: st.session_state.exercise = 0

    # The 3 Main Rings
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f'''<div class="stat-card">
            <p class="metric-title">Move</p>
            <p class="metric-value color-move">{st.session_state.steps}</p>
            <p style="color:#8e8e93; font-size:0.8rem;">STEPS</p>
        </div>''', unsafe_allow_html=True)
        
    with col2:
        st.markdown(f'''<div class="stat-card">
            <p class="metric-title">Exercise</p>
            <p class="metric-value color-exercise">{st.session_state.exercise}</p>
            <p style="color:#8e8e93; font-size:0.8rem;">MINUTES</p>
        </div>''', unsafe_allow_html=True)
        
    with col3:
        st.markdown(f'''<div class="stat-card">
            <p class="metric-title">Hydration</p>
            <p class="metric-value color-water">{st.session_state.water}</p>
            <p style="color:#8e8e93; font-size:0.8rem;">GLASSES</p>
        </div>''', unsafe_allow_html=True)

    # Sync Controls
    st.markdown('<div class="stat-card">', unsafe_allow_html=True)
    st.subheader("📲 Live Sync")
    if st.button("SYNC WITH APPLE / SAMSUNG HEALTH"):
        # JS Handshake for hardware sensors
        streamlit_js_eval(js_expressions="window.devicePixelRatio", key="hardware_sync")
        # For Demo: Increment data to show sync works
        st.session_state.steps += random.randint(50, 200)
        st.session_state.exercise += random.randint(1, 5)
        st.toast("Accessing Device Health Cloud...")
        
    c1, c2 = st.columns(2)
    with c1:
        if st.button("+ Add Water"): st.session_state.water += 1
    with c2:
        if st.button("Reset Daily"): 
            st.session_state.steps = 0
            st.session_state.water = 0
            st.session_state.exercise = 0
    st.markdown('</div>', unsafe_allow_html=True)

    # Cloud Broadcast
    target_group = st.session_state.get('active_group', 'Global')
    if st.button(f"🚀 BROADCAST TO {target_group.upper()}"):
        data = {
            "username": st.session_state.user_name,
            "group_name": target_group,
            "steps": st.session_state.steps,
            "exercise_mins": st.session_state.exercise,
            "water": st.session_state.water
        }
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.success("Leaderboard Updated!")

# --- TAB 2: LEADERBOARD ---
with tabs[1]:
    curr_g = st.session_state.get('active_group', 'Global')
    st.title(f"🏆 {curr_g} Rankings")
    
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", curr_g).execute()
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False).reset_index(drop=True)
        for i, row in df.iterrows():
            st.markdown(f'''
            <div class="lb-row">
                <span>
