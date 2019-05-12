import pandas as pd
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])
#-------------------------------------------------------------------------------------------
#ДОСТУПЫ И ПРИСВАИВАНИЯ
#-------------------------------------------------------------------------------------------
my_series.index#Выдает индексы серии
my_series.values#Выдает значения серии

my_series2[['a', 'b', 'f']] = 0#Групповое присваивание

'd' in my_series3#Проверяет есть ли 'd' среди индексов
7 in my_series2.values#Проверяет есть ли 7 среди значений

y_series3.name = 'numbers'#Имя серии
my_series3.index.name = 'letters'#Имя индекса серии

my_series3.index = ['A', 'B', 'C', 'D']#Изменение индекса
my_series[4]#У индекса есть цифровой номер и то название, которое ему дали, в данном случае 4=е

dataNew.reset_index(inplace=True) # исправляем
