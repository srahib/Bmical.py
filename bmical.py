import streamlit as st
import time

st.set_page_config(page_title = "BMI CALCULATOR",)
st.title("BMI CALCULATOR")
st.markdown(""""
## apna body mass index (bmi) calculate kren nechay apna **weight and height** enter kren""")

col1 , col2 = st.columns(2)
with col1:
    weight= st.number_input("weight (kg): ", min_value=1.0,format="%.2f")
with col2:
    height = st.number_input("height (m): ", min_value=1.0,format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.subheader("Apka BMI hai:")
    st.markdown(f"{bmi:.2f}", unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("under weight")
    elif 18.5  <= bmi < 24.9:
        st.success("Normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("Over weight")
    else:
        st.error("Obsity")
else:
    st.info("Please Enter a valid weight and height")                  

st.markdown("<div style='text-align: center;'>Created by  Rahib Siddiqui </div>", unsafe_allow_html=True)