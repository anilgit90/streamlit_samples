import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import seaborn as sns

df = pd.read_csv("D:/avocado.csv")

fig = plt.figure(figsize=(10,5))
# Color differenciation is not there
sns.countplot(x = "year",data= df)
st.pyplot(fig)