import streamlit as st
import time

st.title("Chương trình nhập thông tin học sinh")

name = st.text_input("Nhập tên")
age = st.text_input("Nhập tuổi")
school = st.text_input("Nhập trường")

if st.button("Submit"):
    bar = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        bar.progress(i + 1)

    st.write("Tên:", name)
    st.write("Tuổi:", age)
    st.write("Trường:", school)

    st.balloons()

