import altair as alt
import streamlit as st
import pandas as pd

df = pd.read_csv("D:/albany.csv")

area = alt.Chart(df).mark_area(color="orange").encode(
    x = "Date",
    y = "Large Bags"
)

st.altair_chart(area)