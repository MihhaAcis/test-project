import pandas as pd
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])
#-------------------------------------------------------------------------------------------
#СОРТИРОВКИ
#-------------------------------------------------------------------------------------------
# сортировка по индексу
data.sort_index( ascending = False ).head()
# сортировка по значениям
data.sort_values( by = 'Age', ascending = False ).head()
# сортировка по значениям нескольких столбцов
data.sort_values( by = ['Sex', 'Age'], ascending = [True, False] ).head()