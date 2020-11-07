#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
from plotly import tools
import plotly.offline as py
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_excel('data_tables/sed17-sr-tab002.xlsx')
df = df.iloc[4:,:]
df.columns = ['Year','Doctorate-granting institutions','Recipients Total','Recipients Mean (per institution)','Recipients Median (per institution)']
year = list(df.Year)
df = df.iloc[:,1:]
df.reset_index(drop=True, inplace=True)
if st.checkbox('Show Dataframe'):
  st.write(df)
df_1 = df
country = st.multiselect('Choose an option', df.columns)
if len(country) > 0:
  df_1 = df[country]  
fig = go.Figure()
for i in df_1.columns:
	fig.add_trace(go.Scatter(x=year, y=df[i],mode='lines',name=i))	
st.plotly_chart(fig, use_container_width=True)