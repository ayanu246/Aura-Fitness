import streamlit as st
import datetime

# --- AURA CHEF | GLOBAL ELITE TERMINAL v36.0 ---
st.set_page_config(page_title="AURA CHEF | GLOBAL ELITE", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; background-color: #000; padding: 25px; border-bottom: 1px solid #1a1a1a; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 8px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; border: 1px solid #34d399; padding: 2px 8px; font-family: monospace; }
    .spice-tag { background: #1e293b; color: #34d399; padding: 6px 12px; border-radius: 4px; font-size: 0.85rem; margin: 4px; display: inline-block; border: 1px solid #334155; }
    .video-frame { border: 3px solid #34d399; border-radius: 12px; overflow: hidden; background: #000; }
</style>
""", unsafe_allow_html=True)

# --- DIRECT MEDIA DATABASE (UNBLOCKABLE MP4s) ---
# These are professional culinary clips that rotate based on the day of the week
daily_media = {
    0: {"name": "Lamb Mandi Fusion", "url": "https://assets.mixkit.co/videos/preview/mixkit-cooking-meat-in-a-pan-close-up-4690-large.mp4"},
    1: {"name": "Wagyu Garlic Steak", "url": "https://assets.mixkit.co/videos/preview/mixkit-fresh-steak-being-fried-in-a-pan-4693-large.mp4"},
    2: {"name": "Royal Butter Chicken", "url": "https://assets.mixkit.co/videos/preview/mixkit-chef-preparing-a-dish-in-a-professional-kitchen-4700-large.mp4"},
    3: {"name": "Mexican Birria Tacos", "url": "https://assets.mixkit.co/videos/preview/mixkit-chef-cutting-meat-with-a-knife-4703-large.mp4"},
    4: {"name": "Authentic Ramen Masterclass", "url": "https://assets.mixkit.co/videos/preview/mixkit-preparing-delicious-ramen-soup-42861-large.mp4"},
    5: {"name": "Pakistani Nihari Slow-Braise", "url": "https://assets.mixkit.co/videos/preview/mixkit-putting-seasoning-on-meat-4691-large.mp4"},
    6: {"name": "Truffle Pasta Masterclass", "url": "https://assets.mixkit.co/videos/preview/mixkit-chef-preparing-a-gourmet-pasta-dish-4701-large.mp4"}
}

day_idx = datetime.datetime.now().weekday()
featured = daily_media[day_idx]

# --- DEEP HERITAGE DATABASE ---
heritage_db = {
    "Pakistani": {
        "spices": ["Kashmiri Chili", "Turmeric", "Garam Masala", "Kala Jeera", "Green Cardamom", "Kasuri Methi", "Nutmeg", "Mace"],
        "steps": 30, "focus": "The Bhuna (Oil-Masala Separation) & Dum Steam"
    },
    "Arab/Egyptian": {
        "spices": ["Black Lime (Loomi)", "Saffron", "Baharat Blend", "Clove", "Cinnamon Stick", "Bay Leaf", "Cardamom Pods"],
        "steps": 30, "focus": "Whole Spice Infusion & Rice Absorption"
    },
    "Asian": {
        "spices": ["Star Anise", "Five Spice", "White Pepper", "Dried Chilies", "Ginger Root", "Garlic", "Soy Reduction"],
        "steps": 25, "focus": "Wok-Hei & Layered Umami Emulsion"
    },
    "American": {
        "spices": ["Smoked Paprika", "Garlic Powder", "Cayenne", "Brown Sugar", "Thyme", "Mustard Powder"],
        "steps": 22, "focus": "Maillard Reaction & Butter Basting"
    },
    "Mexican": {
        "spices": ["Ancho Chili", "Guajillo Chili", "Mexican Oregano", "Cumin", "Clove", "Cinnamon", "Apple Cider Vinegar"],
        "steps": 30, "focus": "Chili Rehydration & Braising"
    }
}

tab1, tab2 = st.tabs(["MASTERCLASS PORTAL", "GLOBAL HERITAGE ENGINE"])

with tab1:
    st.markdown(f"<h1 style='text-align: center; font-weight: 900;'>{featured['name'].upper()}</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    with mid:
        # THE YETI-STYLE FIX: Native HTML5 Video Tag
        # This is unblockable because it is a direct .mp4 file.
        st.markdown(f"""
            <div class="video-frame">
                <video width="100%" height="auto" controls autoplay muted loop>
                    <source src="{featured['url']}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            <p style='text-align:center; color:#34d399; font-weight:bold; margin-top:15px;'>
                DIRECT 4K CULINARY STREAM: ACTIVE // V36.0
            </p>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### THE GLOBAL ARCHITECT")
    dish = st.text_input("DISH NAME", value="Lamb")
    heritage = st.selectbox("SELECT HERITAGE STYLE", list(heritage_db.keys()))
    
    h = heritage_db[heritage]
    st.markdown("**SEASONING PROTOCOL:**")
    st.markdown("".join([f"<span class='spice-tag'>{s}</span>" for s in h['spices']]), unsafe_allow_html=True)
    
    if st.button(f"GENERATE {h['steps']}-STEP BLUEPRINT"):
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.write(f"**Primary Technique:** {h['focus']}")
        st.write("---")
        for i in range(1, h['steps'] + 1):
            if i == 1: text = f"Mise en place: Scale {dish} and prep heritage spices."
            elif i == 15: text = f"Technical Stage: Infusing {h['spices'][0]} into the fat medium."
            elif i == h['steps']: text = f"Final Presentation: Garnish and serve the ultimate {heritage} {dish}."
            else: text = f"Technical Phase {i}: Monitoring aromatic development and thermal consistency."
            st.markdown(f"<p><span class='step-num'>{i:02}</span> {text}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
