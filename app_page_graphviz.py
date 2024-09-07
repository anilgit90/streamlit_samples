import streamlit as st
import graphviz as graphviz

st.title('GraphViz')

# Working 
graph = graphviz.Digraph()
graph.edge('Training data','ML algorithm')
graph.edge('ML algorithm','Model')
graph.edge('Model','Result Forecasting')
graph.edge('New Data','Model')
st.graphviz_chart(graph)

# Not working
#st.graphviz_chart('''
#    digraph {
#        "Training Data" -> "ML Algorithm"
#        "ML Algorithm -> "Model"
#        "Model" -> "Result Forecasting"
#        "New Data" -> "Model"
#    }
#''')