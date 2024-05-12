import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Define task data
tasks = {
    "设备1": [("任务A", 0, 2, 100), ("任务B", 3, 6, 150)],
    "设备2": [("任务C", 0, 1, 80), ("任务D", 2, 4, 120)],
    "设备3": [("任务E", 1, 3, 90), ("任务F", 4, 6, 110)]
}

# Function to get the status of devices
def get_device_status(device_tasks, current_time):
    status = []
    for task, start, end, _ in device_tasks:
        if start <= current_time < end:
            status.append((task, "运行中"))
        elif current_time < start:
            status.append((task, "待机"))
        else:
            status.append((task, "完成"))
    return status

# Function to plot a Gantt chart for device tasks
def plot_gantt(device_tasks, current_time):
    fig, ax = plt.subplots(figsize=(10, 3))
    yticks = []
    yticklabels = []
    i = 1
    for task, start, end, _ in device_tasks:
        yticks.append(i)
        yticklabels.append(task)
        ax.broken_barh([(start, end-start)], (i-0.4, 0.8), facecolors=('red' if start <= current_time < end else 'green' if current_time >= end else 'grey'))
        i += 1

    plt.grid(True)
    st.pyplot(fig)  # Use st.pyplot() to display the plot

# Streamlit app main body
st.title('设备监控电子看板')
current_time = st.slider("选择时间", min_value=0, max_value=6, value=0)
selected_device = st.selectbox("选择设备查看详细信息", list(tasks.keys()))

# Display detailed information and chart for the selected device
if selected_device:
    st.subheader(f"{selected_device} 详细信息")
    device_tasks = tasks[selected_device]
    device_status = get_device_status(device_tasks, current_time)
    for task, state in device_status:
        st.text(f"{task}: {state}")
    plot_gantt(device_tasks, current_time)

# Display an overview Gantt chart for all devices
st.subheader("所有设备总览")
for device, device_tasks in tasks.items():
    st.markdown(f"### {device}")
    plot_gantt(device_tasks, current_time)