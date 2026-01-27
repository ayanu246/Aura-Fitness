import streamlit as st
import datetime

# --- AURA CHEF | DIRECT MEDIA FIXED v25.0 ---
st.set_page_config(page_title="AURA CHEF | DIRECT VIDEO", page_icon="⚖️", layout="wide")

# --- UI STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
    .recipe-card { background: #0a0a0a; padding: 40px; border: 1px solid #1f1f1f; border-radius: 4px; margin-top: 20px; }
    .step-num { color: #34d399; font-weight: 900; margin-right: 15px; font-family: monospace; border: 1px solid #34d399; padding: 2px 8px; }
    video { border: 2px solid #34d399; border-radius: 8px; width: 100%; box-shadow: 0 0 20px rgba(52, 211, 153, 0.2); }
</style>
""", unsafe_allow_html=True)

# --- DIRECT MEDIA DATABASE (No YouTube Restrictions) ---
# We use direct .mp4 links from cloud storage (like Cloudinary or Pexels)
# These NEVER show "Video Unavailable" because they are raw video files.
daily_media = {
    "Lamb Mandi Biryani Fusion": "https://assets.mixkit.co/videos/preview/mixkit-cooking-meat-in-a-pan-close-up-4690-large.mp4",
    "Generic Chef Masterclass": "https://assets.mixkit.co/videos/preview/mixkit-chef-preparing-a-dish-in-a-professional-kitchen-4700-large.mp4"
}

tab1, tab2 = st.tabs(["DIRECT MASTERCLASS", "GLOBAL PANTRY ENGINE"])

with tab1:
    st.markdown("<h1 style='text-align: center; font-weight: 900;'>LAMB MANDI BIRYANI FUSION</h1>", unsafe_allow_html=True)
    c1, mid, c2 = st.columns([1, 4, 1])
    
    with mid:
        # THE ONE-SHOT FIX: Direct HTML5 Video Player
        # This bypasses all YouTube blocks.
        st.video(daily_media["Lamb Mandi Biryani Fusion"], format="video/mp4", start_time=0)
        
        st.markdown("<p style='text-align:center; color:#34d399; font-weight:bold; margin-top:10px;'>DIRECT MP4 STREAM SECURED // NO YOUTUBE BLOCKS</p>", unsafe_allow_html=True)

with tab2:
    st.markdown("### GLOBAL PANTRY ENGINE")
    # This is where kids can type what they want
    user_idea = st.text_input("KIDS: WHAT DO YOU WANT TO MAKE TODAY?", placeholder="e.g. Pasta, Tacos, Burgers...")
    
    if user_idea:
        # THE "KIDS-FIX" 15-STEP LOGIC
        st.markdown(f"### HOW TO MAKE THE BEST {user_idea.upper()} IN THE WORLD")
        steps = [
            "**Mise En Place:** Gather all your tools and ingredients like a professional chef.",
            "**Safety Check:** Make sure an adult is nearby before turning on the heat.",
            "**Prep the Base:** Chop your vegetables or protein into even, bite-sized pieces.",
            "**The Heat:** Pre-heat your pan until it's 'chef hot' (when water beads dance on it).",
            "**The Sear:** Brown your main ingredient first to lock in all the flavor.",
            "**Aromatics:** Add garlic or onions; wait until the kitchen smells amazing.",
            "**Spice Layering:** Add your salt and secret spices now so they cook into the food.",
            "**The Sauce:** Pour in your liquid (broth or sauce) and scrape the bottom of the pan.",
            "**Simmering:** Turn the heat down low and let the flavors 'marry' each other.",
            "**Testing:** Use a clean spoon to taste. Does it need more salt? More zing?",
            "**The Secret Ingredient:** Add a tiny pat of butter at the end for that restaurant shine.",
            "**Plating:** Use a big white plate; food always looks better with space around it.",
            "**Garnish:** Add a sprinkle of green (parsley or cilantro) to make it 'pop'.",
            "**The Reveal:** Present it to your family and tell them the story of how you made it.",
            "**Cleanup:** Real chefs always clean their station before they eat!"
        ]
        
        st.markdown(f"""
            <div class="recipe-card">
                {"".join([f"<p><span class='step-num'>{i+1:02}</span> {s}</p>" for i, s in enumerate(steps)])}
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#222; font-size:0.7rem;'>AURA CHEF // V25.0 // CLOUD NATIVE</p>", unsafe_allow_html=True)
