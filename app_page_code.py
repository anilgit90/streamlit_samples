import streamlit as st

st.subheader("""Python Code""")
code = '''def hello():
            print("Hello, Streamlit!")'''
st.code(code,language='python')