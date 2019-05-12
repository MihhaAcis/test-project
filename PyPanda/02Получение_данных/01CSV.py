import pandas as pd
import pyodbc
#-------------------------------------------------------------------------------------------
#ПОЛУЧЕНИЕ ДАННЫХ ИЗ CSV
#-------------------------------------------------------------------------------------------
names2015 = pd.read_csv('D:\\Работа\\2_DataS\\yob\\yob2015.txt',
					   names = ['Name', 'Sex', 'Babies'],delimiter=',')
#data=pd.read_csv(filename,delimiter=',', dtype = {'SibSp':str,'Parch':str}) #Изменение типа столбцов
