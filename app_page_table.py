import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# plot the data in the table this is static table cannot be changed
st.table(df)