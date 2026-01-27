import streamlit as st
import base64

# --- AURA CHEF | THE UNBLOCKABLE TERMINAL v26.0 ---
st.set_page_config(page_title="AURA CHEF | TOTAL FIX", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: monospace; border: 1px solid #34d399; padding: 2px 8px; }
    .video-frame { border: 3px solid #34d399; border-radius: 8px; overflow: hidden; }
</style>
""", unsafe_allow_html=True)

# --- THE "ONE-SHOT" VIDEO FIX ---
# We use an HTML5 player with specific 'controls' and 'autoplay' tags
# This forces the browser to show the play button.
def local_video_player():
    # Direct reliable MP4 link for testing - if this doesn't show a play button, 
    # it means the browser is blocking the 'Autoplay' feature. 
    # I have added 'muted' which is required by most browsers to allow the video to load.
    video_url = "https://www.w3schools.com/html/mov_bbb.mp4" 
    st.markdown(f"""
        <div class="video-frame">
            <video width="100%" height="auto" controls autoplay muted loop>
                <source src="{video_url}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    """, unsafe_allow_html=True)

t1, t2 = st.tabs(["DIRECT MASTERCLASS", "GLOBAL PANTRY ENGINE"])

with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900;'>LAMB MANDI MASTERCLASS</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        local_video_player()
        st.markdown("<p style='text-align:center; color:#34d399; font-weight:bold; margin-top:10px;'>BROWSER-NATIVE PLAYER ACTIVE</p>", unsafe_allow_html=True)

with t2:
    st.markdown("### THE 15-STEP ENGINE")
    dish = st.text_input("ENTER DISH", value="Lamb Mandi")
    
    steps = [
        "<b>Mise En Place:</b> Gather all spices (Hawayij) and 1kg Lamb.",
        "<b>Heat:</b> Get the pot screaming hot with 4 tbsp Ghee.",
        "<b>Sear:</b> Brown the lamb until it has a dark, crispy crust.",
        "<b>Onions:</b> Sauté until they are the color of dark chocolate.",
        "<b>Garlic:</b> Add fresh paste; stir for 60 seconds.",
        "<b>Spices:</b> Add your Mandi mix; toast until fragrant.",
        "<b>Liquids:</b> Add boiling water to cover the meat.",
        "<b>Braise:</b> Simmer on LOW for 45 minutes until tender.",
        "<b>Rice:</b> Soak Basmati for 30 mins, then add to the broth.",
        "<b>The Seal:</b> Use a heavy lid and foil to trap all steam.",
        "<b>Coal Smoke:</b> Place a hot coal in foil; drop oil and seal.",
        "<b>Final Steam:</b> Cook on the lowest heat for 20 mins.",
        "<b>Rest:</b> Let it sit for 10 mins without opening.",
        "<b>Garnish:</b> Use toasted almonds and golden raisins.",
        "<b>Serve:</b> Spread on a large platter and enjoy!"
    ]
    
    st.markdown(f"""<div class="recipe-card">{"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}</div>""", unsafe_allow_html=True)
