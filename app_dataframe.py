"""
# My First Pandas dataframe File
"""
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

# Pass the dataframe streamlit will render the same magic rendering
df