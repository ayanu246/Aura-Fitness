import streamlit as st
import datetime

# --- AURA CHEF AI v20.0 ---
st.set_page_config(page_title="AURA CHEF | LIVE VIDEO", page_icon="⚖️", layout="wide")

# --- UI STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: monospace; border: 1px solid #34d399; padding: 2px 8px; }
    .video-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000; border: 2px solid #1a1a1a; }
    .video-container iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
</style>
""", unsafe_allow_html=True)

# --- DAILY FOOD LOGIC ---
menu = {
    0: {"name": "Lamb Mandi Biryani Fusion", "id": "FjS6m2rOat0"}, # Specific Video IDs that allow embedding
    1: {"name": "Wagyu Smash Burgers", "id": "6bt0BlYMovE"},
    2: {"name": "Butter Chicken Masterclass", "id": "a03U45jFxOI"},
    3: {"name": "Mexican Birria Tacos", "id": "Xra45DHI8UE"},
    4: {"name": "Thai Green Curry", "id": "ry2lNNVz5DM"},
    5: {"name": "Authentic Nihari", "id": "281_2v7X0p0"},
    6: {"name": "Gourmet Pasta", "id": "LpM2c397Vuc"}
}
day = datetime.datetime.now().weekday()
food = menu[day]

t1, t2 = st.tabs(["LIVE MASTERCLASS", "GLOBAL PANTRY ENGINE"])

# --- TAB 1: DIRECT VIDEO EMBED ---
with t1:
    st.markdown(f"<h1 style='text-align: center; font-weight: 900;'>{food['name'].upper()}</h1>", unsafe_allow_html=True)
    
    # This is the "One Shot" fix: Embedding the video directly into the UI
    st.markdown(f"""
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/{food['id']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='text-align:center; color:#444; margin-top:10px;'>DIRECT STREAM SECURED // 4K CULINARY DATA</p>", unsafe_allow_html=True)

# --- TAB 2: PANTRY ENGINE ---
with t2:
    st.markdown("### GLOBAL PANTRY ENGINE")
    item = st.text_input("WHAT ARE WE CREATING?", placeholder="e.g. Chicken, Beef, Lamb...")
    
    if item:
        heritage = st.selectbox("SELECT STYLE", ["Pakistani", "Arab/Egyptian", "Indian", "Asian", "Mexican", "American"])
        
        # 15-Step Professional Database
        steps = [
            f"<b>Mise En Place:</b> Organize all spices and prep 1kg of {item}.",
            f"<b>Fat Prep:</b> Heat oil/ghee to <span style='color:#ff4b4b;'>HIGH</span>.",
            f"<b>Aromatics:</b> Sauté onions until deep 'Barista' brown (15 mins).",
            f"<b>Bloom:</b> Add ginger-garlic paste and toast for 2 mins.",
            f"<b>Spice Work:</b> Hydrate your dry spices with water before adding to the fat.",
            f"<b>Searing:</b> Flash-sear {item} to trigger the Maillard reaction.",
            f"<b>Deglazing:</b> Add tomato puree and scrape the flavor from the bottom.",
            f"<b>The Bhuna:</b> Cook until the oil separates from the spice paste.",
            f"<b>Tempering:</b> Whisk in yogurt on <span style='color:#ffa500;'>MEDIUM</span> heat.",
            f"<b>Braising:</b> Add boiling water, cover, and drop to <span style='color:#4b96ff;'>LOW</span>.",
            f"<b>Infusion:</b> Add fresh chilies and whole spices (cardamom/cloves).",
            f"<b>The Dum:</b> Seal the lid with foil or dough for 20 minutes.",
            f"<b>Smoke:</b> Optional: Infuse with a hot coal for 5 mins.",
            f"<b>Relaxation:</b> Turn off heat; let rest for 10 minutes.",
            f"<b>Final Plating:</b> Garnish with cilantro and serve immediately."
        ]
        
        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">{heritage.upper()} {item.upper()}</h2>
            <hr style="border:0.1px solid #222">
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // V20.0 // 2026</p>", unsafe_allow_html=True)
