import streamlit as st

# Title
st.title("🌡️ Temperature Converter")

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

# Input fields
temperature = st.number_input("Enter Temperature", value=0.0)
unit = st.selectbox("Select Unit", ["Celsius", "Fahrenheit"])

# Convert function
def convert_temperature(temp, unit):
    if unit == "Celsius":
        converted = (temp * 9/5) + 32
        return round(converted, 2), "Fahrenheit"
    else:
        converted = (temp - 32) * 5/9
        return round(converted, 2), "Celsius"

# Button to trigger conversion
if st.button("Convert"):
    result, target_unit = convert_temperature(temperature, unit)
    st.success(f"{temperature}°{unit[0]} = {result}°{target_unit[0]}")

    # Store in history
    st.session_state.history.insert(0, f"{temperature}°{unit[0]} → {result}°{target_unit[0]}")

# Show history
if st.session_state.history:
    st.subheader("🕓 Conversion History")
    for record in st.session_state.history:
        st.write(record)
