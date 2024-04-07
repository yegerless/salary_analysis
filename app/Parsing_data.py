import pandas as pd


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


if __name__ == '__main__':
    print(df_salary.info())
    print('\n' * 3)
    print(df_inflation.info())
    print('\n' * 3)
    print(df_salary_delta.info())
    print('\n' * 3)
    print(df_real_salary.info())