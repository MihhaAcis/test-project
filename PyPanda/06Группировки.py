import pandas as pd
#-------------------------------------------------------------------------------------------
#ГРУППИРОВКИ
#-------------------------------------------------------------------------------------------

filename='D:\\Работа\\1_Python\\titanic.csv' #Создаем переменную для пути к файлу
titanic_df=pd.read_csv(filename,delimiter=',') #Создали DataFrame из файла
df = pd.read_csv('D:\\Работа\\1_Python\\apple.csv', index_col='Date', parse_dates=True)


print(titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())#сгруппировали по полу и Survived
# и посчитали количество PassengerID

print(titanic_df.groupby(['PClass', 'Survived'])['PassengerID'].count())#сгруппировали по классу

print(titanic_df.loc[titanic_df.Survived==1].groupby( 'Sex' )['Age'].mean().reset_index())

print(titanic_df.groupby( ['Sex', 'Age'] ).mean())

group_name = titanic_df.groupby(['Sex'])
print(group_name.sum())
print(group_name.sum().unstack())#Перевернули солбцы в строки

df = df.sort_index()
print(df.loc['2012-Feb', 'Close'].mean())
print(df.loc['2012-Feb':'2015-Feb', 'Close'].mean())
print(df.resample('Y')['Close'].mean())

#print(data.groupby('First ascent')[['Rank1']].sum().sort_values( by = 'Rank1', ascending = False ).head(1))#группируем по столбцу 'First ascent' складываем значения 'Rank1' и сортируем по убыванию
#print(data.groupby('Year')['Tm'].nunique())#Уникальные значения команд по годам