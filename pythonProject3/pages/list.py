import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import csv
import plotly.express as px
df = pd.read_csv('data/工作簿3.csv', encoding='GBK')
x = df['速度比例增益']
y = (df['速度波动范围'])
st.write(x)
st.write(y)
plt.scatter(x, y, color='red')
p = np.polyfit(x, y, 9)
st.write(p)
func = np.poly1d(p)
x_dict = np.linspace(x.min(), x.max(), 100)
y_dict = func(x_dict)
plt.plot(x_dict, y_dict)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.title('速度比例增益-速度波动范围图')
plt.xlabel('速度比例增益')
plt.ylabel('速度波动范围/min')
plt.legend()
st.pyplot()

y1 = df['max']
y2 = df['min']
plt.scatter(x, y2, color='red')
plt.scatter(x, y1, color='blue')
p1 = np.polyfit(x, y1, 7)
p2 = np.polyfit(x, y2, 7)
func1 = np.poly1d(p1)
func2 = np.poly1d(p2)
x_dict = np.linspace(x.min(), x.max(), 100)
y1_dict = func1(x_dict)
y2_dict = func2(x_dict)
plt.plot(x_dict, y1_dict, label = 'max')
plt.plot(x_dict, y2_dict, label = 'min')
plt.title('速度比例增益-加速度曲线图')
plt.xlabel('速度比例增益')
plt.ylabel('加速度')
plt.legend()
st.pyplot()

dff = pd.read_csv('data/工作簿4.csv', encoding='GBK')
xx = dff['位置比例增益']
yy1 = dff['max']
yy2 = dff['min']
plt.scatter(xx, yy2, color='red')
plt.scatter(xx, yy1, color='blue')
pp1 = np.polyfit(xx, yy1, 9)
pp2 = np.polyfit(xx, yy2, 9)
func1 = np.poly1d(pp1)
func2 = np.poly1d(pp2)
xx_dict = np.linspace(xx.min(), xx.max(), 100)
yy1_dict = func1(xx_dict)
yy2_dict = func2(xx_dict)
plt.plot(xx_dict, yy1_dict, label = 'max')
plt.plot(xx_dict, yy2_dict, label = 'min')
plt.title('位置比例增益-跟随误差曲线图')
plt.xlabel('位置比例增益')
plt.ylabel('跟随误差/mm')
plt.legend()
st.pyplot()