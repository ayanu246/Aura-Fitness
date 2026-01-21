import streamlit as st
from supabase import create_client
import pandas as pd
import random

# Connection
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Health Pro", page_icon="❤️")

# --- LOGIN GATE ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Aura Login")
    user_input = st.text_input("Enter your Username to Sign In:")
    if st.button("Sign In"):
        if user_input:
            st.session_state.user_name = user_input
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Please enter a name.")
    st.stop() # Stops the rest of the app from running until logged in

# --- APP START (Only runs after login) ---

# Sidebar
with st.sidebar:
    st.title(f"Hi, {st.session_state.user_name}!")
    if st.button("Sign Out"):
        st.session_state.logged_in = False
        st.rerun()
    
    st.divider()
    menu = st.radio("Menu", ["Summary", "Manage Groups", "Trends"])

# --- TAB 1: SUMMARY (Saves to Database) ---
if menu == "Summary":
    st.title("Today's Stats")
    
    # Try to load existing data so it's not empty when you open it
    existing = supabase.table("aura_collab_tracker").select("*").eq("username", st.session_state.user_name).execute()
    
    # Apple Health Cards
    col1, col2 = st.columns(2)
    with col1:
        steps = st.number_input("Steps", min_value=0, step=100)
        water = st.number_input("Water", min_value=0)
    with col2:
        sleep = st.number_input("Sleep", min_value=0.0)
        exercise = st.number_input("Exercise", min_value
