import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
if st.button("Submit"):
    x=st.progress(0)
    with st.spinner("Loading........"):
        for i in range(100):
            import time
            time.sleep(0.02)
            x.progress(i+1)
    st.info("Submitted")
m={"name":["bansi","AB","CD"],"AGE":[18,20,21]}
st.table(m)
st.dataframe(m)
st.json(m)
h=st.file_uploader("Upload ph",type=["png","jpeg"])
if st.button("submit"):
    st.image(h)
d=st.download_button("download csv",data=h)
x=["A","B","C","D"]
y=[10,55,20,32]
# plt.plot(x,y)
# st.pyplot(plt)
# plt.clf()
# plt.bar(x,y)
# st.pyplot(plt)

z=np.column_stack((x,y))
st.line_chart(z)
st.area_chart(z)

d=np.arange(1,11)
y1=np.random.randint(1,101,10)
z1=np.column_stack((d,y1))
st.bar_chart(z1)

# bold
st.markdown("**Student**") 
# for italic
st.markdown("*dsffggh*")
# for header
st.markdown("# fdgdgh")
