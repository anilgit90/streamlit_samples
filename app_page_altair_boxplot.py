import altair as alt
import streamlit as st
import pandas as pd

# Read the data from csv
df = pd.read_csv("D:/albany.csv")

# Configure the box plot
box_plot = alt.Chart(df).mark_boxplot().encode(
    x = "Date",
    y = "Large Bags"
)
# plot the chart
st.altair_chart(box_plot)