# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:41:45 2021

@author: hteh
"""

import streamlit as st,pandas as pd,numpy as np,os,pickle


st.title('Henry Testing')
st.subheader('Raw data')
data=pd.read_csv('vc1902_inline.csv').dropna(axis=1,thresh=30000).head(200)
st.write(data)
