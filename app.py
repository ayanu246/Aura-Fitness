import streamlit as st
import time

# --- AURA CHEF AI v14.0 ---
st.set_page_config(page_title="AURA CHEF | AI INTELLIGENCE", page_icon="⚖️", layout="wide")

# --- PRO TERMINAL STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 40px; background-color: #000; padding: 20px; border-bottom: 2px solid #1a1a1a; }
    .stTabs [data-baseweb="tab"] { font-size: 0.85rem; font-weight: 700; color: #444; text-transform: uppercase; letter-spacing: 1.5px; }
    .recipe-card { background: #0a0a0a; padding: 45px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 25px; line-height: 1.8; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: monospace; border: 1px solid #34d399; padding: 2px 8px; }
    .heat-tag { font-weight: bold; padding: 2px 8px; border-radius: 2px; font-size: 0.75rem; text-transform: uppercase; }
    .high { background: #471111; color: #ff4b4b; }
    .med { background: #473211; color: #ffa500; }
    .low { background: #112247; color: #4b96ff; }
    .ai-visual-frame { border: 2px solid #34d399; padding: 10px; border-radius: 4px; background: #000; text-align: center; }
</style>
""", unsafe_allow_html=True)

t1, t2 = st.tabs(["AI SIGNATURE SELECTION", "GLOBAL HERITAGE ENGINE"])

# --- TAB 1: AI SIGNATURE ---
with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900; margin-top:40px;'>AURA AI SELECTION</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1,2,1])
    with mid:
        st.markdown("""
        <div class="recipe-card">
            <h2 style="text-align:center;">Lamb Mandi & Biryani Fusion</h2>
            <p style="color:#666; text-align:center;">AI-Engineered recipe combining smoke-infusion with 32-spice complexity.</p>
            <div class="ai-visual-frame">
                <p style="color:#34d399; font-size:0.7rem; letter-spacing:2px;">AI VIDEO PREVIEW GENERATING...</p>
                <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqZ2V6eHByZzRycHJ0ZzRycHJ0ZzRycHJ0ZzRycHJ0ZzRycHJ0JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxVjFzRjT7W/giphy.gif" width="100%">
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: GLOBAL ENGINE (15 STEPS) ---
with t2:
    st.markdown("### GLOBAL HERITAGE ENGINE")
    items = st.text_input("ENTER INGREDIENTS", placeholder="Chicken, Beef, Lamb, etc.")
    
    if items:
        heritage = st.selectbox("CHOOSE HERITAGE", ["Pakistani", "Indian", "Arab/Egyptian", "Asian", "Mexican", "American"])
        
        # This database contains the deep 15-step logic
        db = {
            "Pakistani": [
                "<b>Mise En Place:</b> Peel and thin-slice 3 large onions; crush 3 inches of ginger and 10 garlic cloves.",
                "<b>Fat Activation:</b> Heat 1/2 cup oil on <span class='heat-tag high'>HIGH</span> until it shimmers.",
                "<b>The Browning:</b> Sauté onions for 12-15 mins. They must be uniform chocolate brown for authentic flavor.",
                "<b>Aromatic Bloom:</b> Add ginger-garlic paste. Stir for 90 seconds until the raw smell is replaced by sweetness.",
                "<b>Spice Hydration:</b> Mix Garam Masala, Chili, and Turmeric with 2 tbsp water; add to pot to prevent scorching.",
                "<b>The Maillard Reaction:</b> Add " + items + ". Increase heat to max and sear until deep brown on all sides.",
                "<b>Acidity Layer:</b> Add 2 chopped tomatoes. Cook until they dissolve into a jam-like consistency.",
                "<b>The Bhuna:</b> Continue stirring on high heat until the oil separates completely from the masala paste.",
                "<b>Dairy Tempering:</b> Reduce to <span class='heat-tag med'>MEDIUM</span>. Add whisked yogurt one spoonful at a time.",
                "<b>Pressure/Cover:</b> Add 1 cup hot water. Cover with a heavy, weighted lid.",
                "<b>Slow Braise:</b> Reduce heat to <span class='heat-tag low'>LOW</span>. Simmer for 35 minutes for fall-off-the-bone texture.",
                "<b>The Scent:</b> Add 4 slit green chilies and a palmful of dried fenugreek leaves (Kasuri Methi).",
                "<b>Garnish:</b> Use 1 cup of fresh cilantro and 1/2 cup of julienned ginger.",
                "<b>Resting Phase:</b> Turn off heat. Keep lid sealed for 10 mins to allow juices to redistribute.",
                "<b>Service:</b> Serve on a heated platter with Roghni Naan or Basmati rice."
            ],
            "Arab/Egyptian": [
                 "<b>Ghee Prep:</b> Melt 4 tbsp of pure Ghee in a heavy Dutch oven over <span class='heat-tag med'>MEDIUM</span> heat.",
                 "<b>Aromatic Start:</b> Sauté 2 onions until translucent. Do not brown them—keep them sweet.",
                 "<b>Whole Spice Toast:</b> Add 4 green cardamom pods, 1 cinnamon stick, and 2 dried limes (Loomi).",
                 "<b>Heritage Spices:</b> Add 1 tbsp of Baharat and 1 tsp of Sumac. Toast for 45 seconds.",
                 "<b>Searing:</b> Add your " + items + ". Sear until the exterior is golden and coated in yellow ghee.",
                 "<b>Braising:</b> Add 3 cups of boiling water. Cover and simmer on <span class='heat-tag low'>LOW</span> for 45 minutes.",
                 "<b>Nut Prep:</b> In a separate pan, fry almonds and pine nuts in butter until golden. Drain.",
                 "<b>Rice Integration:</b> Add washed and soaked long-grain rice to the meat broth.",
                 "<b>Liquid Check:</b> Ensure liquid is exactly 2cm above the rice line.",
                 "<b>Absorption:</b> Bring to boil on <span class='heat-tag high'>HIGH</span> until holes appear in the rice.",
                 "<b>The Dum:</b> Cover with a tight cloth and lid. Cook on lowest possible heat for 20 mins.",
                 "<b>The Smoke:</b> Light a charcoal briquette. Place in a foil cup with oil inside the pot. Close for 5 mins.",
                 "<b>Flipping:</b> Carefully remove the meat and fluff the rice with a fork.",
                 "<b>Plating:</b> Arrange rice on a giant platter, place the meat on top.",
                 "<b>Final Touch:</b> Shower with the toasted nuts and fresh chopped parsley."
            ]
        }
        
        # Fallback logic for remaining heritages
        steps = db.get(heritage, db["Pakistani"])

        st.markdown(f"""
        <div class="recipe-card">
            <h2 style="color:#34d399; text-align:center;">AI CULINARY BLUEPRINT: {heritage.upper()} {items.upper()}</h2>
            <hr style="border:0.1px solid #333">
            {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
        </div>
        """, unsafe_allow_html=True)
        
        

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // AI SECURE TERMINAL // 2026</p>", unsafe_allow_html=True)
