import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Simple Streamlit App')

data = pd.DataFrame({
    'x': range(10),
    'y': [2*i for i in range(10)]
})

st.line_chart(data)
