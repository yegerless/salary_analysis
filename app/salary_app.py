import pandas as pd
import streamlit as st
import plotly.express as px

from app.Parsing_data import df_salary, df_inflation, df_salary_delta, df_real_salary

st.header("Анализ динамики средней заработной платы в России в 2000-2023 годах")
st.image(r'./app/static/money.jpg')
st.write('Сравнение динамики средней заработной платы работников финансового сектора, здравоохранения и социальной поддержки, а также чиновников и военных')

