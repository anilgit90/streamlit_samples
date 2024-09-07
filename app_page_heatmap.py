import altair as alt
import streamlit as st 
import pandas as pd

# Read CSV
df = pd.read_csv("D:/albany.csv")

# Configure Heat Map
heat_map = alt.Chart(df).mark_rect().encode(
    alt.Y('AveragePrice:Q'),
    alt.X('Large Bags:Q'),
    alt.Color('AveragePrice:Q'),
    tooltip=['AveragePrice','type','Large Bags','Date']
).interactive()

# Plot the Chart using altair
st.altair_chart(heat_map)