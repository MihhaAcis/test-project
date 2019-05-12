import pandas as pd
import numpy as np
#-------------------------------------------------------------------------------------------
#ИЗ СЛОВАРЯ
#-------------------------------------------------------------------------------------------

pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
"""
data – массив ndarray, словарь (dict) или другой DataFrame
index – список меток для записей (имена строк таблицы)
columns – список меток для полей (имена столбцов таблицы)
dtype – объект numpy.dtype, определяющий тип данных
copy – создает копию массива данных, если параметр равен True в ином случае ничего не делает.
"""
d = {'fff':[1,2,3], 'asd':[2,3,8]} #Простой

dd = {"price":pd.Series([1, 2, 3], index=['v1', 'v2', 'v3']),#Из серий
"count": pd.Series([10, 12, 7], index=['v1', 'v2', 'v3'])}

ddd = {"price":np.array([1, 2, 3]),#Из нумпай арреев
"count": np.array([10, 12, 7])}

dddd = [{"price": 3, "count":8}, {"price": 4, "count": 11}]


df = pd.DataFrame(d)
df1 = pd.DataFrame(dd)
df2 = pd.DataFrame(ddd, index=['v1', 'v2', 'v3'])
df3 = pd.DataFrame(dddd)
print(df)

df4 = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])