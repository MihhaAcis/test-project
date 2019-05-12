import pandas as pd
import numpy as np

filename='D:\\Работа\\1_Python\\titanic.csv' #Создаем переменную для пути к файлу
titanic_df=pd.read_csv(filename,delimiter=',') #Создали DataFrame из файла
df = pd.read_csv('D:\\Работа\\1_Python\\apple.csv', index_col='Date', parse_dates=True)
#-------------------------------------------------------------------------------------------
#СВОДНЫЕ ТАБЛИЦЫ
#-------------------------------------------------------------------------------------------

pvt = titanic_df.pivot_table(index=['Sex'], columns=['PClass'], values='Name', aggfunc='count')
print(pvt.loc['female', ['1st', '2nd', '3rd']])


df = df.sort_index()
print(df.loc['2012-Feb', 'Close'].mean())
print(df.loc['2012-Feb':'2015-Feb', 'Close'].mean())
print(df.resample('Y')['Close'].mean())

all_years = []
for year in range(1880, 2015+1):
    all_years.append(pd.read_csv('D:\\Работа\\2_DataS\\yob\\yob{}.txt'.format(year),
    names = ['Name', 'Sex', 'Babies']))
    all_years[-1]['Year'] = year
    all_names = pd.concat(all_years)

#print(pd.pivot_table(all_names, 'Babies', 'Name', 'Year'))
print(pd.pivot_table(all_names, 'Babies', ['Name', 'Year']).head(3))
#print(pd.pivot_table(all_names, 'Babies', ['Name', 'Sex'], 'Year'))
print(all_names.pivot_table(index=['Sex'],columns=['Name', 'Year'], values='Babies').head(3))
