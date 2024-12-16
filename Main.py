import streamlit as st
import plotly.express as px
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

gdf_korea_sido = gpd.read_file('sido.json')

df = pd.read_excel("disabledperson.xlsx")
df2 = pd.read_excel("disabledperson2.xlsx")
df3 = pd.read_excel("disabledperson3.xlsx")
df4 = pd.read_excel("disabledperson4.xlsx")
df5 = pd.read_excel("C:disabledperson5.xlsx")
df6 = pd.read_excel("C:disabledperson6.xlsx")

korea_5179 = gdf_korea_sido.to_crs(epsg=5179,inplace=False)

p=df[['총인구수']] #인구수
dp=df[['총장애인']] #장애인 인구수
dp_rate=df[['장애인구비율']] #장애인구비율=장애인인구수/총인구수*100

###============장애인구 지도시각화============###
gdf_dp=pd.concat([gdf_korea_sido, dp], axis=1) #시군구별 장애인 인구 수 지도시각화
ax = gdf_dp.plot(column='총장애인', legend=True, cmap="Reds", k=7)
ax.set_axis_off()
ax.set_title("시군구별 장애인 인구 수 [단위:명]")
plt.show()

gdf_dp_rate=pd.concat([gdf_korea_sido, dp_rate], axis=1) #시군구별 장애인 인구 비율 지도시각화
ax = gdf_dp_rate.plot(column='장애인구비율', legend=True, cmap="Reds", k=7)
ax.set_axis_off()
ax.set_title("시군구별 장애인 비율 [단위:%]")
plt.show()
