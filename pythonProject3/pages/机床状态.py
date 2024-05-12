import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import csv
import random
import plotly.express as px
st.write('时间条')
time_now = st.slider('当前时间', 0, 40, value=0)
st.write('当前时间为',time_now)
dff = pd.read_csv('data/甘特图暂用.csv', encoding='GBK')
sex = st.selectbox(label='机床编号', options=(dff['机床编号'].unique()))
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
stat_df_select = stat_df.query('机床编号 == @sex')
stat_df.to_csv('data/甘特图暂用2.csv', index=False)
stat_df_select.to_csv('data/甘特图暂用3.csv', index=False)
b1_width = 3
b2_width = 2
b3_width = 1
coll_1, coll_2= st.columns((b1_width, b2_width))
with coll_1:
    st.title(f'机床编号 {sex}')
    dff = pd.read_csv('data/甘特图暂用3.csv')
    dff_timeselection = dff.query('机床编号 == @sex')
    dff_timeselection2 = dff_timeselection.iloc[:, :8]
    #s随机产生机床状态
    #nam = ['运行', '暂停', '异常', '离线']
    ran = random.randint(1,100)
    with open('data/甘特图暂用.csv', 'r') as f:
         reader = csv.DictReader(f)
         for row in reader:
          if ran <=95:
            if row['机床编号'] == sex:
                #st.write(int(row['startime']), time_now, int(row['endtime']))
                if int(row['startime']) <= time_now and int(row['endtime']) >= time_now:
                   nam=1
                 #  st.write(row['加工任务'])
                   break
                else:
                   nam = 2
          elif ran>97:
            nam = 3
          else:
            nam = 4
    st.header(f"机床 _{sex}_ 状态:")
    st.divider()
    container1 = st.container()
    with container1:
        col1,col2,col3,col4=st.columns(4)
        with col1:
            if nam == 1:
               st.markdown('<table><tr><td bgcolor=green>运行中</td></tr></table>', unsafe_allow_html=True)
            else:
               st.markdown('<table><tr><td bgcolor=grey>运行中</td></tr></table>', unsafe_allow_html=True)
        with col2:
            if nam == 2:
                st.markdown('<table><tr><td bgcolor=green>暂停</td></tr></table>', unsafe_allow_html=True)
            else:
                st.markdown('<table><tr><td bgcolor=grey>暂停</td></tr></table>', unsafe_allow_html=True)
        with col3:
            if nam == 3:
                st.markdown('<table><tr><td bgcolor=red>故障</td></tr></table>', unsafe_allow_html=True)
            else:
                st.markdown('<table><tr><td bgcolor=grey>故障</td></tr></table>', unsafe_allow_html=True)
        with col4:
            if nam == 4:
                st.markdown('<table><tr><td bgcolor=blue>维修</td></tr></table>', unsafe_allow_html=True)
            else:
                st.markdown('<table><tr><td bgcolor=grey>维修</td></tr></table>', unsafe_allow_html=True)
    st.divider()
    st.dataframe(dff_timeselection2, width=1000,height=500)
with coll_2:
    #状态占比图
    df = pd.read_csv('data/机床状态.csv', encoding='GBK')
    pie_chart = px.pie(df,
                       title=f'机床{sex}历史状态占比',
                       values='时间',
                       names='状态',
                       height=500,
                       width=400,
                       )
    st.plotly_chart(pie_chart)
    st.divider()
    #维修提醒,不知道放啥
    st.title('维修提醒')
    if nam <=2:
      container2 = st.container()
      with container2:
          colll1,colll2 = st.columns(2)
          with colll1:
             st.markdown(f'机床 _{sex}_ 已经连续工作')
          with colll2:
              i = random.randint(1,100)
              if i<=70:
                 st.markdown(f'<table><tr><td bgcolor=green>{i} 小时</td></tr></table>', unsafe_allow_html=True)
              else:
                 st.markdown(f'<table><tr><td bgcolor=red>{i} 小时</td></tr></table>', unsafe_allow_html=True)
      st.divider()
      container3 = st.container()
      with container3:
          col11,col22 = st.columns(2)
          with col11:
              st.markdown('距离上次检修已过')
          with col22:
              j=random.randint(1,100)
              if j<=70:
                  st.markdown(f'<table><tr><td bgcolor=green>{i} 小时</td></tr></table>', unsafe_allow_html=True)
              else:
                  st.markdown(f'<table><tr><td bgcolor=red>{i} 小时</td></tr></table>', unsafe_allow_html=True)
    if nam ==3:
      st.divider()
      st.markdown('<table><tr><td bgcolor=red>设备故障</td></tr></table>', unsafe_allow_html=True)
    if nam ==4:
        st.divider()
        st.markdown('<table><tr><td bgcolor=grey>设备离线</td></tr></table>', unsafe_allow_html=True)