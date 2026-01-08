import streamlit as st
st.title("Project")
st.sidebar.title("Sidebar")
m=st.sidebar.selectbox("Batch",["B4","B5","B6"])
ge=st.sidebar.radio("Select gender",["male","female"])
sub=st.sidebar.selectbox("SUBJECT",["Python","FSD"])
if sub=='Python':
    choose=st.title("Welcome python world")
    en=st.number_input("Enter your enroll number ",min_value=2400217121)
    pn=st.text_input("Enter project Name ")
    pd=st.text_area("Enter project descripition ")
else:
    choose1=st.title("Welcome FSD world")
    en1=st.number_input("Enter your enroll number ")
    pn1=st.text_input("Enter project Name ")
    pd1=st.text_area("Enter project descripition ")

bt=st.button("submit")
m={"name":["bansi","AB","CD"],"AGE":[18,20,21]}
st.table(m)