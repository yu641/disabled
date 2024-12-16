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

###============장애인구 지도시각화============###
col_1, col_2 = st.columns([1,1])

with col_1:
    st.write('## 시군구별 장애인 인구 수 [단위:명]')
    gdf_dp=pd.concat([gdf_korea_sido, dp], axis=1) #시군구별 장애인 인구 수 지도시각화
    ax = gdf_dp.plot(column='총장애인', legend=True, cmap="Reds", k=7)
    ax.set_axis_off()
    plt.show()

with col_2:
    st.write('## 시군구별 장애인 비율 [단위:%]')
    gdf_dp_rate=pd.concat([gdf_korea_sido, dp_rate], axis=1) #시군구별 장애인 인구 비율 지도시각화
    ax = gdf_dp_rate.plot(column='장애인구비율', legend=True, cmap="Reds", k=7)
    ax.set_axis_off()
    plt.show()

###============장애인구 분포============###
st.title('## 장애인 인구 유형별 분포')
tab_1, tab_2, tab_3 = st.tabs(['지역','성별','연령대'])

# 시도별 장애인구 바차트
with tab_1:
    st.write('## 시도별 장애인 인구 수')
    fig = px.bar(
        data_frame = df2,
        x='전체',
        y='시군구별',
        color='시군구별',
        orientation = 'h'
        )   
    fig.show()

# 성별에 따른 분류 파이차트
with tab_2:
    st.write('## 성별별 장애인 인구 수')
    fig=px.pie(
        values = [2641896, 1529806],
        names = ['남성','여성']
           )
    fig.update_traces(
        textposition = 'outside',
        textinfo = 'label+percent+value'
    )
    fig.show()

# 연령에 따른 분류 바차트
with tab_3:
    st.write('## 연령대별 장애인 인구 수')
    fig = px.bar(
        data_frame = df3,
        x='연령별',
        y='계',
        )
    fig.show()

###============장애의 구분============###
st.title('장애의 유형별 분포')
tab_1, tab_2 = st.tabs(['장애정도','장애유형'])

# 장애 정도에 따른 분류 파이차트
with tab_1:
    st.write('## 장애 정도별 인구 수')
    fig=px.pie(
        values = [978634,1663262],
        names = ['심한장애','심하지 않은 장애']
               )
    fig.update_traces(
        textposition = 'outside',
        textinfo = 'label+percent+value'
    )
    fig.show()
