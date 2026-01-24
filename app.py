import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import time

# --- 1. DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Aura Elite", layout="wide")

# --- 3. PRO UI STYLING ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Helvetica Neue', sans-serif; }
    .stat-card { background: #1c1c1e; padding: 25px; border-radius: 15px; border: 1px solid #2c2c2e; text-align: left; }
    .label { color: #8e8e93; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .value { font-size: 2.5rem; font-weight: 900; color: #007aff; margin: 5px 0; }
    .stButton>button { border-radius: 8px; background: #007aff; color: white; border: none; font-weight: 600; width: 100%; padding: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 4. AUTHENTICATION ---
if 'auth' not in st.session_state: 
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Athlete ID", placeholder="Enter username...")
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
                else:
                    st.session_state.steps, st.session_state.exercise, st.session_state.water = 0, 0, 0
                    st.session_state.active_group = "Global"
            except:
                st.session_state.steps, st.session_state.exercise, st.session_state.water
