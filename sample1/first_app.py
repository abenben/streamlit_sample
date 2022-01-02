import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello World")
st.subheader("This is subheader")
st.write("This is testdata")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
print("test")
