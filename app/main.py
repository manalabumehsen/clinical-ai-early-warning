import streamlit as st
from app.dashboard import show_dashboard

st.set_page_config(page_title="Clinical AI Early Warning Platform", layout="wide")
st.title("💉 Clinical AI Early Warning Platform")

# Call dashboard
show_dashboard()
