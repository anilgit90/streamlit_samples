import streamlit as st
import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("D:/avocado.csv")

st.header("Pie chart")

pie_chart = go.Figure(
    go.Pie(
        labels = data.type,
        values = data.AveragePrice,
        hoverinfo="label+percent",
        textinfo="value+percent"
    )
)

st.plotly_chart(pie_chart)