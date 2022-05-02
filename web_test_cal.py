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

st.markdown("""
<nav  style="background-color: #3498DB;top: 0;right: 0;left: 0;padding: 0.5rem 1rem;font-size: 1.25rem;text-align:center;">
  <a  href="web_test.py" style="text-decoration: none;;color: #fff";>机器学习在线演示</a>
  </button>
</nav>
""", unsafe_allow_html=True)



init_bar = st.progress(0)
import numpy as np
import pandas as pd
init_bar.progress(12)
from joblib import load
import matplotlib.pyplot as plt
import seaborn as sea
init_bar.progress(33)
import datetime
from sklearn.feature_selection import SelectKBest,f_regression
init_bar.progress(40)
from sklearn.ensemble import RandomForestRegressor
init_bar.progress(45)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
init_bar.progress(66)
from collections import Counter
from sklearn.metrics import mean_absolute_error
init_bar.progress(70)
from sklearn.metrics import mean_squared_error
init_bar.progress(78)
from sklearn.model_selection import train_test_split
plt.rcParams['font.sans-serif'] = ['SimHei']  #显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #这两行需要手动设置
init_bar.progress(100)



randomForest_model =  load(filename ="RandomForest.pkl")

empty1,form_col1,empty2,form_col2,empty3 = st.columns([1,6,1,6,1])

with form_col1:
    date_for_predict = st.date_input("请输入日期")
    t_values = st.slider(
    '请输入最低气温和最高气温',
    -20.0, 60.0, (20.0, 30.0))
    avg_tmp = round((t_values[0]+t_values[1])/2,2)
    st.write('最低气温为:',t_values[0],'℃ 最高气温为:', t_values[1],'℃ 平均气温为：',avg_tmp,'℃')
    Slpress_for_web = st.slider('请输入海平面大气压', 870, 1100, 1000)
    st.write("海平面大气压为 ", Slpress_for_web, "千帕斯卡")
    WindSpeed_for_web = st.slider("请输入风速:",0,20,0)
    cloud_for_web = st.slider("输入云量",0,10,2)
    winddir_for_web = st.slider('请输入风向', 0,360,0)
    tp=Image.open('arrow.png')
    tp_s=tp.resize([75,75])
    tp_r = tp_s.rotate(-1*winddir_for_web)
    st.image(image=tp_r)
    st.write("风向示意如上（箭头方向）")
    data_M_for_predict =  date_for_predict.strftime('%m')

    data_for_web = np.array([[avg_tmp,t_values[1],t_values[0],Slpress_for_web,winddir_for_web,WindSpeed_for_web,cloud_for_web,data_M_for_predict]])#,columns=['Ave_t', 'Max_t','Min_t','SLpress','Winddir','Windsp','Cloud','mon'])
    
    result_p =  randomForest_model.predict([[avg_tmp,t_values[1],t_values[0],Slpress_for_web,winddir_for_web,WindSpeed_for_web,cloud_for_web,data_M_for_predict]])


with empty1:
  st.empty()
with empty2:
  st.empty()
with empty3:
  st.empty()
st.markdown(''' <style>
                css-wmn9kq e13vu3m50 div{
                      text-align: center;
                }
                </style>''',unsafe_allow_html=True)
with form_col2:
  if result_p[0]==0:
    st.success('-☀️风和日丽，快出去走走吧☀️-')
  else:
    st.info('-🌧️与可能下雨哦，注意带伞🌧️-')
    KNN_w_model = load('KNN_model_fw.pkl')
    result_w = KNN_w_model.predict([[avg_tmp,t_values[1],t_values[0],Slpress_for_web,winddir_for_web,WindSpeed_for_web,cloud_for_web,data_M_for_predict]])
    st.info("🌧️预计降水量为"+str(round(result_w[0]+1.43),2)+'毫米🌧️')
