import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')
val1 = st.slider('valeur 1', 0, 5, 3)

val2 = st.slider('valeur 2', 0, 50, 20)

chart_data = pd.DataFrame(
     np.random.randn(val2, val1),
     columns=['a', 'b', 'c'])

chart_data

st.line_chart(chart_data)
