import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="Aura Fitness", layout="wide")

# 2. Setup (We will add the 'Registration' logic next)
st.title("🏃‍♂️ Aura Fitness")

# 3. Sidebar Navigation
menu = ["Home", "My Performance", "Buddy Group", "AI Coach"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Home":
    st.subheader("Welcome to Aura Performance")
    st.write("Join the elite. Track metrics. Share progress.")

elif choice == "Buddy Group":
    st.header("🤝 Buddy Community")
    tab1, tab2 = st.tabs(["Join/Create Group", "Group Feed"])
    
    with tab1:
        st.write("Connect with your training partners.")
        group_id = st.text_input("Enter Buddy Group Code (e.g., AURA-X)")
        if st.button("Link Account"):
            st.success(f"Linked to group: {group_id}")
            
    with tab2:
        st.subheader("Live Progress Feed")
        # Example of shared data
        buddy_data = pd.DataFrame({
            "Athlete": ["You", "Buddy_Alpha", "Buddy_Beta"],
            "Weekly Points": [450, 320, 510]
        })
        st.bar_chart(buddy_data.set_index("Athlete"))

# 4. Login Gate (To be added once the database is connected)
