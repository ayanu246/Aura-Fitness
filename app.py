import streamlit as st
from supabase import create_client
import pandas as pd
import random

# Connection
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Health Pro", page_icon="❤️", layout="centered")

# --- PERSISTENT LOGIN SYSTEM ---
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'my_groups' not in st.session_state:
    st.session_state.my_groups = ["Solo"]

# --- SIDEBAR (Login & Group Switcher) ---
with st.sidebar:
    st.title("👤 My Profile")
    st.session_state.user_name = st.text_input("Login Name", value=st.session_state.user_name)
    
    if st.session_state.user_name:
        st.success(f"Logged in as {st.session_state.user_name}")
    
    st.divider()
    st.title("📂 My Groups")
    active_group = st.selectbox("Current Active Group", st.session_state.my_groups)
    
    st.divider()
    menu = st.radio("Navigation", ["Summary", "Manage Groups", "Trends & Leaderboards"])

# --- TAB 1: SUMMARY (The "Apple Health" Dashboard) ---
if menu == "Summary":
    st.title("Summary")
    st.caption("Tip: Add this page to your iPhone/Android Home Screen to keep tracking active.")
    
    # Apple Health Style Cards
    with st.container():
        st.markdown("### 🏃 Activity")
        steps = st.number_input("Steps Walked Today", min_value=0, step=500)
        exercise = st.number_input("Exercise Minutes", min_value=0)
        
        st.markdown("### 💤 Health")
        sleep = st.number_input("Sleep (Hours)", min_value=0.0, step=0.5)
        water = st.number_input("Water (Glasses)", min_value=0)

    if st.button("Sync Data to Cloud"):
        if st.session_state.user_name:
            data = {
                "username": st.session_state.user_name,
                "group_name": active_group,
                "steps": steps, "sleep_hours": sleep,
                "water": water, "exercise_mins": exercise
            }
            supabase.table("aura_collab_tracker").upsert(data).execute()
            st.success(f"Saved to {active_group}!")
        else:
            st.warning("Please enter a name in the sidebar to save.")

# --- TAB 2: MANAGE GROUPS (Multiple Groups) ---
elif menu == "Manage Groups":
    st.title("Manage Groups")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Join a New Group")
        join_code = st.text_input("Enter Code")
        if st.button("Join"):
            if join_code not in st.session_state.my_groups:
                st.session_state.my_groups.append(join_code)
                st.success(f"Added {join_code} to your list!")

    with col2:
        st.subheader("Create a Group")
        new_name = st.text_input("New Group Name")
        if st.button("Generate"):
            code = f"{new_name[:3].upper()}-{random.randint(1000, 9999)}"
            st.session_state.my_groups.append(code)
            st.write("Share this code:")
            st.code(code)

# --- TAB 3: TRENDS (The Selector) ---
elif menu == "Trends & Leaderboards":
    st.title("Trends")
    
    # This is the "Choose what group you want to view" part
    view_choice = st.selectbox("Choose group to view standings:", st.session_state.my_groups)
    
    st.subheader(f"Rankings for {view_choice}")
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", view_choice).execute()
    
    if res.data:
        df = pd.DataFrame(res.data)
        # Custom display
        st.table(df[["username", "steps", "exercise_mins", "water"]].sort_values(by="steps", ascending=False))
    else:
        st.info("No data found for this group yet.")
        
