import streamlit as st

# session loses it value on browser refresh
st.title('Counter Example')

if 'count' not in st.session_state:
    st.session_state['count'] = 0

increment_value = st.number_input('Enter a value',value=0,step=1)

def increment_counter():
    st.session_state['count'] += 1

# Using callback function and argument
st.button('Increment',on_click=increment_counter(), args = (increment_value,))

st.write('Count = ',st.session_state['count'])