import pandas as pd

df1 = pd.DataFrame( [ (0, 1), (2, 3), (4, 5) ], columns = [ 'value1', 'value2' ] ) #матрица из двух столбцов и 3 строк
df2 = pd.DataFrame( [ (10, 11), (12, 13), (14, 15), (17, 18) ], columns = [ 'value1', 'value3' ] )#матрица из двух столбцов и 4 строк
df1.add( df2 )#складывает значения столбцов, которые совпали по названию, если в одном датафреймы строк больше, то они отбрасываются, все, что не совпало - NaN
# для несовпадающих строк используем значение из fill_value
#df1.add( df2, fill_value = 100 ).fillna(0) #создает матрицу, там где в одном датафрейме нет значений подставляет 100, где значений нет вообще ставит 0. В матрице присутствуют все столбцы и макс количество строк
#df1.mul( df2, fill_value = 0 )
#df1.div( df2, fill_value = 17 )
#df1.sub( df2 )

# сохраняем все значения ключей, которые есть в df1
# если нужно несколько столбцов, то пишем left_on = ['key1', ...] и right_on = ['key2', ...]
df1.merge( df2, how = 'left', left_on = 'key1', right_on = 'key2' )

# сохраняем все значения ключей, которые есть в df2
df1.merge( df2, how = 'right', left_on = 'key1', right_on = 'key2' )

# сохраняем все значения ключей (объединение)
df1.merge( df2, how = 'outer', left_on = 'key1', right_on = 'key2' )

# сохраняем только общие значения ключей
df1.merge( df2, how = 'inner', left_on = 'key1', right_on = 'key2' )

# объединение DataFrame путем обычного "склеивания"
pd.concat( [df1, df2] )

# горизонтальное объединение
pd.concat( [df1, df2], axis = 1 )

# для join надо указать lsuffix и rsuffix
df1.join( df2, how = 'left', lsuffix = '_df1', rsuffix = '_df2' )

