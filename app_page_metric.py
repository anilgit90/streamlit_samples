import streamlit as st

# Label Chart name,value is value, delta is change in value, positive is green, negative is red
st.metric(label="Temperature",value="31C",delta="-1.2C")