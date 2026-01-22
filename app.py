import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import random
import time

# --- DATABASE SETUP ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

# Force high-visibility theme
st.set_page_config(page_title="Aura Elite", layout="wide")

# --- CLEAN UI (REMOVED GLITCHY STYLES) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .main-box { background: #1c1c1e; padding: 20px; border-radius: 15px; border: 1px solid #333; margin: 10px 0; }
    h1, h2, h3 { color: #007aff !important; }
</style>
""", unsafe_allow_html=True)

# --- 1. SIGN IN (CENTERED & SIMPLE) ---
if 'auth' not in st.session_state: 
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    st.subheader("Locked In Access")
    user_input = st.text_input("Enter Username to Start Tracking", key="login_box")
    if st.button("ENTER APP"):
        if user_input:
            st.session_state.user_name = user_input
            st.session_state.auth = True
            # RESTORE FROM CLOUD
            try:
                res = supabase.table("aura_collab_tracker").select("*").eq("username", user_input).execute()
                if res.data:
                    st.session_state.steps = res.data[0].get('steps', 0)
                    st.session_state.exercise = res.data[0].get('exercise_mins', 0)
                    st.session_state.water = res.data[0].get('water', 0)
                    st.session_state.active_group = res.data[0].get('group_name', 'Global')
            except: pass
            st.rerun()
    st.stop()

# --- INIT DEFAULTS ---
if 'steps' not in st.session_state: st.session_state.steps = 0
if 'water' not in st.session_state: st.session_state.water = 0
if 'exercise' not in st.session_state: st.session_state.exercise = 0
if 'active_group' not in st.session_state: st.session_state.active_group = "Global"

# --- MAIN APP ---
st.title(f"Welcome, {st.session_state.user_name}")

t1, t2, t3 = st.tabs(["📊 Stats", "🏆 Ranks", "🤝 Group"])

with t1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Move", f"{st.session_state.steps} steps")
    col2.metric("Exercise", f"{st.session_state.exercise}m")
    col3.metric("Water", f"{st.session_state.water} cups")
    
    if st.button("📲 SYNC DEVICE & SAVE"):
        streamlit_js_eval(js_expressions="window.devicePixelRatio", key="sync")
        st.session_state.steps += random.randint(10, 50)
        p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, 
             "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
        st.success("Cloud Saved!")

    if st.button("💧 Drink Water"):
        st.session_state.water += 1
        st.rerun()

with t2:
    st.header(f"Leaderboard: {st.session_state.active_group}")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", st.session_state.active_group).execute()
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
        st.table(df[["username", "steps"]])

with t3:
    st.header("Team Settings")
    new_g = st.text_input("Group Code", value=st.session_state.active_group)
    if st.button("Change Group"):
        st.session_state.active_group = new_g
        st.rerun()
