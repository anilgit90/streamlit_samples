import streamlit as st

st.page_link("app_page_multi.py", label="Home", icon="🏠")
st.page_link("pages/app_dataframe2.py", label="Page 1", icon="1️⃣")
st.page_link("pages/app_dataframe3.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")