import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import csv
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
st.write('时间条')
time_now = st.slider('当前时间', 0, 40, value=0)
st.write('当前时间为',time_now)
a1_width=3
a2_width=1
col_1,col_2=st.columns((a1_width,a2_width))
with col_1:
    st.header('生产排程')
    fig, ax = plt.subplots()
    with open('data/甘特图暂用.csv', 'r') as f:
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
                ax.broken_barh([(start, last)], (3*sthigh-1, 1), facecolors=row['colorfull'],edgecolors='k')
        st.pyplot(fig)
        reader2 = csv.reader(f)
    dff = pd.read_csv('data/甘特图暂用.csv', encoding='GBK')
    dff_timeselection = dff.query('endtime>@time_now')
    st.dataframe(dff_timeselection.head(), width=1000)
with col_2:
    st.title('机床状态')
    chosem=st.radio('界面选择',['甘特图','表格'])
    if chosem=='甘特图':
        da_data2 = pd.DataFrame(np.random.randn(10, 10), columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','j'])

        st.table(da_data2)
    else:
        da_data3=pd.DataFrame(np.random.randn(10, 12), columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','i','j','k','l'])
        st.write(da_data3)
    st.write('\r\n')
    st.write('\r\n')
    st.write('\r\n')
    st.title('生产数据')
    fig, ax = plt.subplots()
    x = np.linspace(0,10,100)
    y = np.sin(x)
    ax.plot(x, y)
    st.pyplot(fig)
    st.write('---')
    linchar_data=np.random.randn(10,1)