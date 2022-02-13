"""
    実行方法
    $ python -m streamlit.cli run app.py
"""

import streamlit as st
import plotly.graph_objs as go

animals = ['カップラーメン', 'ボンカレー', 'ぱん']
populations = [45, 14, 32]

fig = go.Figure(data=[go.Bar(x=animals, y=populations)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "おれおれランチ",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Populations",
        title_standoff = 25),
    title ='サンプルです')

st.plotly_chart(fig, use_container_width=True)