import streamlit as st
import joblib
model = joblib.load('My_model.pkl')
st.title("Student pass/Fail Prediction")
st.write("Enter Your Marks")

marks = st.number_input("Enter your marks:",min_value = 0, max_value = 100)

if st.button("Predict"):
    result = model.predict([[marks]])
    if result[0] == 1:
        st.success("You are pass")
    else : 
        st.error("Sorry You are fail")

