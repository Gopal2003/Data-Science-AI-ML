import streamlit as st

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")

age = st.slider("Select your age: ",0,100,22)
st.write(f"Your age, {age}")

if name:
    st.write(f"Hello, {name}")