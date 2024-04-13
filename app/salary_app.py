import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Загрузка первой части данных о средней заработной плате в РФ (данные с 2000 по 2016 года)
df_salary_1 = pd.read_excel(r'./data/salary_data_2000_2023.xlsx', sheet_name=1, 
                            header=2, index_col=0, nrows=35).loc[['Финансовая деятельность', 'Здравоохранение и предоставление социальных услуг',
                                                                  'Государственное управление и обеспечение военной безопасности; социальное страхование']]
df_salary_1.rename(inplace=True, 
                   index={'Здравоохранение и предоставление социальных услуг': 'Здравоохранение и социальные услуги', 
                          'Государственное управление и обеспечение военной безопасности; социальное страхование': 
                          'Гос. управление, военные и социальное страхование'})


# Загрузка второй части данных о средней заработной плате в РФ (2016-2023 года)
df_salary_2 = pd.read_excel(r'./data/salary_data_2000_2023.xlsx', sheet_name=0, header=4, index_col=0, names=[i for i in range(2017, 2024)], 
                            nrows=53).loc[['деятельность финансовая и страховая', 
                                           'деятельность в области здравоохранения и социальных услуг', 
                                           'государственное управление и обеспечение военной безопасности; социальное обеспечение']]
df_salary_2.rename(inplace=True, 
                   index={'деятельность финансовая и страховая': 'Финансовая деятельность', 
                          'деятельность в области здравоохранения и социальных услуг': 'Здравоохранение и социальные услуги', 
                          'государственное управление и обеспечение военной безопасности; социальное обеспечение': 
                          'Гос. управление, военные и социальное страхование'})


# Соединение данных о средней заработной плате в один датафрейм
df_salary = df_salary_1.merge(df_salary_2, how='inner', left_index=True, right_index=True, validate='one_to_one').T


# Загрузка данных о годовой инфляции в РФ
df_inflation = pd.read_excel(r'./data/inflation.xlsx', usecols=['Год', 'Всего'], index_col=0).loc[[i for i in range(2000, 2024)]]


# Расчет изменений средней ЗП по годам с учетом инфляции
df_salary_delta = df_salary.copy() 

for col in df_salary_delta.columns:
    for i in df_salary_delta.index.values.tolist():
        if i == 2000: 
            df_salary_delta.at[i, col] = 1
        else:
            df_salary_delta.at[i, col] = (df_salary[col].loc[i] / df_salary[col].loc[i - 1]) - (df_inflation['Всего'].loc[i - 1] / 100)


# Расчет реальной средней заработной платы в деньгах 2000 года
df_real_salary = df_salary.copy()
for col in df_real_salary.columns:
    for i in df_real_salary.index.values.tolist():
        if i == 2000: continue
        df_real_salary.at[i, col] = df_salary[col].loc[i - 1] * df_salary_delta[col].loc[i]


# График динамики номинальной средней заработной платы
salary_fig = make_subplots(specs=[[{'secondary_y': True}]])
salary_fig.add_trace(go.Scatter(x=df_salary.index, y=df_salary['Финансовая деятельность'], mode='lines+markers', name='Финансовая деятельность', 
                                line_color='#269926'), secondary_y=False)
salary_fig.add_trace(go.Scatter(x=df_salary.index, y=df_salary['Здравоохранение и социальные услуги'], mode='lines+markers', 
                                name='Здравоохранение и социальные услуги', line_color='#466FD5'), secondary_y=False)
salary_fig.add_trace(go.Scatter(x=df_salary.index, y=df_salary['Гос. управление, военные и социальное страхование'], mode='lines+markers', 
                                name='Гос. управление, военные и социальное страхование', line_color='#BFBE30'), secondary_y=False)
salary_fig.add_trace(go.Scatter(x=df_inflation.index, y=df_inflation['Всего'], mode='lines+markers', 
                                name='Годовая инфляция %', line_color='#A60000'), secondary_y=True)
salary_fig.update_layout(plot_bgcolor='white', margin={'l': 30, 'r': 0, 't': 50, 'b': 0}, 
                         xaxis_title='Год', yaxis={'title': 'Заработная плата (руб.)'}, yaxis2={'title': 'Инфляция %'})


# График динамики изменения средней заработной платы с учетом инфляции
salary_delta_fig = make_subplots(specs=[[{'secondary_y': True}]])
salary_delta_fig.add_trace(go.Scatter(x=df_salary_delta.index, y=df_salary_delta['Финансовая деятельность'], mode='lines+markers', 
                                      name='Финансовая деятельность', line_color='#269926'), 
                     secondary_y=False)
salary_delta_fig.add_trace(go.Scatter(x=df_salary_delta.index, y=df_salary_delta['Здравоохранение и социальные услуги'], mode='lines+markers', 
                                name='Здравоохранение и социальные услуги', line_color='#466FD5'), secondary_y=False)
salary_delta_fig.add_trace(go.Scatter(x=df_salary_delta.index, y=df_salary_delta['Гос. управление, военные и социальное страхование'], mode='lines+markers', 
                                name='Гос. управление, военные и социальное страхование', line_color='#BFBE30'), secondary_y=False)
salary_delta_fig.update_layout(plot_bgcolor='white', margin={'l': 30, 'r': 0, 't': 50, 'b': 0}, 
                         xaxis_title='Год', yaxis={'title': 'Изменение ЗП относительно предыдущего года'})


# График динамики реальной средней заработной платы
real_salary_fig = make_subplots(specs=[[{'secondary_y': True}]])
real_salary_fig.add_trace(go.Scatter(x=df_real_salary.index, y=df_real_salary['Финансовая деятельность'], mode='lines+markers', name='Финансовая деятельность'), 
                     secondary_y=False)
real_salary_fig.add_trace(go.Scatter(x=df_real_salary.index, y=df_real_salary['Здравоохранение и социальные услуги'], mode='lines+markers', 
                                name='Здравоохранение и социальные услуги'), secondary_y=False)
real_salary_fig.add_trace(go.Scatter(x=df_real_salary.index, y=df_real_salary['Гос. управление, военные и социальное страхование'], mode='lines+markers', 
                                name='Гос. управление, военные и социальное страхование'), secondary_y=False)
real_salary_fig.update_layout(plot_bgcolor='white', margin={'l': 30, 'r': 0, 't': 50, 'b': 0}, 
                         xaxis_title='Год', yaxis={'title': 'Заработная плата (руб.)'}, yaxis2={'title': 'Инфляция %'}, 
                        #  legend={'x': 0.93, 'y': 0.5, 'traceorder': 'reversed', 'font': {'family': 'Arial', 'size': 14, 'color': 'Black'}, 
                        #           'yanchor': 'top', 'xanchor': 'left'}
                                  )



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

