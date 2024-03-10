import streamlit as st

st.title("Registration Form")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type="password")
gender = st.radio("Select your gender", ("Male", "Female", "Other"))
country = st.selectbox("Select Country", ["India", "China", "USA", "UK", "Nepal", "Bhutan"])
age = st.slider("Enter your age", min_value=18, max_value=50)
st.write("Age : {}".format(age))
