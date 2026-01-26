import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Universal Chef", page_icon="🌎", layout="centered")

# --- UI STYLE ---
st.markdown("""
<style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    .recipe-card { 
        background: #161b22; 
        padding: 25px; 
        border-radius: 20px; 
        border: 1px solid #30363d;
        margin-top: 20px;
    }
    .badge { padding: 5px 15px; border-radius: 50px; font-size: 0.8rem; font-weight: bold; }
    .halal { background: #065f46; color: #34d399; }
    .global { background: #1f6feb; color: #f0f6fc; }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #238636, #2ea043);
        color: white;
        font-weight: bold;
        border: none;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🌎 Universal Chef")
st.markdown("### *Global Recipes for Every Kitchen*")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Dietary Settings")
    mode = st.radio("Mode", ["Global Mode", "Halal Only Mode"])
    diet = st.radio("Preference", ["Meat & Veg", "Vegetarian Only"])

# --- RECIPE OF THE DAY ---
st.subheader("🌟 Today's Special")
if mode == "Halal Only Mode":
    daily_name = "Halal Smash Burgers & Loaded Fries"
    badge = '<span class="badge halal">🌙 HALAL MODE ACTIVE</span>'
else:
    daily_name = "Classic American Burgers & Fries"
    badge = '<span class="badge global">🌎 GLOBAL MODE ACTIVE</span>'

st.markdown(f"""
<div class="recipe-card">
    {badge}
    <h2 style="margin-top:10px;">{daily_name}</h2>
    <p>Double patties, melted cheese, and hand-cut fries.</p>
</div>
""", unsafe_allow_html=True)

# --- INGREDIENT INPUT ---
st.markdown("---")
st.subheader("👨‍🍳 What's in your pantry?")
items = st.text_area("List everything you have:", placeholder="Chicken, potatoes, flour, spices...", height=150)

if st.button("🚀 CREATE RECIPE"):
    if not items:
        st.warning("Tell me what you have first!")
    else:
        with st.spinner("Cooking up something great..."):
            time.sleep(1.5)
            st.markdown(f"""
            <div class="recipe-card" style="border-top: 4px solid #238636;">
                <h4>Custom Comfort Meal</h4>
                <p>Based on: {items}</p>
                <hr style="border:0.1px solid #30363d">
                <strong>Step 1:</strong> Prep your protein and slice your potatoes.<br>
                <strong>Step 2:</strong> Season heavily and fry until golden.<br>
                <strong>Step 3:</strong> Serve hot and enjoy!
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
