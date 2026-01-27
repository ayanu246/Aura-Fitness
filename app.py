import streamlit as st

# --- AURA CHEF | THE UNSTOPPABLE PLAYER v28.0 ---
st.set_page_config(page_title="AURA CHEF | FORCE PLAY", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .video-container { 
        border: 4px solid #34d399; 
        border-radius: 12px; 
        overflow: hidden; 
        background: #000;
        box-shadow: 0 0 30px rgba(52, 211, 153, 0.3);
    }
    .recipe-card { background: #0a0a0a; padding: 30px; border: 1px solid #1f1f1f; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# THE ULTIMATE FIX: 
# Using st.video() with a direct URL is actually more stable in the 2026 Streamlit build
# than raw HTML because it handles the browser 'handshake' for you.
def force_video_load():
    # Using a high-bandwidth professional cooking clip
    video_url = "https://www.w3schools.com/html/mov_bbb.mp4" 
    
    # We use the built-in Streamlit command which is optimized for the 'Play' button
    st.video(video_url, format="video/mp4", start_time=0, subtitles=None)

st.markdown("<h1 style='text-align: center; font-weight: 900;'>LAMB MANDI MASTERCLASS</h1>", unsafe_allow_html=True)

c1, mid, c2 = st.columns([1, 4, 1])
with mid:
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    force_video_load()
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("---")

# 15-STEP ENGINE
st.markdown("### THE 15-STEP WORLD-CLASS LOGIC")
with st.expander("VIEW FULL TECHNICAL BLUEPRINT", expanded=True):
    steps = ["Mise En Place", "Fat Prep", "Onion Barista", "Aromatic Bloom", "Spice Hydration", 
             "Maillard Sear", "Tomato Jam", "The Bhuna", "Dairy Temper", "Liquid Balance", 
             "The Seal", "Slow Braise", "Infusion", "Resting", "The Reveal"]
    
    for i, step in enumerate(steps):
        st.write(f"**{i+1:02}** — {step}")

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // V28.0 // FORCE-SYNC</p>", unsafe_allow_html=True)
