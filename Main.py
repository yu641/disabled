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
st.title('장애인 인구 지도시각화')
st.header('시군구별 장애인 인구 수 지도시각화 [단위: 명]')

gdf_dp=pd.concat([gdf_korea_sido, dp], axis=1) #시군구별 장애인 인구 수 지도시각화
ax = gdf_dp.plot(column='총장애인', cmap='Blues', legend=True, k=7)
ax.set_axis_off()
st.pyplot()

st.write('')


st.header('시군구별 장애인 비율 [단위: %]')
gdf_dp_rate=pd.concat([gdf_korea_sido, dp_rate], axis=1) #시군구별 장애인 인구 비율 지도시각화
ax = gdf_dp_rate.plot(column='장애인구비율', cmap='Blues', legend=True, k=7)
ax.set_axis_off()
plt.show()
st.pyplot()

st.caption('장애인 인구 출처: KOSIS 시도별,장애유형별,성별 등록장애인수, 2023년')
st.caption('인구 출처: 행정안전부 행정동별 주민등록 인구 및 세대현황, 2023년')
