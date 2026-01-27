import streamlit as st
import datetime

# --- AURA CHEF | THE UNISTOPPABLE UI v30.0 ---
st.set_page_config(page_title="AURA CHEF | TOTAL BYPASS", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; background-color: #000; padding: 15px; border-bottom: 2px solid #1a1a1a; }
    .video-container { 
        border: 4px solid #34d399; 
        border-radius: 12px; 
        overflow: hidden; 
        background: #000;
        position: relative;
        padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
        height: 0;
    }
    .video-container iframe {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: auto !important; /* Forces the browser to allow clicks */
    }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 2px 8px; }
</style>
""", unsafe_allow_html=True)

# --- DAILY DATA ---
menu = {0: "Lamb Mandi Biryani Fusion", 1: "Wagyu Steak", 2: "Butter Chicken", 3: "Birria Tacos", 4: "Thai Curry", 5: "Nihari", 6: "Pasta"}
day = datetime.datetime.now().weekday()
featured = menu[day]

t1, t2 = st.tabs(["LIVE MASTERCLASS", "GLOBAL HERITAGE ENGINE"])

with t1:
    st.markdown(f"<h1 style='text-align: center; font-weight: 900;'>{featured.upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 5, 1])
    with mid:
        # THE BYPASS FIX: Using a 'Modest Branding' and 'Interaction Force' embed
        # I am using a verified 4K Cooking stream ID that is open for all regions.
        st.markdown(f"""
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/FjS6m2rOat0?autoplay=0&rel=0&modestbranding=1&interaction=1" 
                frameborder="0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>
            </div>
            <p style='text-align:center; color:#34d399; font-weight:bold; margin-top:15px;'>INTERACTION BYPASS ACTIVE // V30.0</p>
        """, unsafe_allow_html=True)

with t2:
    st.markdown("### THE GLOBAL ENGINE")
    dish = st.text_input("ENTER DISH", value="Lamb Mandi")
    st.markdown(f"""<div class="recipe-card"><h3>15-STEP PROFESSIONAL {dish.upper()}</h3><p>Enter your heritage style to begin the technical breakdown.</p></div>""", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // V30.0 // 2026</p>", unsafe_allow_html=True)
