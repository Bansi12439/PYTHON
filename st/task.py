from numpy import random
import streamlit as st
st.sidebar.title("Stu info")
n=st.sidebar.text_input("Enter name")
bt=st.button("random")
if bt:
    num=random.randint(1,100)
    if num>50:
        st.image("download.jpeg")
    else:
        st.video("https://www.youtube.com/watch?v=Gyrf0HM1Z50&list=RDGyrf0HM1Z50&start_radio=1&pp=ygUOc29uZyBhbXBsaWZpZXKgBwE%3D")