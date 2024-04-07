import pandas as pd
import streamlit as st

from parsing_data import df_salary, df_inflation, df_salary_delta, df_real_salary
from graphs import salary_fig, salary_delta_fig, real_salary_fig

st.header("Анализ динамики средней заработной платы в России в 2000-2023 годах")
st.image(r'./app/static/money.jpg')
st.write('Сравнение динамики средней заработной платы работников финансового сектора, здравоохранения и социальной поддержки, а также чиновников и военных')

