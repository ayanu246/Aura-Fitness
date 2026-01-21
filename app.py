import streamlit as st
from supabase import create_client
import pandas as pd
import random
import time

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", page_icon="⚡", layout="wide")

# --- PRO DARK UI ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stat-card {
        background-color: #1c1c1e; padding: 20px; border-radius: 20px;
        border: 1px solid #38383a; margin-bottom: 15px;
    }
    .stButton>button {
        border-radius: 12px; background: #007AFF; color: white; font-weight: bold; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ACCOUNT LOGIN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("⚡ Aura Elite")
    user = st.text_input("Username")
    if st.button("Enter Pro Hub"):
        st.session_state.user_name = user
        st.session_state.auth = True
        st.rerun()
    st.stop()

# --- APP TABS ---
tabs = st.tabs(["📊 Summary", "🏋️ Library", "⚽ Start Workout", "🏆 Trends"])

# --- TAB 1: SUMMARY ---
with tabs[0]:
    st.title("My Health Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        steps = st.number_input("Steps Today", min_value=0, step=100)
        ex_mins = st.number_input("Total Exercise (Min)", min_value=0)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        water = st.number_input("Water (Cups)", min_value=0.0)
        sleep = st.number_input("Sleep (Hours)", min_value=0.0)
        st.markdown('</div>', unsafe_allow_html=True)
    
    active_g = st.text_input("Active Group Name:", value="Solo")
    if st.button("Sync to Cloud"):
        data = {"username": st.session_state.user_name, "group_name": active_g, "steps": steps, "sleep_hours": sleep, "water": water, "exercise_mins": ex_mins}
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.success("Synced to Cloud!")

# ---
