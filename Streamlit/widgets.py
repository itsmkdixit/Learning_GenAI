import streamlit as st
import pandas as pd

st.title("Streamlit Text input")

#Input Block
name = st.text_input("Enter your name:")

#Slider block
age = st.slider("Select your age:", 0,120,18)

st.write(f"Your age is {age}.") 

#Dropdown or Select Box
gender = ["Male", "Female", "Trans", "Prefer not to say"]
choice = st.selectbox("Select your Gender:", gender)
st.write(f"Gender: {choice}")

if name:
    st.write(f"Welcome to Streamlit, {name}")


#Dataframe
data = {
    "Name" : ["Mayank", "Ruchi", "Shashank", "Rishu"],
    "Age" : [32,33,28,30],
    "City" : ["Bangalore", "Pune", "Delhi", "Kolkata"]
}

df = pd.DataFrame(data)
st.write(df)

#Upload files

uploaded_file = st.file_uploader("Choose a CSV file", type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)