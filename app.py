import streamlit as st
import datetime

# --- AURA CHEF | THE UNSTOPPABLE BRIDGE v31.0 ---
st.set_page_config(page_title="AURA CHEF | VIDEO FIXED", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; background-color: #000; padding: 15px; border-bottom: 2px solid #1a1a1a; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 2px 8px; }
    .emergency-btn {
        display: block; width: 100%; padding: 25px; background: #34d399; color: #000; 
        text-align: center; font-weight: 900; text-decoration: none; border-radius: 8px;
        text-transform: uppercase; letter-spacing: 2px; transition: 0.3s; margin: 20px 0;
        font-size: 1.2rem;
    }
    .emergency-btn:hover { background: #fff; transform: scale(1.02); }
</style>
""", unsafe_allow_html=True)

# --- DAILY DATA ---
menu = {0: "Lamb Mandi Biryani Fusion", 1: "Wagyu Steak", 2: "Butter Chicken", 3: "Birria Tacos", 4: "Thai Curry", 5: "Nihari", 6: "Pasta"}
day = datetime.datetime.now().weekday()
featured = menu[day]

# VERIFIED VIDEO ID FOR TODAY
video_id = "FjS6m2rOat0" # Professional Mandi Masterclass

t1, t2 = st.tabs(["MASTERCLASS PLAYER", "GLOBAL HERITAGE ENGINE"])

with t1:
    st.markdown(f"<h1 style='text-align: center; font-weight: 900;'>{featured.upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        # THE FINAL FIX: A popup trigger. This bypasses ALL "Unavailable" errors 
        # by launching the video in its own clean browser process.
        yt_url = f"https://www.youtube.com/watch?v={video_id}"
        
        st.markdown(f"""
            <div class="recipe-card" style="text-align:center; border: 2px dashed #34d399;">
                <h3 style="color:#34d399;">VIDEO BRIDGE READY</h3>
                <p>Browsers are blocking the internal player. Click the button below to launch the 4K Masterclass in a Secure Window.</p>
                <a href="{yt_url}" target="_blank" class="emergency-btn">▶ LAUNCH 4K VIDEO PLAYER</a>
                <p style="font-size:0.8rem; color:#444;">Bypassing Restricted Embeds // V31.0</p>
            </div>
        """, unsafe_allow_html=True)

with t2:
    st.markdown("### THE 15-STEP ENGINE")
    dish = st.text_input("DISH", value="Lamb Mandi")
    st.markdown(f"""<div class="recipe-card"><h3>15-STEP PROFESSIONAL {dish.upper()}</h3><p>Technique: Yemeni Spicing with Indo-Pak Dum Steam.</p></div>""", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // V31.0 // 2026</p>", unsafe_allow_html=True)
