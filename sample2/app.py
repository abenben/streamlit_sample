import streamlit as st
import numpy as np
import pandas as pd

locale = {"東京": [35.68, 139.76], "大阪": [34.70, 135.49]}

l = st.selectbox(
    'Which places do you like best?',
    ("東京", "大阪"))
'You selected:', l

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + locale[l],
    columns=['lat', 'lon'])
st.map(map_data)

if st.checkbox('Show dataframe'):
    st.write(map_data)
