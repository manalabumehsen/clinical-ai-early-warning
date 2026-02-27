import streamlit as st

def show_dashboard():
    st.subheader("Dashboard Under Construction")
    st.write("Live vitals, risk score, and alerts will appear here.")

    # مثال لإضافة بعض الفيتالز الوهمية للعرض
    vitals = {
        "BP": "120 mmHg",
        "HR": "75 bpm",
        "SpO2": "97%",
        "UF rate": "200 mL"
    }
    
    st.markdown("### Current Vitals")
    for key, value in vitals.items():
        st.write(f"**{key}:** {value}")
