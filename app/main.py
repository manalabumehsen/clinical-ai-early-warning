import streamlit as st
from dashboard import show_dashboard 

# إعداد الصفحة
st.set_page_config(page_title="Clinical AI Early Warning Platform", layout="wide")
st.title("💉 Clinical AI Early Warning Platform")

# استدعاء الداشبورد
show_dashboard()
