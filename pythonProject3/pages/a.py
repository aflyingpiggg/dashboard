import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import csv
import plotly.express as px
df = pd.read_csv('data/����״̬.csv', encoding='utf-8')
pie_chart = px.pie(df,
                   title='������ʷ״̬ռ��',
                   values='ʱ��',
                   names='״̬',
                   height=500,
                   width=400,
                   )
st.plotly_chart(pie_chart)
st.divider()
# ά������,��֪����ɶ
st.title('ά������')