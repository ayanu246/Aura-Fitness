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

st.set_page_config(page_title="Aura Elite", page_icon="🌙", layout="wide")

# --- UI STYLING ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card { background: #1c1c1e; padding: 20px; border-radius: 20px; border: 1px solid #2c2c2e; margin-bottom: 10px; text-align: center; }
    .metric-title { color: #8e8e93; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }
    .metric-value { font-size: 2.2rem; font-weight: 800; margin: 0; }
    .stButton>button { border-radius: 12px; background: #1c1c1e; color: #007aff; border: 1px solid #007aff; font-weight: 700; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 1. SIGN IN & AUTO-RESTORE ---
if 'auth' not in st.session_state: 
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🌙 Aura Elite")
    user_input = st.text_input("Username")
    if st.button("LOCKED IN"):
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
            except:
                pass
