import streamlit as st
import calculations as calc

st.set_page_config(page_title="DF Properties Calculator", page_icon="🔬", layout="wide")

st.title("Drilling Fluid Properties Calculator")
st.markdown("Enter the mud and rheology measurements below to calculate fluid properties.")
# input sec
st.header("1. Input Data")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Mud Weight (MW)")
    mw_value = st.number_input("Mud Weight Value", min_value=0.0, step=0.1)
    mw_unit = st.selectbox("Unit", ["PPG", "SG", "lb/ft³", "kg/m³", "psi/1000ft"])
with col2:
    st.subheader("Fann Viscometer Dial Readings")
    theta_600 = st.number_input("600 RPM Reading (\u03b8\u2086\u2080\u2080)", min_value=0.0, step=0.5)
    theta_300 = st.number_input("300 RPM Reading (\u03b8\u2083\u2080\u2080)", min_value=0.0, step=0.5)
    
    st.subheader("Gel Strength Readings")
    gel_10s = st.number_input("10-Second Gel Strength (lb/100 ft²)", min_value=0.0, step=1.0)
    gel_10m = st.number_input("10-Minute Gel Strength (lb/100 ft²)", min_value=0.0, step=1.0)
# calculations & output sec
st.markdown("---")
st.header("2. Calculated Properties")
# Convert Mud Weight
mw_conversions = calc.convert_mw(mw_value, mw_unit)
mw_ppg = mw_conversions['PPG']
# Calculate Rheology
pv = calc.calculate_pv(theta_600, theta_300)
av = calc.calculate_av(theta_600)
yp = calc.calculate_yp(theta_300, pv)
ti = calc.calculate_ti(yp, pv)
n = calc.calculate_n(theta_600, theta_300)
k = calc.calculate_k(theta_300, n)
# Calculate Buoyancy Factor
bf = calc.calculate_bf(mw_ppg)
# Display Mud Weight conversions 
st.subheader("Mud Weight Conversions")
mw_df = {
    "Unit": list(mw_conversions.keys()),
    "Value": [f"{v:.3f}" for v in mw_conversions.values()]
}
st.table(mw_df)
# Display Rheological Properties
st.subheader("Rheological & Gel Properties")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric("Plastic Viscosity (PV)", f"{pv:.1f} cP")
    st.metric("Flow Index (n)", f"{n:.3f}")
with col_b:
    st.metric("Apparent Viscosity (AV)", f"{av:.1f} cP")
    st.metric("Consistency Index (k)", f"{k:.3f} lb\u00b7s\u207f/100 ft\u00b2")
with col_c:
    st.metric("Yield Point (YP)", f"{yp:.1f} lb/100 ft\u00b2")
    st.metric("Transport Index (TI)", f"{ti:.3f}")
# Display Gel Strengths
st.markdown("**Gel Strengths entered**:")
st.write(f"- 10-Second Gel: {gel_10s} lb/100 ft²")
st.write(f"- 10-Minute Gel: {gel_10m} lb/100 ft²")
# Display Buoyancy Factor
st.markdown("---")
st.subheader("Buoyancy Factor (BF)")
st.write(f"The buoyancy factor for this mud weight is: **{bf:.3f}**")