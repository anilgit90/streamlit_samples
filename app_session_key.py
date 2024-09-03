import streamlit as st

st.text_input("Your Name",key="name")
# the key name is stored in the current session, will be deteled after refresh
st.session_state.name