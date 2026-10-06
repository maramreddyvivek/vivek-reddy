"""Streamlit web application for IC engine performance calculations."""

import streamlit as st

from ic_engine_performance_calculator import (
    calculate_brake_power,
    calculate_friction_power,
    calculate_indicated_power,
    calculate_mechanical_efficiency,
)


st.set_page_config(page_title="IC Engine Performance Calculator", page_icon="⚙️")

st.title("⚙️ IC Engine Performance Calculator")
st.write("Calculate the main performance values of an internal-combustion engine.")

calculation = st.selectbox(
    "Select a calculation",
    (
        "Brake Power",
        "Indicated Power",
        "Friction Power",
        "Mechanical Efficiency",
    ),
)

if calculation == "Brake Power":
    st.subheader("Brake Power")
    st.caption("BP = 2πNT / 60,000")
    speed = st.number_input("Engine speed (rpm)", min_value=0.0, value=1500.0, step=100.0)
    torque = st.number_input("Brake torque (N·m)", min_value=0.0, value=100.0, step=1.0)

    if st.button("Calculate brake power"):
        result = calculate_brake_power(speed, torque)
        st.metric("Brake power", f"{result:.3f} kW")

elif calculation == "Indicated Power":
    st.subheader("Indicated Power")
    st.caption("IP = BP + FP")
    brake_power = st.number_input("Brake power (kW)", min_value=0.0, value=20.0, step=0.1)
    friction_power = st.number_input("Friction power (kW)", min_value=0.0, value=5.0, step=0.1)

    if st.button("Calculate indicated power"):
        result = calculate_indicated_power(brake_power, friction_power)
        st.metric("Indicated power", f"{result:.3f} kW")

elif calculation == "Friction Power":
    st.subheader("Friction Power")
    st.caption("FP = IP − BP")
    indicated_power = st.number_input("Indicated power (kW)", min_value=0.0, value=25.0, step=0.1)
    brake_power = st.number_input("Brake power (kW)", min_value=0.0, value=20.0, step=0.1)

    if st.button("Calculate friction power"):
        if brake_power > indicated_power:
            st.error("Brake power cannot exceed indicated power.")
        else:
            result = calculate_friction_power(indicated_power, brake_power)
            st.metric("Friction power", f"{result:.3f} kW")

else:
    st.subheader("Mechanical Efficiency")
    st.caption("Mechanical efficiency = (BP / IP) × 100")
    indicated_power = st.number_input("Indicated power (kW)", min_value=0.0, value=25.0, step=0.1)
    brake_power = st.number_input("Brake power (kW)", min_value=0.0, value=20.0, step=0.1)

    if st.button("Calculate mechanical efficiency"):
        if indicated_power == 0:
            st.error("Indicated power must be greater than zero.")
        elif brake_power > indicated_power:
            st.error("Brake power cannot exceed indicated power.")
        else:
            result = calculate_mechanical_efficiency(brake_power, indicated_power)
            st.metric("Mechanical efficiency", f"{result:.2f}%")

st.divider()
st.caption("All power values are displayed in kilowatts (kW).")
