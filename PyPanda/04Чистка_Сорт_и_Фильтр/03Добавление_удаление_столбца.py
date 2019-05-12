import pandas as pd
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])
#-------------------------------------------------------------------------------------------
#ДОБАВЛЕНИЕ/УДАЛЕНИЕ НОВОГО СТОЛБЦА
#-------------------------------------------------------------------------------------------
df['density'] = df['population'] / df['square'] * 1000000

df.drop(['density'], axis='columns')
del df['density']

dataNew.reset_index(inplace=True) # исправляем

data['nameLength'] = data['Name'].str.split(' ')#создание нового столбца
data['nameLength'] = data['Name'].str.split(' ').str.len()#создание нового столбца с подсчетом слов

