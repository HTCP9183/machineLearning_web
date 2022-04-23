#引入
import io
import string
import time
import streamlit as st
top_col1,top_col2 = st.columns(2)
with top_col1:
    init_bar = st.progress(0)
with top_col2:
    st.button("重新运行",key=None,help="点击以重新运行")
import numpy as np
import pandas as pd
init_bar.progress(12)
import joblib as job
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

buffer_info = io.StringIO()

QDwt=pd.read_csv("QDwt.csv")
st.write("📃查看pandas所有可用参数")
with st.expander("参数细节已隐藏，点击查看更多"):
    st.text(pd.describe_option("",False))
st.write("查看当前QDwt.csv的前五行")
st.table(QDwt.head())
st.write(QDwt.describe())
st.write("此数据具有 温度 降水量 海平面气压 风速 风向 等信息")
st.info("看每一列数据类型")
QDwt.info(buf=buffer_info)
s = buffer_info.getvalue()
st.code(s)
st.write("可以看出没有空缺值")
#统计降雨的天数
st.code(Counter(QDwt['Prec']>0))
st.write("经过分析下雨的天数有334天")
QDwt['rainif']=0
QDwt['rainif']=QDwt['rainif'].mask(QDwt['Prec']>0,1)
st.code('''QDwt['rainif']=0
QDwt['rainif']=QDwt['rainif'].mask(QDwt['Prec']>0,1)''')
st.write("设置 rainif 值，用来直观说明是否下雨")
st.write("Prec大于0的认为有降水并将rainif设为1，否则设为0")
st.table(QDwt.head())