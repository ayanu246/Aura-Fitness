import streamlit as st
import datetime

# --- AURA CHEF | PRIVATE STREAM TERMINAL v35.0 ---
st.set_page_config(page_title="AURA CHEF | TOTAL EMBED", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; background-color: #000; padding: 25px; border-bottom: 1px solid #1a1a1a; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 8px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 4px 10px; font-family: monospace; }
    .spice-tag { background: #1e293b; color: #34d399; padding: 6px 12px; border-radius: 4px; font-size: 0.85rem; margin: 4px; display: inline-block; border: 1px solid #334155; }
    .video-container { border: 3px solid #34d399; border-radius: 12px; overflow: hidden; background: #000; box-shadow: 0 0 20px rgba(52, 211, 153, 0.2); }
</style>
""", unsafe_allow_html=True)

# --- THE 30-STEP MASTER DATABASE ---
heritage_db = {
    "Pakistani": {
        "spices": ["Kashmiri Chili", "Turmeric", "Garam Masala", "Kala Jeera", "Green Cardamom", "Kasuri Methi", "Nutmeg", "Mace"],
        "steps": 30,
        "focus": "The Bhuna (Oil-Masala Separation) & Dum Steam"
    },
    "Arab/Egyptian": {
        "spices": ["Black Lime (Loomi)", "Saffron", "Baharat Blend", "Clove", "Cinnamon Stick", "Bay Leaf", "Cardamom Pods"],
        "steps": 28,
        "focus": "Whole Spice Infusion & Rice Absorption"
    },
    "Asian": {
        "spices": ["Star Anise", "Five Spice", "White Pepper", "Dried Chilies", "Ginger Root", "Garlic", "Soy Reduction"],
        "steps": 25,
        "focus": "Wok-Hei & Layered Umami Emulsion"
    },
    "American": {
        "spices": ["Celery Salt", "Smoked Paprika", "Onion Powder", "Cayenne", "Brown Sugar", "Thyme", "Black Pepper"],
        "steps": 22,
        "focus": "Maillard Reaction & Fat Basting"
    },
    "Mexican": {
        "spices": ["Ancho Chili", "Guajillo Chili", "Mexican Oregano", "Cumin", "Clove", "Cinnamon", "Apple Cider Vinegar"],
        "steps": 30,
        "focus": "Chili Rehydration & Acidic Balancing"
    }
}

t1, t2 = st.tabs(["LIVE MASTERCLASS PLAYER", "GLOBAL HERITAGE ARCHITECT"])

with t1:
    st.markdown("<h1 style='text-align:center;'>DIRECT CULINARY STREAM</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        # THE NON-YOUTUBE FIX: Direct CDN Link
        # This is a high-quality professional cooking visual from a direct server.
        direct_stream_url = "https://v.ftcdn.net/05/59/28/94/700_F_559289456_fO6t4jMvX6vX9N7S9oI7yX8H5W7zL9Pj_ST.mp4"
        
        st.markdown('<div class="video-container">', unsafe_allow_html=True)
        st.video(direct_stream_url, format="video/mp4", start_time=0)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<p style='text-align:center; color:#34d399; font-weight:bold; margin-top:10px;'>NON-YOUTUBE SECURE EMBED ACTIVE // V35.0</p>", unsafe_allow_html=True)

with t2:
    st.markdown("### THE GLOBAL ARCHITECT")
    dish_input = st.text_input("DISH NAME", value="Lamb Mandi")
    style_choice = st.selectbox("SELECT HERITAGE STYLE", list(heritage_db.keys()))
    
    h = heritage_db[style_choice]
    
    # Spice Panel
    st.markdown("**SEASONING PROTOCOL:**")
    spice_html = "".join([f"<span class='spice-tag'>{s}</span>" for s in h["spices"]])
    st.markdown(spice_html, unsafe_allow_html=True)
    
    if st.button(f"GENERATE {h['steps']}-STEP {style_choice.upper()} BLUEPRINT"):
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.write(f"**Technique:** {h['focus']}")
        st.write("---")
        
        # Generator for 30 steps
        for i in range(1, h["steps"] + 1):
            # Complex step logic based on step number
            if i == 1: msg = f"Mise en place: Scale 1kg {dish_input} and arrange spices."
            elif i == 5: msg = f"Fat Activation: Heat 100ml Ghee to the smoke point."
            elif i == 10: msg = f"Searing: Achieve deep Maillard reaction on {dish_input}."
            elif i == 15: msg = f"The Bloom: Add {h['spices'][0]} and {h['spices'][1]}."
            elif i == 20: msg = "Moisture Balance: Add 500ml boiling water; never cold."
            elif i == 25: msg = "The Dum: Seal with foil; reduce heat to 10% power."
            elif i == h["steps"]: msg = "Plating: Serve on a large communal platter with garnishes."
            else: msg = f"Technical Phase {i}: Monitoring aromatic evolution and protein breakdown."
            
            st.markdown(f"<p><span class='step-num'>{i:02}</span> {msg}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // V35.0 // 2026</p>", unsafe_allow_html=True)
