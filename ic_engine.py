"""IC Engine Performance Calculator — Streamlit Community Cloud entry point."""

import math

import streamlit as st


def calculate_brake_power(speed_rpm: float, torque_nm: float) -> float:
    """Calculate brake power in kW from speed in rpm and torque in N·m."""
    return (2 * math.pi * speed_rpm * torque_nm) / 60_000


def calculate_indicated_power(brake_power_kw: float, friction_power_kw: float) -> float:
    """Calculate indicated power in kW: IP = BP + FP."""
    return brake_power_kw + friction_power_kw


def calculate_friction_power(indicated_power_kw: float, brake_power_kw: float) -> float:
    """Calculate friction power in kW: FP = IP - BP."""
    return indicated_power_kw - brake_power_kw


def calculate_mechanical_efficiency(brake_power_kw: float, indicated_power_kw: float) -> float:
    """Calculate mechanical efficiency as a percentage."""
    if indicated_power_kw <= 0:
        raise ValueError("Indicated power must be greater than zero.")
    return (brake_power_kw / indicated_power_kw) * 100


st.set_page_config(
    page_title="IC Engine Performance Calculator",
    page_icon="⚙️",
    layout="centered",
)

st.title("⚙️ IC Engine Performance Calculator")
st.write("Calculate brake power, indicated power, friction power, and mechanical efficiency.")

calculation = st.radio(
    "Select calculation",
    ["Brake Power", "Indicated Power", "Friction Power", "Mechanical Efficiency"],
    horizontal=True,
)

if calculation == "Brake Power":
    st.subheader("Brake Power")
    st.info("Formula: BP = 2πNT / 60,000")
    speed = st.number_input("Engine speed (rpm)", min_value=0.0, value=1500.0, step=100.0)
    torque = st.number_input("Brake torque (N·m)", min_value=0.0, value=100.0, step=1.0)

    if st.button("Calculate Brake Power", use_container_width=True):
        brake_power = calculate_brake_power(speed, torque)
        st.success(f"Brake Power = {brake_power:.3f} kW")

elif calculation == "Indicated Power":
    st.subheader("Indicated Power")
    st.info("Formula: IP = BP + FP")
    brake_power = st.number_input("Brake power (kW)", min_value=0.0, value=20.0, step=0.1)
    friction_power = st.number_input("Friction power (kW)", min_value=0.0, value=5.0, step=0.1)

    if st.button("Calculate Indicated Power", use_container_width=True):
        indicated_power = calculate_indicated_power(brake_power, friction_power)
        st.success(f"Indicated Power = {indicated_power:.3f} kW")

elif calculation == "Friction Power":
    st.subheader("Friction Power")
    st.info("Formula: FP = IP − BP")
    indicated_power = st.number_input("Indicated power (kW)", min_value=0.0, value=25.0, step=0.1)
    brake_power = st.number_input("Brake power (kW)", min_value=0.0, value=20.0, step=0.1)

    if st.button("Calculate Friction Power", use_container_width=True):
        if brake_power > indicated_power:
            st.error("Brake power cannot exceed indicated power.")
        else:
            friction_power = calculate_friction_power(indicated_power, brake_power)
            st.success(f"Friction Power = {friction_power:.3f} kW")

else:
    st.subheader("Mechanical Efficiency")
    st.info("Formula: Mechanical efficiency = (BP / IP) × 100")
    indicated_power = st.number_input("Indicated power (kW)", min_value=0.0, value=25.0, step=0.1)
    brake_power = st.number_input("Brake power (kW)", min_value=0.0, value=20.0, step=0.1)

    if st.button("Calculate Mechanical Efficiency", use_container_width=True):
        if indicated_power <= 0:
            st.error("Indicated power must be greater than zero.")
        elif brake_power > indicated_power:
            st.error("Brake power cannot exceed indicated power.")
        else:
            efficiency = calculate_mechanical_efficiency(brake_power, indicated_power)
            st.success(f"Mechanical Efficiency = {efficiency:.2f}%")

st.divider()
st.caption("All power values are in kilowatts (kW).")
