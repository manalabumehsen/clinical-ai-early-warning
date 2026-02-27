import streamlit as st
from dashboard import show_dashboard  # بدون "app."

st.set_page_config(page_title="Clinical AI Early Warning Platform", layout="wide")
st.title("💉 Clinical AI Early Warning Platform")

show_dashboard()
