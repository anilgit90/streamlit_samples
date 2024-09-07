import pandas as pd
import numpy as np
import altair as alt
import streamlit as st


df = pd.DataFrame(
    np.random.randn(10,2),
    columns=['a','b']
)

chart = alt.Chart(df).mark_bar().encode(x='a',y='b',tooltip=['a','b'])

st.write(chart)