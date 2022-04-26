#引入
import io
import string
import time
from xml.etree.ElementTree import tostring
from PIL import Image
from matplotlib.axes import Axes
from sklearn.utils import column_or_1d
import streamlit as st
import pyecharts
import streamlit_echarts as st_echarts
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

top_col1,top_col2 = st.columns(2)
with top_col1:
    init_bar = st.progress(0)
with top_col2:
    st.button("重新运行",key=None,help="点击以重新运行")
import numpy as np
import pandas as pd
init_bar.progress(12)
from joblib import load
import matplotlib.pyplot as plt
import seaborn as sea
init_bar.progress(33)
import datetime
from sklearn.feature_selection import SelectKBest,f_regression
from sklearn.ensemble import RandomForestRegressor
init_bar.progress(45)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
init_bar.progress(66)
from collections import Counter
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
init_bar.progress(78)
from sklearn.model_selection import train_test_split
plt.rcParams['font.sans-serif'] = ['SimHei']  #显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #这两行需要手动设置
init_bar.progress(100)



randomForest_model =  load(filename ="RandomForest.pkl")

form_col1,form_col2 = st.columns(2)

with form_col1:
    date_for_predict = st.date_input("请输入日期")
    t_values = st.slider(
    '请输入最低气温和最高气温',
    -20.0, 60.0, (20.0, 30.0))
    avg_tmp = round((t_values[0]+t_values[1])/2,2)
    st.write('最低气温和最高气温为:', t_values,'平均气温为：',avg_tmp)
    Slpress_for_web = st.slider('请输入海平面大气压', 870, 1100, 1000)
    st.write("海平面大气压为 ", Slpress_for_web, "千帕斯卡")
    WindSpeed_for_web = st.slider("请输入风速:",0,20,0)
    cloud_for_web = st.slider("输入云量",0,10,2)
    winddir_for_web = st.slider('请输入风向', 0,360,0)
    tp=Image.open('arrow.png')
    tp_r = tp.rotate(-1*winddir_for_web)
    st.image(image=tp_r)
    st.write("风向示意如上（箭头方向）")
    st.button("点击开始计算",key=None,)
    data_M_for_predict =  date_for_predict.strftime('%m')

    data_for_web = np.array([[avg_tmp,t_values[1],t_values[0],Slpress_for_web,winddir_for_web,WindSpeed_for_web,cloud_for_web,data_M_for_predict]])#,columns=['Ave_t', 'Max_t','Min_t','SLpress','Winddir','Windsp','Cloud','mon'])
    
    result_p =  randomForest_model.predict([[avg_tmp,t_values[1],t_values[0],Slpress_for_web,winddir_for_web,WindSpeed_for_web,cloud_for_web,data_M_for_predict]])
    #st.write(result_p)
    x = str(int(result_p[0:1]*100))
with form_col2:
    with st.container():
        st.metric(label="降雨几率", value=x+"%")
#def predict_web():
