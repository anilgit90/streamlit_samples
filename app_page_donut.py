import streamlit as st
import pandas as pd
import plotly.express as px

# Read the data from CSV
data = pd.read_csv("D:/avocado.csv")

# Header for the Page
st.header("Donut Chart")

# Configure the Donut Chart
donut_chart = px.pie(
    names = data.type,
    values = data.AveragePrice,
    hole = 0.40
)

# Plot the Donut Chart
st.plotly_chart(donut_chart)