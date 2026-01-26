import streamlit as st
import time

# --- AURA CHEF ELITE v5.0 ---
st.set_page_config(page_title="AURA CHEF | HERITAGE", page_icon="⚖️", layout="wide")

# --- ELITE UI STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    
    /* Top Tab Navigation */
    .stTabs [data-baseweb="tab-list"] { 
        justify-content: center; gap: 60px; background-color: #000; padding: 25px; border-bottom: 2px solid #1a1a1a; 
    }
    .stTabs [data-baseweb="tab"] { font-size: 1rem; font-weight: 700; color: #555; text-transform: uppercase; letter-spacing: 1px; }
    .stTabs [data-baseweb="tab-highlight"] { background-color: #fff; }

    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #222; border-radius: 4px; margin-top: 20px; }
    .spice-tag { background: #1a1a1a; color: #fff; padding: 5px 15px; border-radius: 2px; font-size: 0.7rem; font-weight: 800; border: 1px solid #333; margin-right: 5px; }
    
    .stButton>button { border-radius: 0px; background: #fff; color: #000; font-weight: 900; padding: 15px; width: 100%; border: none; }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION TABS ---
t1, t2, t3 = st.tabs(["DAILY SIGNATURE", "HERITAGE ENGINE", "TECHNIQUE VAULT"])

# --- TAB 1: DAILY SIGNATURE ---
with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900; margin-top:40px;'>AURA SELECTION</h1>", unsafe_allow_html=True)
    c1, col_mid, c3 = st.columns([1,2,1])
    with col_mid:
        st.markdown("""
        <div class="recipe-card" style="text-align: center;">
            <p style="color:#888; letter-spacing:2px; font-size:0.7rem;">CHEF'S CHOICE</p>
            <h2 style="letter-spacing:-1px;">PAKISTANI CHAPLI KEBAB PLATTER</h2>
            <p style="color:#666;">Hand-crushed pomegranate seeds, dry coriander, and green chili infusion.</p>
        </div>
        """, unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=6bt0BlYMovE")

# --- TAB 2: HERITAGE ENGINE (THE SPICE SELECTOR) ---
with t2:
    st.markdown("### HERITAGE ENGINE")
    st.caption("INPUT INGREDIENTS AND SELECT YOUR FLAVOR HERITAGE")
    
    # Input field (Press Enter to Submit)
    dish_base = st.text_input("1. WHAT ARE YOU COOKING? (e.g. Chicken, Beef, Rice, Potatoes)", placeholder="Type and press Enter...")

    if dish_base:
        st.markdown("---")
        st.markdown("### 2. SELECT FLAVOR HERITAGE")
        # The user chooses the style
        heritage = st.radio("WHICH SPICE PROFILE SHOULD WE APPLY?", 
                            ["Pakistani", "Indian", "Mexican", "Asian", "American/Western"], 
                            horizontal=True)

        with st.spinner(f"APPLYING {heritage.upper()} AROMATICS..."):
            time.sleep(1)
            
            # SPICE LOGIC DATA
            spice_data = {
                "Pakistani": ["Garam Masala", "Kashmiri Red Chili", "Dry Coriander", "Turmeric", "Cumin Seeds"],
                "Indian": ["Cardamom", "Mustard Seeds", "Curry Leaves", "Saffron", "Fenugreek"],
                "Mexican": ["Smoked Paprika", "Cumin", "Oregano", "Chipotle Powder", "Ancho Chili"],
                "Asian": ["Star Anise", "Five Spice", "White Pepper", "Ginger Powder", "Sesame"],
                "American/Western": ["Garlic Powder", "Onion Powder", "Black Pepper", "Thyme", "Rosemary"]
            }

            video_links = {
                "Pakistani": "https://www.youtube.com/watch?v=eqPgJPLRutI",
                "Indian": "https://www.youtube.com/watch?v=V37Lp5C7V6Q",
                "Mexican": "https://www.youtube.com/watch?v=Xra45DHI8UE",
                "Asian": "https://www.youtube.com/watch?v=ry2lNNVz5DM",
                "American/Western": "https://www.youtube.com/watch?v=ry2lNNVz5DM"
            }

            spices = spice_data[heritage]
            
            st.markdown(f"""
            <div class="recipe-card">
                <h2 style="margin-bottom:5px;">{heritage} Style {dish_base}</h2>
                <div style="margin-bottom:20px;">
                    {' '.join([f'<span class="spice-tag">{s.upper()}</span>' for s in spices])}
                </div>
                <hr style="border:0.1px solid #333">
                <div style="display: flex; gap: 20px;">
                    <div style="flex: 2;">
                        <h4>TECHNICAL STEPS</h4>
                        <p>1. <b>Bloom:</b> Heat oil and toast your <b>{spices[0]}</b> and <b>{spices[1]}</b> first.</p>
                        <p>2. <b>Infuse:</b> Add your {dish_base} and allow the heritage aromatics to penetrate the protein.</p>
                        <p>3. <b>Finish:</b> Season with <b>{spices[-1]}</b> for the final flavor profile.</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.video(video_links[heritage])

# --- TAB 3: TECHNIQUE VAULT (SEARCH DISH, GET HOW-TO) ---
with t3:
    st.markdown("### TECHNIQUE VAULT")
    search_query = st.text_input("SEARCH FOR A SPECIFIC DISH (e.g. Biryani, Burger, Tacos)")
    
    if search_query:
        st.markdown(f"""
        <div class="recipe-card">
            <h3>MASTERCLASS: {search_query.upper()}</h3>
            <p style="color:#888;">Technical breakdown for {search_query} preparation.</p>
        </div>
        """, unsafe_allow_html=True)
        # Pulls a general high-quality tutorial
        st.video("https://www.youtube.com/watch?v=hKTN6Njxqxk")

st.markdown("<br><br><p style='text-align:center; color:#333; font-size:0.7rem; letter-spacing:2px;'>AURA CHEF // GLOBAL HERITAGE TERMINAL // 2026</p>", unsafe_allow_html=True)
