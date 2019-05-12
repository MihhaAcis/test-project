import pandas as pd
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])
#-------------------------------------------------------------------------------------------
#ФИЛЬТРАЦИЯ
#-------------------------------------------------------------------------------------------
my_series2[my_series2 > 0]
my_series2[my_series2 > 0] * 2

df.loc['KZ']
df.iloc[0]#Извлекает по числовому значения индекса
df.loc[['KZ', 'RU'], 'population']#индексы в двойных []
df[df.population > 10][['country', 'square']]
df.loc['2012-Feb', 'Close'].mean()
df.loc['2012-Feb':'2015-Feb', 'Close'].mean()

mask = ( data.PassengerId % 2 == 0 )
data.loc[ mask ].head()
data[ data.PassengerId % 2 == 0 ].head()

data.loc[ pd.isnull( data['Age'] ) ].head()#пустые строки
data.loc[ ~pd.isnull( data['Age'] ) ].head()# если надо исключить условие, то ставим тильду:

dataSelected = data.loc[:3, ['Name', 'Age', 'Cabin']]
dataSelected = data.loc[2:15, ['Name', 'Age', 'Cabin']]

my_series2[['a', 'b', 'f']]#Групповая выборка

