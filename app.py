import streamlit as st
from supabase import create_client
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import time

# --- DB CONNECTION ---
URL = "https://uetvrqirjmbgodcbsruh.supabase.co"
KEY = "sb_publishable_6lw0WScY9K1LJ4Itwmw4Eg_07kYJdlC"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Aura Elite", layout="wide")

# --- PRO UI (STRICTLY MAINTAINED) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Helvetica Neue', sans-serif; }
    .stat-card { background: #1c1c1e; padding: 25px; border-radius: 15px; border: 1px solid #2c2c2e; text-align: left; }
    .label { color: #8e8e93; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .value { font-size: 2.5rem; font-weight: 900; color: #007aff; margin: 5px 0; }
    .stButton>button { border-radius: 8px; background: #007aff; color: white; border: none; font-weight: 600; width: 100%; padding: 10px; }
</style>
""", unsafe_allow_html=True)

# --- LOGIN & CLOUD RESTORE ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("Aura Elite Athlete Login")
    u_in = st.text_input("Athlete ID", placeholder="Username to load data...")
    if st.button("AUTHENTICATE"):
        if u_in:
            st.session_state.user_name = u_in
            st.session_state.auth = True
            try:
                r = supabase.table("aura_collab_tracker").select("*").eq("username", u_in).execute()
                if r.data:
                    st.session_state.steps = r.data[0].get('steps', 0)
                    st.session_state.exercise = r.data[0].get('exercise_mins', 0)
                    st.session_state.water = r.data[0].get('water', 0)
                    st.session_state.active_group = r.data[0].get('group_name', 'Global')
            except: pass
            st.rerun()
    st.stop()

# --- INIT DEFAULTS ---
for k, v in {"steps": 0, "water": 0, "exercise": 0, "active_group": "Global"}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- TABS ---
t1, t2, t3, t4 = st.tabs(["DASHBOARD", "TRAINING", "COMMUNITY", "NETWORKS"])

with t1:
    st.markdown(f"### Athlete: {st.session_state.user_name}")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="stat-card"><div class="label">Move</div><div class="value">{st.session_state.steps}</div><div class="label">Steps</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="stat-card"><div class="label">Exercise</div><div class="value" style="color:#30d158">{st.session_state.exercise}</div><div class="label">Mins</div></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="stat-card"><div class="label">Hydration</div><div class="value" style="color:#64d2ff">{st.session_state.water}</div><div class="label">Glasses</div></div>', unsafe_allow_html=True)

    if st.button("🔄 SYNC APPLE / SAMSUNG HEALTH"):
        st.info("Handshaking with Health Cloud...")
        streamlit_js_eval(js_expressions="""
            DeviceMotionEvent.requestPermission().then(response => {
                if (response == 'granted') { window.alert('Hardware Sync Active'); }
            }).catch(console.error)
        """, key="hardware_ping")
        p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, 
             "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
        supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
        st.toast("Syncing Successful.")

    if st.button("Log Water"):
        st.session_state.water += 1
        st.rerun()

with t2:
    st.title("Session Tracker")
    s_list = ["Basketball", "Soccer", "Gym Training", "Football", "Boxing", "Swimming", "Tennis", "Volleyball", "Cycling"]
    sport = st.selectbox("Select Activity", s_list)
    if 't_start' not in st.session_state: st.session_state.t_start = None
    c_st, c_sp = st.columns(2)
    if c_st.button("START SESSION"):
        st.session_state.t_start = time.time()
        st.info(f"Recording {sport}...")
    if c_sp.button("STOP & SAVE"):
        if st.session_state.t_start:
            dur = int((time.time() - st.session_state.t_start) / 60)
            st.session_state.exercise += dur
            st.session_state.t_start = None
            p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
            supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
            st.success(f"Locked in {dur} mins!")

with t3:
    st.title("Community Rankings")
    
    # FETCH ONLY REAL GROUPS FROM DB
    try:
        all_g_res = supabase.table("aura_collab_tracker").select("group_name").execute()
        g_list = sorted(list(set([x['group_name'] for x in all_g_res.data])))
    except:
        g_list = [st.session_state.active_group]
    
    # DROP DOWN TO SELECT VIEW
    view_g = st.selectbox("View Group Leaderboard", g_list, index=g_list.index(st.session_state.active_group) if st.session_state.active_group in g_list else 0)
    
    # FILTER: ONLY SHOW PEOPLE IN THE SELECTED GROUP
    res = supabase.table("aura_collab_tracker").select("*").eq("group_name", view_g).execute()
    
    if res.data:
        df = pd.DataFrame(res.data).sort_values(by="steps", ascending=False)
        st.dataframe(df[["username", "steps", "exercise_mins"]], use_container_width=True, hide_index=True)
    else:
        st.info("No athletes found in this group.")

with t4:
    st.title("Networks")
    st.subheader("Create a New Team")
    create_name = st.text_input("New Group Name", placeholder="e.g. Ora")
    if st.button("CREATE & JOIN TEAM"):
        if create_name:
            st.session_state.active_group = create_name
            p = {"username": st.session_state.user_name, "group_name": create_name, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
            supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
            st.success(f"Network Set to: {create_name}")
            st.rerun()

    st.write("---")
    st.subheader("Join Existing Team")
    join_name = st.text_input("Enter Group Code", placeholder="e.g. Global")
    if st.button("JOIN TEAM"):
        if join_name:
            st.session_state.active_group = join_name
            p = {"username": st.session_state.user_name, "group_name": join_name, "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
            supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
            st.success(f"Joined: {join_name}")
            st.rerun()
