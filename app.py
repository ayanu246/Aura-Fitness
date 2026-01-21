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
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.logged_in:
    st.title("❤️ Aura Health Sign-In")
    user_input = st.text_input("Enter your Username:")
    if st.button("Sign In"):
        if user_input:
            st.session_state.user_name = user_input
            st.session_state.logged_in = True
            st.rerun()
    st.stop()

# --- APP AFTER LOGIN ---
with st.sidebar:
    st.title(f"Welcome, {st.session_state.user_name}")
    menu = st.radio("Go to:", ["Summary", "Manage Groups", "Trends"])
    if st.button("Sign Out"):
        st.session_state.logged_in = False
        st.rerun()

# --- TAB 1: SUMMARY ---
if menu == "Summary":
    st.header("Daily Activity")
    col1, col2 = st.columns(2)
    with col1:
        steps = st.number_input("Steps Today", min_value=0, step=100)
        water = st.number_input("Water (Glasses)", min_value=0)
    with col2:
        sleep = st.number_input("Sleep (Hours)", min_value=0.0, step=0.5)
        exercise = st.number_input("Exercise (Minutes)", min_value=0)

    # Group to save to
    active_g = st.text_input("Current Group (Default: Solo)", value="Solo")

    if st.button("Sync to Cloud"):
        data = {
            "username": st.session_state.user_name,
            "group_name": active_g,
            "steps": steps, 
            "sleep_hours": sleep,
            "water": water, 
            "exercise_mins": exercise
        }
        # This saves to Supabase so it stays there forever
        supabase.table("aura_collab_tracker").upsert(data, on_conflict="username,group_name").execute()
        st.success(f"Successfully saved to {active_g}!")

# --- TAB 2: MANAGE GROUPS ---
elif menu == "Manage Groups":
    st.header("Group Management")
    st.write("Create a group to get a unique invite code.")
    new_g_name = st.text_input("New Group Name:")
    if st.button("Create Group"):
        code = f"{new_g_name.upper()}-{random.randint(1000, 9999)}"
        st.success(f"Group Created!")
        st.write("Share this code with your friends:")
        st.code(code)

# --- TAB 3: TRENDS ---
elif menu == "Trends":
    st.header("Community Trends")
    # THE SELECTOR: View any group you want
    view_g = st.text_input("Which group leaderboard do you want to see?", value="Solo")
    
    res = supabase.table("aura_collab_tracker").select("*").eq
