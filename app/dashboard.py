import streamlit as st
import plotly.graph_objects as go
import time

# -----------------------------
# سيناريوهات جاهزة
scenarios = {
    "Normal BP, Normal Flow": {"blood_pressure": 120, "flow_speed": 5, "uf_rate": 200},
    "High BP, Fast Flow": {"blood_pressure": 160, "flow_speed": 8, "uf_rate": 300},
    "Low BP, Slow Flow": {"blood_pressure": 90, "flow_speed": 3, "uf_rate": 100},
    "High Fluids, Moderate Flow": {"blood_pressure": 140, "flow_speed": 6, "uf_rate": 400}
}

# -----------------------------
# مؤقت الحركة
if 't' not in st.session_state:
    st.session_state.t = 0
if 'running' not in st.session_state:
    st.session_state.running = True

# -----------------------------
# واجهة تفاعلية
selected_scenario = st.selectbox("Select Patient Profile", list(scenarios.keys()))
scenario = scenarios[selected_scenario]

col1, col2, col3 = st.columns(3)
if col1.button("▶️ Start"):
    st.session_state.running = True
if col2.button("⏸ Stop"):
    st.session_state.running = False
if col3.button("🔄 Reset"):
    st.session_state.t = 0

# -----------------------------
# عرض Risk Status حسب السيناريو
bp = scenario["blood_pressure"]
uf = scenario["uf_rate"]
if bp > 150 or uf > 350:
    risk = "High 🔴"
elif bp < 100 or uf < 150:
    risk = "Low 🟢"
else:
    risk = "Medium 🟡"

st.markdown(f"**Patient Risk Status:** {risk}")
st.markdown(f"**Current Vitals:** BP: {bp} mmHg | UF rate: {uf} mL | Flow: {scenario['flow_speed']}")

# -----------------------------
# رسم حركة الدم
num_pipes = 4
num_points = 10
pipe_length = 100
placeholder = st.empty()

if st.session_state.running:
    fig = go.Figure()
    for i in range(num_pipes):
        y = i * 5
        # رسم الأنبوب
        fig.add_trace(go.Scatter(
            x=[0, pipe_length], y=[y, y],
            mode='lines', line=dict(color='black', width=12),
            showlegend=False
        ))
        # حركة الدم (نقاط حمراء)
        positions = [(p + st.session_state.t * scenario["flow_speed"]) % pipe_length for p in range(0, pipe_length, pipe_length // num_points)]
        fig.add_trace(go.Scatter(
            x=positions, y=[y]*len(positions),
            mode='markers', marker=dict(color='red', size=15),
            showlegend=False
        ))
        # المضخة على أول أنبوب
        if i == 0:
            fig.add_trace(go.Scatter(
                x=[5], y=[y],
                mode='markers+text',
                marker=dict(color='blue', size=25),
                text=["Pump"], textposition="top center",
                showlegend=False
            ))
    fig.update_layout(
        xaxis=dict(range=[0, pipe_length], visible=False),
        yaxis=dict(range=[-5, num_pipes*5], visible=False),
        height=250
    )
    placeholder.plotly_chart(fig, use_container_width=True)
    st.session_state.t += 1
