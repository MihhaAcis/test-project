import pandas as pd
import pyodbc
#-------------------------------------------------------------------------------------------
#РАБОТА С SQL
#-------------------------------------------------------------------------------------------
def my_connection():
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.119.138; PORT=1433;\
DATABASE=Adventure;UID=sa;PWD=1qaz!QAZ')
    mySQLQuery=("""
			SELECT EnglishProductCategoryName as name, Model,Region,Age,
			CalendarYear as yr, Amount FROM dbo.vDMPrep
			""")
    df = pd.read_sql(mySQLQuery, connection)#,index_col='id') #Создаем датафрейм
    connection.close()
    return df
