import streamlit as st
from supabase import create_client
import pandas as pd

# Connection
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Hub", layout="wide")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Aura Navigation")
    name = st.text_input("Profile Name", placeholder="Your name...")
    
    # The different "Tabs" you asked for
    menu = st.radio("Go to:", ["My Daily Tracker", "Groups & Social", "Leaderboard"])

# --- TAB 1: TRACKING ---
if menu == "My Daily Tracker":
    st.header(f"Welcome back, {name if name else 'Athlete'}!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏃 Activity")
        # Step tracking note
        st.caption("Tip: Check your phone's Health app and enter the total below.")
        steps = st.number_input("Steps Today", min_value=0, step=100)
        exercise = st.number_input("Workout Minutes", min_value=0)
        
    with col2:
        st.subheader("💤 Recovery & Health")
        sleep = st.number_input("Sleep (Hours)", min_value=0.0, max_value=24.0, step=0.5)
        water = st.number_input("Water (Glasses/Liters)", min_value=0.0)

    group_to_save = st.text_input("Group Code (Leave 'Solo' if tracking alone)", value="Solo")

    if st.button("Log Everything"):
        if name:
            data = {
                "username": name, 
                "group_name": group_to_save, 
                "steps": steps, 
                "sleep_hours": sleep,
                "water": water,
                "exercise_mins": exercise
            }
            supabase.table("aura_collab_tracker").upsert(data).execute()
            st.success("All stats synced!")
        else:
            st.error("Please enter your name in the sidebar first!")

# --- TAB 2: GROUPS & SOCIAL ---
elif menu == "Groups & Social":
    st.header("👥 Group Hub")
    choice = st.selectbox("What do you want to do?", ["Join/Create a Group", "Invite Friends"])
    
    if choice == "Join/Create a Group":
        new_group = st.text_input("Enter a Group Name to Create or Join:")
        if new_group:
            st.success(f"You are now part of: {new_group}")
            st.info(f"Go to 'Leaderboard' to see {new_group} stats.")
            
    elif choice == "Invite Friends":
        invite_code = st.text_input("Group Name to Share:")
        if invite_code:
            msg = f"Join my Aura Hub group! Code: {invite_code}"
            st.code(msg)
            st.write(f"[Share via WhatsApp](https://wa.me/?text={msg})")

# --- TAB 3: LEADERBOARD ---
elif menu == "Leaderboard":
    st.header("🏆 Competition Board")
    view_group = st.text_input("Enter Group Name to view others:")
    
    if view_group:
        res = supabase.table("aura_
