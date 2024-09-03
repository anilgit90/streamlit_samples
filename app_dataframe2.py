import streamlit as st
import numpy as np

dataframe = np.random.randn(10,20)
# draws a interactive chart that can be used to search and interact with.
st.dataframe(dataframe)