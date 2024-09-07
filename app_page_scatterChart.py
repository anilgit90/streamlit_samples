import streamlit as st
import pandas as pd
import plotly.express as px

# Read the data from CSV
data = pd.read_csv("D:/avocado.csv")

# Header for the Page
st.header("Scatter Chart")

# Configure the Scatter Chart
scat = px.scatter(
    x = data.Date,
    y = data.AveragePrice
)

# Plot the Scatter Chart
st.plotly_chart(scat)