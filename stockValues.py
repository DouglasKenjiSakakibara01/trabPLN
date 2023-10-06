import pandas as pd
import pandas_datareader.data as pdr
import yfinance
from datetime import datetime,timedelta

yfinance.pdr_override()


def stockValue(stock,date):
    date_separeted=date.split('-')
    data_alvo = datetime(int(date_separeted[0]),int(date_separeted[1]),int(date_separeted[2]))  # Substitua esta data pela data desejada
    dia_semana = data_alvo.weekday()
    if(dia_semana==4):#caso a data da publicacao seja sexta
        before = data_alvo - timedelta(days=1)
        before=str(before)
        before=before.split(' ')
        before=before[0]
        after = data_alvo + timedelta(days=3)
        after=str(after)
        after=after.split(' ')
        after=after[0]
        #print('Sexta')
    elif(dia_semana==5):#caso a data da publicacao seja sabado
        before = data_alvo - timedelta(days=1)
        before=str(before)
        before=before.split(' ')
        before=before[0]
        after = data_alvo + timedelta(days=2)
        after=str(after)
        after=after.split(' ')
        after=after[0]
        #print('sabado')
    elif(dia_semana==6):#caso a data da publicacao seja domingo
        before = data_alvo - timedelta(days=3)
        before=str(before)
        before=before.split(' ')
        before=before[0]
        after = data_alvo + timedelta(days=1)
        after=str(after)
        after=after.split(' ')
        after=after[0]    
        #print('domingo')
    elif(dia_semana==0):#caso a data da publicacao seja segunda
        before = data_alvo - timedelta(days=3)
        before=str(before)
        before=before.split(' ')
        before=before[0]
        after = data_alvo + timedelta(days=1)
        after=str(after)
        after=after.split(' ')
        after=after[0]  
        #print('segunda')
    else:
        before = data_alvo - timedelta(days=1)
        before=str(before)
        before=before.split(' ')
        before=before[0]
        after = data_alvo + timedelta(days=1)
        after=str(after)
        after=after.split(' ')
        after=after[0]
        #print('normal')
    #print(before)
    #print(date)
    #print(after)



    tableBefore = pdr.get_data_yahoo(stock, before)
    #print(tableBefore)
    valueBefore=round(tableBefore.iloc[0, 3],2)
    #print(valueBefore)
    tableValue = pdr.get_data_yahoo(stock, date)
    #print(tableValue)
    value=round(tableValue.iloc[0, 3],2)
    #print(value)
    tableAfter= pdr.get_data_yahoo(stock, after)
    #print(tableAfter)
    valueAfter=round(tableAfter.iloc[0, 3],2)
    #print(valueAfter)
    return valueBefore, value, valueAfter
    
#marketValue('JBSS3.SA','2023-10-02')