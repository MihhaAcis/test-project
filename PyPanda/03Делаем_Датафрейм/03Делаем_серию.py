import pandas as pd
import numpy as np

#-------------------------------------------------------------------------------------------
#СЕРИЯ
#У серии всегда вставляется индекс (иногда индексом становится другой столбец),
#который желательно сбрасывать x.reset_index(inplace=True)
#-------------------------------------------------------------------------------------------

pd.Series(dataNP, index = [ 'first', 'second', 'third' ])
x=df[column] 
my_series = pd.Series([5, 6, 7, 8, 9, 10])
my_series.index
my_series.values
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
