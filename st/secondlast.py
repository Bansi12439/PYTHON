import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import random

st.sidebar.title("Sidebar")
m=st.sidebar.selectbox("Batch",["B4","B5","B6"])
ge=st.sidebar.radio("Select gender",["male","female"])
sub=st.sidebar.selectbox("SUBJECT",["Python","FSD","Chart"])
t1,t2,t3=st.tabs(["python","fsd","charts"])


with t3:
    choose2=st.title("CHARTS")
    d=np.arange(1,11)
    y1=np.random.randint(1,101,10)
    z1=np.column_stack((d,y1))
    st.bar_chart(z1)
    
with t1:
   
            choose=st.title("Welcome python world")
            en=st.number_input("Enter your enroll number ",min_value=2400217121)
            pn=st.text_input("Enter project Name ")
            pd=st.text_area("Enter project descripition ")
with t2:
    if sub=='FSD':
        choose1=st.title("Welcome FSD world")
        en1=st.number_input("Enter your enroll number ")
        pn1=st.text_input("Enter project Name ")
        pd1=st.text_area("Enter project descripition ")



