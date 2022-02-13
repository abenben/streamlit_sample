"""
    実行方法
    $ python -m streamlit.cli run first_app.py
"""

import streamlit as st
import pandas as pd

st.title("Hello World")
st.subheader("This is subheader")
st.write("This is testdata")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4, 5, 6],
    'second column': [10, 20, 30, 40, 50, 60]
}))
