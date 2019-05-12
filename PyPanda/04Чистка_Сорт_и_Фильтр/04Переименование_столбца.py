import pandas as pd
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])

#-------------------------------------------------------------------------------------------
#ПЕРЕИМЕНОВАНИЕ СТОЛБЦОВ
#-------------------------------------------------------------------------------------------
df = df.rename(columns={'Country Code': 'country_code'}, inplace=True ) # параметр inplace указывает, что надо подставить новое значение в самом DataFrame data
# можно заменить названия столбцов
data.columns = [ 'ID', 'Survived', 'Class', 'FIO', 'Gender', 'Age', 'SibSp', 'Parch', 'Ticker number', 'Fare', 'Cabin', 'Emnarked' ]

