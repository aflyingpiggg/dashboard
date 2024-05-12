import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import csv
import plotly.express as px

# -*- coding:utf-8 -*-
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
st.write('时间条')
time_now = st.slider('当前时间', 0, 40, value=0)
st.write('当前时间为',time_now)
stat=[]
#根据时间重新写入机床状态
with open('data/甘特图暂用.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['endtime']) < time_now:
                row['状态'] = '已完成'
        elif int(row['startime']) > time_now:
                row['状态'] = '未完成'
        else:
                row['状态'] = '进行中'
        stat.append(row)
stat_df = pd.DataFrame(stat)
stat_df.to_csv('data/甘特图暂用2.csv', index=False)
st.title('生产数据')
a1_width = 3
a2_width = 1
a3_width = 3
col_1, col_2= st.columns((a1_width,a2_width))
with col_1:
    container = st.container()
    with container:
        col1, col2= st.columns((2,3))
        df = pd.read_csv('data/甘特图暂用2.csv')
        df_timeselection = df.iloc[:, :8]
        df_now = df_timeselection.query('startime < @time_now & endtime > @time_now')
        with col1:
            st.header('当前任务')
            st.dataframe(df_now,height=300)
        with col2:
            st.header('机床生产状况')
            st.dataframe(df_timeselection, height=300)
    st.subheader('近30天机床启动比例')
    with open('data/启动比.csv', 'r') as f:
        reader = csv.DictReader(f)
        fig_bar2 = px.bar(reader, x='机床编号', y='比例', width=700, height=300)
        st.plotly_chart(fig_bar2)

with col_2:
    st.subheader('任务进行情况')
    stat = []
    with open('data/甘特图暂用.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['endtime']) > time_now and int(row['startime']) < time_now:#int(row['endtime']) >= time_now and int(row['startime']) <= time_now
                k = [row['机床编号'], (time_now-int(row['startime']))/(int(row['endtime'])-int(row['startime']))]
                stat.append(k)
    stat_df = pd.DataFrame(stat)
    stat_df.to_csv('data/机床运行状态.csv',index=False)
    stat_now = pd.read_csv('data/机床运行状态.csv')
    stat_now.columns=['机床编号', '任务进行情况/%']
    fig_bar = px.bar(stat_now, x='任务进行情况/%', y='机床编号',width=400, height=600)
    st.plotly_chart(fig_bar)
st.divider()
