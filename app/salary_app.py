import pandas as pd
import streamlit as st

from parsing_data import df_salary, df_inflation, df_salary_delta, df_real_salary
from graphs import salary_fig, salary_delta_fig, real_salary_fig

st.set_page_config(layout="wide")

st.title("Анализ динамики средней заработной платы в России в 2000-2023 годах")
st.image(r'./app/static/money.jpg')
st.write('Сравнение динамики средней заработной платы работников финансового сектора, здравоохранения и социальной поддержки, а также чиновников и военных')

tab1, tab2, tab3, tab4 = st.tabs(['Динамика средней ЗП', 'Изменения ЗП с учетом инфляции', 'Динамика реальной средней ЗП', 'Данные'])


with tab1:
   tab1.header('Динамика среднего уровня заработной платы в России')
   st.plotly_chart(salary_fig, use_container_width=True)


with tab2:
   tab2.header('Динамика изменений среднего уровня заработной платы с учетом инфляции')
   st.plotly_chart(salary_delta_fig, use_container_width=True)


with tab3:
   tab3.header('Динамика среднего уровня заработной платы с учетом инфляции')
   st.plotly_chart(real_salary_fig, use_container_width=True)


with tab4:
   tab4.header('Здесь вы можете ознакомиться с исследуемыми данными')
   
   st.write('Данные об уровне средней заработной платы в РФ в 2000-2023 годах')
   st.table(df_salary)
   
   st.write('Данные об уровне инфляции в РФ в 2000-2023 годах')
   st.table(df_inflation)

   st.write('Данные об изменении средней ЗП относительно ЗП в предыдущий год с учетом инфляции в РФ в 2000-2023 годах')
   st.table(df_salary_delta)

   st.write('Данные об уровне реальной средней заработной платы (ЗП с учетом инфляции) в РФ в 2000-2023 годах')
   st.table(df_real_salary)

