import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import csv
import plotly.express as px
df = pd.read_csv('data/机床状态.csv', encoding='utf-8')
pie_chart = px.pie(df,
                   title='机床历史状态占比',
                   values='时间',
                   names='状态',
                   height=500,
                   width=400,
                   )
st.plotly_chart(pie_chart)
st.divider()
# 维修提醒,不知道放啥
st.title('维修提醒')