import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import csv
import plotly.express as px
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
st.write('时间条')
time_now = st.slider('当前时间', 0, 40, value=0)
st.write('当前时间为',time_now)
stat=[]
#根据时间重新写入机床状态
with open('data\甘特图暂用.csv', 'r') as f:
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
stat_df.to_csv('data\甘特图暂用2.csv', index=False)
a1_width = 3
a2_width = 1
col_1, col_2 = st.columns((a1_width,a2_width))
with (col_1):
    #生成甘特图
    st.header('生产排程')
    fig, ax = plt.subplots()
    with open('data\甘特图暂用.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            start = int(row['startime'])
            end = int(row['endtime'])
            last = end-start
            if row['机床'] == '铣床':
                sthigh = 1
            if row['机床'] == '车床':
                sthigh = 2
            if row['机床'] == '钻床':
                sthigh = 3
            if end > time_now:
                start = max(start, time_now)
                ax.broken_barh([(start, last)], (int(row['sthigh'])*3, 1), facecolors=row['colorfull'], edgecolors='white', label = row['机床编号'])
    yticks = [3.5,6.5,9.5,12.5,15.5,18.5]
    yticklabels = ['x1','y1','z1','x2','y2','z2']
    xticks = [time_now,time_now+5,time_now+10,time_now+15,time_now+20,time_now+25,time_now+30]
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels, color='white')
    #ax.set_color('white')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks, color='white')
    ax.set_facecolor('#00172B')
    fig.set_facecolor('#00172B')
    ax.set_alpha(0.5)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel('时间/min',fontsize=10,color='white')
    plt.ylabel('机床编号',fontsize=10,color='white')
    #plt.grid(True)
    st.pyplot(fig)
   # reader2 = csv.reader(f)
     #绘制表格
    tab1, tab2 = st.tabs(['当前生产任务', '全部生产任务'])
    with tab1:
      dff = pd.read_csv('data\甘特图暂用2.csv')
      dff_timeselection = dff.query('endtime>@time_now & startime<@time_now')
      dff_timeselection2 = dff_timeselection.iloc[:, :8]
      st.dataframe(dff_timeselection2.head(), width=1000,height=300)
    with tab2:
        df2 = pd.read_csv('data\甘特图暂用2.csv')
        st.dataframe(df2, width=1000,height=300)
with col_2:
    #机床状态
    st.subheader('机床状态')
    container1 = st.container()
    with container1:
        col1, col2 = st.columns((1,1))
        with col1:
            st.markdown(' 铣床 _x1_<table><tr><td bgcolor=red>故障</td></tr></table>', unsafe_allow_html=True)
        with col2:
             st.markdown(' 钻床 _z1_<table><tr><td bgcolor=green>运行中</td></tr></table>', unsafe_allow_html=True)
    st.divider()
    container2 = st.container()
    with container2:
        col1, col2 = st.columns((1, 1))
        with col1:
            st.markdown(' 车床 _c1_<table><tr><td bgcolor=green>运行中</td></tr></table>', unsafe_allow_html=True)
        with col2:
            st.markdown(' 铣床 _x2_<table><tr><td bgcolor=grey>维修</td></tr></table>', unsafe_allow_html=True)
    st.divider()
    container3 = st.container()
    with container3:
        col1, col2 = st.columns((1, 1))
        with col1:
            st.markdown(' 钻床 _z2_<table><tr><td bgcolor=green>暂停</td></tr></table>', unsafe_allow_html=True)
        with col2:
            st.markdown(' 车床 _c2_<table><tr><td bgcolor=red>故障</td></tr></table>', unsafe_allow_html=True)
    st.write('\r\n')
    st.write('\r\n')
    st.write('\r\n')
    #生产数据部分
    st.subheader('任务进行情况')
    stat = []
    with open('data\甘特图暂用.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['endtime']) > time_now and int(row['startime']) < time_now:#int(row['endtime']) >= time_now and int(row['startime']) <= time_now
                k = [row['机床编号'], (time_now-int(row['startime']))/(int(row['endtime'])-int(row['startime']))]
                stat.append(k)
    stat_df = pd.DataFrame(stat)
    stat_df.to_csv('data\机床运行状态.csv',index=False)
    stat_now = pd.read_csv('data\机床运行状态.csv')
    stat_now.columns = ['机床编号', '任务进行情况/%']
    fig_bar = px.bar(stat_now, x='任务进行情况/%', y='机床编号',width=400, height=600)
    st.plotly_chart(fig_bar)