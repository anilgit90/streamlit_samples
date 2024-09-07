import streamlit as st

# Initialize columns 
c1, c2, c3 = st.columns(3)

# Set Metric
c1.metric("Rainfall","100cm","10cm")
c2.metric(label = "Population",value="123 Billons",delta="1 Billions",delta_color="inverse")
c3.metric(label = "Customers",value=100,delta=10,delta_color="off")

st.metric(label="Speed",value=None,delta=0)
st.metric("Trees","91456","-1132649")
