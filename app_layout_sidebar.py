import streamlit as st

# Sidebar of the browser, collapsable
add_selectionbox = st.sidebar.selectbox(
    'How would you like to contacted?',
    ('Email','Home Phone','Mobile Phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0,100.0,(25.0,75.0)
)
