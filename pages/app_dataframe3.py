import streamlit as st
import pandas as pd
import numpy as np

# Dataframe using random values
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' %i for i in range(10))
)

# highlight minimum value for the column
st.dataframe(df.style.highlight_min(axis=0))