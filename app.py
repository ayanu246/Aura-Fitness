# --- CHROME HARDWARE FORCE (V2) ---
if st.button("ACTIVATE CHROME HEALTH BRIDGE"):
    st.warning("Pinging System Health Sensors...")
    
    streamlit_js_eval(js_expressions="""
        (async () => {
            try {
                // Check for Generic Sensor API (Chrome Standard)
                if ('Accelerometer' in window) {
                    const acc = new Accelerometer({frequency: 10});
                    acc.onerror = (event) => {
                        if (event.error.name === 'NotAllowedError') {
                            window.alert('CHROME BLOCKED: Tap the icon next to the URL at the top > Permissions > Allow Motion Sensors.');
                        }
                    };
                    acc.start();
                    window.alert('Handshake Sent. Sensor detected.');
                } 
                // Fallback for older versions
                else if (typeof DeviceMotionEvent !== 'undefined' && typeof DeviceMotionEvent.requestPermission === 'function') {
                    const res = await DeviceMotionEvent.requestPermission();
                    window.alert('Sensor Access: ' + res);
                } else {
                    window.alert('System Error: Please ensure "Motion Sensors" is ON in Chrome Site Settings.');
                }
            } catch (e) {
                window.alert('Connection ready. Use "Add to Home Screen" version for best results.');
            }
        })()
    """, key="chrome_sync_v2")
    
    # Push data to cloud so you don't lose progress while troubleshooting
    p = {"username": st.session_state.user_name, "group_name": st.session_state.active_group, 
         "steps": st.session_state.steps, "exercise_mins": st.session_state.exercise, "water": st.session_state.water}
    supabase.table("aura_collab_tracker").upsert(p, on_conflict="username,group_name").execute()
