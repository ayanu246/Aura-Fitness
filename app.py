import streamlit as st
import time

# --- AURA CHEF ELITE v8.0 ---
st.set_page_config(page_title="AURA CHEF | PROFESSIONAL", page_icon="⚖️", layout="wide")

# --- CUSTOM CSS: TERMINAL AESTHETIC ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    
    .stTabs [data-baseweb="tab-list"] { 
        justify-content: center; gap: 50px; background-color: #000; padding: 20px; border-bottom: 2px solid #1a1a1a; 
    }
    .stTabs [data-baseweb="tab"] { font-size: 0.9rem; font-weight: 700; color: #444; text-transform: uppercase; }
    
    .dish-card { background: #0a0a0a; padding: 30px; border: 1px solid #222; border-radius: 4px; margin-top: 20px; }
    .spice-tag { background: #1a1a1a; color: #34d399; padding: 4px 10px; border: 1px solid #34d399; font-size: 0.7rem; font-weight: 800; margin-right: 5px; }
    .step-label { color: #555; font-weight: 900; margin-right: 10px; }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
t1, t2, t3 = st.tabs(["SELECTION OF THE DAY", "PANTRY ENGINE", "GLOBAL VIDEO VAULT"])

# --- TAB 1: SELECTION OF THE DAY ---
with t1:
    st.markdown("<h1 style='text-align: center; font-weight: 900; margin-top:40px;'>AURA SIGNATURE</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1,2,1])
    with mid:
        st.markdown("""
        <div class="dish-card" style="text-align: center;">
            <p style="color:#888; letter-spacing:2px; font-size:0.7rem;">CHEF'S SPECIAL</p>
            <h2 style="margin-top:10px;">Authentic Chicken Karahi</h2>
            <p style="color:#666;">Traditional Pakistani high-heat wok cooking with fresh ginger and green chilies.</p>
        </div>
        """, unsafe_allow_html=True)
        # VERIFIED COOKING VIDEO
        st.video("https://www.youtube.com/watch?v=eqPgJPLRutI")

# --- TAB 2: PANTRY ENGINE ---
with t2:
    st.markdown("### PANTRY ENGINE")
    
    user_items = st.text_input("INPUT INGREDIENTS (e.g. Chicken, Potato, Rice)", placeholder="Type and press Enter...")

    if user_items:
        st.markdown("---")
        # SPICE SELECTION
        style = st.radio("SELECT SPICE PROFILE", ["Pakistani", "Indian", "Mexican", "Asian", "American"], horizontal=True)
        
        spice_map = {
            "Pakistani": ["Garam Masala", "Kashmiri Chili", "Coriander", "Turmeric"],
            "Indian": ["Cardamom", "Curry Leaves", "Mustard Seeds", "Saffron"],
            "Mexican": ["Smoked Paprika", "Cumin", "Chipotle", "Dried Oregano"],
            "Asian": ["Five Spice", "White Pepper", "Star Anise", "Ginger Powder"],
            "American": ["Garlic Powder", "Black Pepper", "Thyme", "Onion Powder"]
        }
        
        selected_spices = spice_map[style]
        
        st.markdown(f"### {style} Style Generation")
        st.markdown(f"{' '.join([f'<span class="spice-tag">{s.upper()}</span>' for s in selected_spices])}", unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"""
            <div class="dish-card">
                <h4>Option 1: {style} Stir-fry / Roast</h4>
                <p><span class="step-label">01</span> Heat oil and toast {selected_spices[0]}.</p>
                <p><span class="step-label">02</span> Add your {user_items} and sear on high heat.</p>
                <p><span class="step-label">03</span> Season with {selected_spices[1]} and {selected_spices[2]}.</p>
                <p><span class="step-label">04</span> Finish with fresh herbs and lemon juice.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown(f"""
            <div class="dish-card">
                <h4>Option 2: {style} Traditional Stew</h4>
                <p><span class="step-label">01</span> Sauté onions with {selected_spices[3]}.</p>
                <p><span class="step-label">02</span> Slow-cook {user_items} in a covered pot.</p>
                <p><span class="step-label">03</span> Add water or broth to create a rich gravy.</p>
                <p><span class="step-label">04</span> Simmer until tender and aromatics are released.</p>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 3: GLOBAL VIDEO VAULT ---
with t3:
    st.markdown("### GLOBAL VIDEO VAULT")
    search_query = st.text_input("SEARCH DISH (e.g. Biryani, Butter Chicken, Tacos, Burgers)", key="v_search")
    
    if search_query:
        query_low = search_query.lower()
        
        # MASTER RECIPE DATABASE
        recipes = {
            "biryani": {
                "title": "Hyderabadi Chicken Biryani",
                "steps": "1. Marinate meat in spices and yogurt. 2. Parboil long-grain Basmati. 3. Layer and seal for 'Dum' cooking.",
                "url": "https://www.youtube.com/watch?v=eqPgJPLRutI"
            },
            "butter chicken": {
                "title": "Makhani Butter Chicken",
                "steps": "1. Tandoori-style chicken grill. 2. Tomato and cashew gravy reduction. 3. Finished with cold butter and cream.",
                "url": "https://www.youtube.com/watch?v=a03U45jFxOI"
            },
            "burger": {
                "title": "The Perfect Smash Burger",
                "steps": "1. High-fat beef balls. 2. Hard press on hot griddle for crust. 3. Steamed bun with melted cheddar.",
                "url": "https://www.youtube.com/watch?v=6bt0BlYMovE"
            },
            "taco": {
                "title": "Mexican Street Tacos",
                "steps": "1. Thinly sliced marinated beef. 2. Flash fry on flat-top. 3. Top with white onion and cilantro.",
                "url": "https://www.youtube.com/watch?v=Xra45DHI8UE"
            }
        }
        
        # Check for a match
        found = False
        for key, data in recipes.items():
            if key in query_low:
                st.markdown(f"""
                <div class="dish-card">
                    <h2 style="color:#34d399;">{data['title']}</h2>
                    <hr style="border:0.1px solid #333">
                    <p><b>TECHNIQUE:</b> {data['steps']}</p>
                </div>
                """, unsafe_allow_html=True)
                st.video(data['url'])
                found = True
                break
        
        if not found:
            st.error("DISH NOT IN LOCAL DATABASE. TRY: BIRYANI, BUTTER CHICKEN, BURGER, OR TACOS.")

st.markdown("<br><br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // SECURE TERMINAL // 2026</p>", unsafe_allow_html=True)
