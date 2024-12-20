import streamlit as st
import plotly.express as px
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

gdf_korea_sido = gpd.read_file('sido.json')

df = pd.read_excel("disabledperson.xlsx", engine='openpyxl')
df2 = pd.read_excel("disabledperson2.xlsx", engine='openpyxl')
df3 = pd.read_excel("disabledperson3.xlsx", engine='openpyxl')
df4 = pd.read_excel("disabledperson4.xlsx", engine='openpyxl')
df5 = pd.read_excel("disabledperson5.xlsx", engine='openpyxl')
df6 = pd.read_excel("disabledperson6.xlsx", engine='openpyxl')

korea_5179 = gdf_korea_sido.to_crs(epsg=5179,inplace=False)

p=df[['총인구수']] #인구수
dp=df[['총장애인']] #장애인 인구수
dp_rate=df[['장애인구비율']] #장애인구비율=장애인인구수/총인구수*100

###============장애인의 교육수준============###
st.subheader('장애인의 교육 현황')
col1, col2 = st.columns([1,1])

# 장애인의 학력 파이차트(전체)
with col1:
    st.write('장애인의 학력(전연령)')
    fig=px.pie(
        values = [8.5, 26.8, 16.3, 31.0, 17.4],
        names = ['무학','초등학교','중학교','고등학교','대학이상']
               )
    fig.update_traces(
        textposition = 'outside',
        textinfo = 'label+percent'
    )
    fig.show()
    st.plotly_chart(fig)
    

# 장애인의 학력 파이차트(25-65세)
with col2:
    st.write('장애인의 학력(25-65세)')
    fig=px.pie(
        values = [1.7, 9.5, 12.2, 47.5, 29.0],
        names = ['무학','초등학교','중학교','고등학교','대학이상']
               )
    fig.update_traces(
        textposition = 'outside',
        textinfo = 'label+percent'
    )
    fig.show()
    st.plotly_chart(fig)

st.write('')

tab_1, tab_2, tab_3 = st.tabs(['특수학교','특수학교 학생','특수학교 교원'])
# 시도별 특수학교 수 바차트
with tab_1:
    st.write('특수학교 수')
    fig = px.bar(
        data_frame = df4,
        x='특수학교수',
        y='시군구별',
        color='시군구별',
        orientation = 'h'
        )
    fig.show()
    st.plotly_chart(fig)

# 시도별 특수학교 학생 수 바차트
with tab_2:
    st.write('특수학교 학생 수')
    fig = px.bar(
        data_frame = df4,
        x='학생수',
        y='시군구별',
        color='시군구별',
        orientation = 'h'
        )
    fig.show()
    st.plotly_chart(fig)

# 시도별 특수학교 교원 수 바차트
with tab_3:
    st.write('특수학교 교원 수')
    fig = px.bar(
        data_frame = df4,
        x='교원수',
        y='시군구별',
        color='시군구별',
        orientation = 'h'
        )
    fig.show()
    st.plotly_chart(fig)
st.write('')


###============장애인의 경제활동 현황============###
st.title('장애인 경제활동 현황')
tab_1, tab_2, tab_3 = st.tabs(['개요','지역','교육수준'])

# 장애인 경제활동인구 파이차트
with tab_1:
    st.write('장애인 경제활동 인구')
    fig=px.pie(
        values = [880929,35653,1672465],
        names = ['취업자','실업자','비경제활동인구']
               )
    fig.update_traces(
        textposition = 'outside',
        textinfo = 'label+value+percent'
    )
    st.plotly_chart(fig)

## 지역별

with tab_2:
    st.subheader('지역별 경제활동 현황')
    st.write('지역별 경제활동 인구 수')
    fig = px.bar(
        data_frame = df5,
        x=['취업자', '실업자', '비경제활동인구'],
        y='지역별',
        orientation = 'h'
        ) # 지역별 경제활동상태 바차트
    st.plotly_chart(fig)

    st.write('지역별 경제활동 인구 비율')
    fig = px.bar(
        data_frame = df5,
        x='지역별',
        y='경활률 (%)',
        ) # 지역별 경제활동인구비율
    st.plotly_chart(fig)

## 교육수준별
with tab_3:
    st.subheader('교육수준별 경제활동 현황')
    st.write('교육수준별 경제활동 인구 수')
    fig = px.bar(
        data_frame = df6,
        x=['취업자', '실업자', '비경제활동인구'],
        y='교육정도별',
        orientation = 'h'
        ) # 교육수준별 경제활동상태 바차트
    fig.show()
    st.plotly_chart(fig)

    st.write('교육수준별 경제활동 인구 비율')
    fig = px.bar(
        data_frame = df6,
        x='교육정도별',
        y='경활률 (%)'
        ) # 교육수준별 경제활동인구비율
    fig.show()
    st.plotly_chart(fig)

st.caption('장애인의 교육수준 출처: 보건복지부 2023년 장애인 실태조사 결과')
st.caption('지역별 특수학교 출처: 교육부 국립특수교육원 2023년 특수교육통계')
st.caption('장애인의 경제활동 출처: KOSIS 2023년 장애인 경제활동상태')
