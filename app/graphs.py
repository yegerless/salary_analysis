import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from parsing_data import df_salary, df_inflation, df_salary_delta, df_real_salary

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
salary_fig.update_layout(title={'text': '<b>Динамика номинальной средней заработной платы в РФ 2000-2023</b>', 'x': 0.5, 'y':0.95,
                                'font':{'size': 24, 'color': 'Black'}}, plot_bgcolor='white', margin={'l': 30, 'r': 0, 't': 50, 'b': 0}, 
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
salary_delta_fig.update_layout(title={'text': '<b>Динамика изменений средней заработной платы в РФ 2000-2023 с учетом инфляции</b>', 'x': 0.5, 'y':0.95,
                                'font':{'size': 24, 'color': 'Black'}}, plot_bgcolor='white', margin={'l': 30, 'r': 0, 't': 50, 'b': 0}, 
                         xaxis_title='Год', yaxis={'title': 'Изменение ЗП относительно предыдущего года'})


# График динамики реальной средней заработной платы
real_salary_fig = make_subplots(specs=[[{'secondary_y': True}]])
real_salary_fig.add_trace(go.Scatter(x=df_real_salary.index, y=df_real_salary['Финансовая деятельность'], mode='lines+markers', name='Финансовая деятельность'), 
                     secondary_y=False)
real_salary_fig.add_trace(go.Scatter(x=df_real_salary.index, y=df_real_salary['Здравоохранение и социальные услуги'], mode='lines+markers', 
                                name='Здравоохранение и социальные услуги'), secondary_y=False)
real_salary_fig.add_trace(go.Scatter(x=df_real_salary.index, y=df_real_salary['Гос. управление, военные и социальное страхование'], mode='lines+markers', 
                                name='Гос. управление, военные и социальное страхование'), secondary_y=False)
real_salary_fig.update_layout(title={'text': '<b>Динамика реальной средней заработной платы в РФ 2000-2023</b>', 'x': 0.5, 'y':0.95,
                                'font':{'size': 24, 'color': 'Black'}}, plot_bgcolor='white', margin={'l': 30, 'r': 0, 't': 50, 'b': 0}, 
                         xaxis_title='Год', yaxis={'title': 'Заработная плата (руб.)'}, yaxis2={'title': 'Инфляция %'}, 
                        #  legend={'x': 0.93, 'y': 0.5, 'traceorder': 'reversed', 'font': {'family': 'Arial', 'size': 14, 'color': 'Black'}, 
                        #           'yanchor': 'top', 'xanchor': 'left'}
                                  )






if __name__ == '__main__':
    salary_fig.show()
    salary_delta_fig.show()
    real_salary_fig.show()