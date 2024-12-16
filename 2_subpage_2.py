import streamlit as st
import plotly.express as px
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'

gdf_korea_sido = gpd.read_file('C:/vis/geodata/sido.json')

df = pd.read_excel("C:/vis/disabledperson.xlsx")
df2 = pd.read_excel("C:/vis/disabledperson2.xlsx")
df3 = pd.read_excel("C:/vis/disabledperson3.xlsx")
df4 = pd.read_excel("C:/vis/disabledperson4.xlsx")
df5 = pd.read_excel("C:/vis/disabledperson5.xlsx")
df6 = pd.read_excel("C:/vis/disabledperson6.xlsx")

korea_5179 = gdf_korea_sido.to_crs(epsg=5179,inplace=False)

p=df[['총인구수']] #인구수
dp=df[['총장애인']] #장애인 인구수
dp_rate=df[['장애인구비율']] #장애인구비율=장애인인구수/총인구수*100

###============장애인의 교육수준============###
st.title('## 장애인 인구 유형별 분포')
col1, col2 = st.columns([1,1])

# 장애인의 학력 파이차트(전체)
with col1:
    st.write('## 장애인의 학력')
    fig=px.pie(
        values = [8.5, 26.8, 16.3, 31.0, 17.4],
        names = ['무학','초등학교','중학교','고등학교','대학이상']
               )
    fig.update_traces(
        textposition = 'outside',
        textinfo = 'label+percent'
    )
    fig.show()

# 장애인의 학력 파이차트(25-65세)
with col1:
    st.write('## 장애인의 학력')
    fig=px.pie(
        values = [1.7, 9.5, 12.2, 47.5, 29.0],
        names = ['무학','초등학교','중학교','고등학교','대학이상']
               )
    fig.update_traces(
        textposition = 'outside',
        textinfo = 'label+percent'
    )
    fig.show()

st.write('')

col1, col2, col3 = st.columns([1,1,1])
# 시도별 특수학교 수 바차트
with col1:
    st.write('## 특수학교 수')
    fig = px.bar(
        data_frame = df4,
        x='특수학교수',
        y='시군구별',
        color='시군구별',
        orientation = 'h'
        )
    fig.show()

# 시도별 특수학교 학생 수 바차트
with col2:
    st.write('## 특수학교 학생 수')
    fig = px.bar(
        data_frame = df4,
        x='학생수',
        y='시군구별',
        color='시군구별',
        orientation = 'h'
        )
    fig.show()

# 시도별 특수학교 교원 수 바차트
with col3:
    st.write('## 특수학교 교원 수')
    fig = px.bar(
        data_frame = df4,
        x='교원수',
        y='시군구별',
        color='시군구별',
        orientation = 'h'
        )
    fig.show()
st.write('')

###============장애인의 경제활동 현황============###
st.title('## 장애인 경제활동 현황')
tab_1, tab_2, tab_3 = st.tabs(['개요','지역','교육수준'])

# 장애인 경제활동인구 파이차트
with tab_1:
    st.write('## 장애인 경제활동 인구')
    fig=px.pie(
        values = [880929,35653,1672465],
        names = ['취업자','실업자','비경제활동인구']
               )
    fig.update_traces(
        textposition = 'outside',
        textinfo = 'label+value+percent'
    )
    fig.show()

## 지역별

with tab_2:
    st.write('## 지역별 경제활동 현황')
    st.write('# 지역별 경제활동 인구 수')
    fig = px.bar(
        data_frame = df5,
        x=['취업자', '실업자', '비경제활동인구'],
        y='지역별',
        orientation = 'h'
        ) # 지역별 경제활동상태 바차트
    fig.show()

    st.write('# 지역별 경제활동 인구 비율')
    fig = px.bar(
        data_frame = df5,
        x='지역별',
        y='경활률 (%)',
        ) # 지역별 경제활동인구비율
    fig.show() 

## 교육수준별
with tab_3:
    st.write('## 교육수준별 경제활동 현황')
    st.write('# 교육수준별 경제활동 인구 수')
    ig = px.bar(
        data_frame = df6,
        x=['취업자', '실업자', '비경제활동인구'],
        y='교육정도별',
        orientation = 'h'
        ) # 교육수준별 경제활동상태 바차트
    fig.show() 

    st.write('# 교육수준별 경제활동 인구 비율')
    fig = px.bar(
        data_frame = df6,
        x='교육정도별',
        y='경활률 (%)',
        )
    fig.show() # 교육수준별 경제활동인구비율
