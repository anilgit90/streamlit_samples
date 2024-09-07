import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/avocado.csv")

fig = plt.figure(figsize=(10,5))
# Strip Plot
sns.stripplot(x = "year",y="AveragePrice", data = df)
st.pyplot(fig)