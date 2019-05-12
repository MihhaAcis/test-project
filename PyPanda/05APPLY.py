def ageGroup( row ):
    """
    Простая функция отнесения возраста к группе
    """
    
    # проверяем, что значение возраста не равно NaN
    if not pd.isnull( row['Age'] ):
        if row['Age'] <= 18:
            return 'Child'

        if row['Age'] >= 65:
            return 'Retiree'

        return 'Young'
    
    # если значение возраста NaN, то возвращаем Undef
    return 'Undef'
data['ageGroup'] = data.apply( ageGroup, axis = 1 )
data.head(10)

df.apply( lambda x: x**2 )

data['First ascent']=data['First ascent'].apply( lambda x: int("2020") if x=='unclimbed' else int(x) ) #делаем столбец 'First ascent' интовым и заменяем значения
data['Rank1']=data['Rank'].apply( lambda x: 1 if x>=1 else 1 )#добавляем столбец 'Rank1' и проставляем там 1

