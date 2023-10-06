import sys
import utils
import stockValues
import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime
import urllib.request
import pandas as pd

stocks=['PETR4.SA','JBSS3.SA','CVCB3.SA']

#dates=[]
#hours=[]
#titles=[]
#texts=[]

data = []

class line_stock:
    def __init__(self, name, url,title,date,hour,value,valueBefore,valueAfter):
        self.name=name
        self.url=url
        self.title=title
        self.date=date
        self.hour=hour
        self.value=value
        self.valueBefore=valueBefore
        self.valueAfter=valueAfter
        
def generate_results(stock,stockUrl):
    countNews,links=utils.investingScraping(stockUrl)        
    for i in range(countNews):
        link='https://br.investing.com'+links[i]
        print(link)
        date,hour,title,text=utils.newsScraping(link)
        # Converte a data para um objeto datetime
        obj = datetime.strptime(date, '%d.%m.%Y')
        # Formata a data de acordo com (MM/DD/AAAA) 
        date_format= obj.strftime('%Y-%m-%d')
        sentimentBefore, sentimentAfter=utils.sentiment_analyze(text)
        valueBefore, value, valueAfter=stockValues.stockValue(stock, date_format)
        line=[]
        
        line.append(stock)
        line.append(title)
        line.append(link)
        line.append(date_format)
        line.append(hour)
        line.append(sentimentBefore)
        line.append(sentimentAfter)
        line.append(valueBefore)
        line.append(value)
        line.append(valueAfter)


        
        
        #dates.append(date_format)
        #hours.append(hour)
        #titles.append(title)
        #texts.append(text)
        
        #print(line)
        data.append(line)
    return data
def main(stock):
    stockUrl=None
    fileName=None
    if stock=='MGLU3.SA':
        stockUrl='/magaz-luiza-on-nm-news'
        data=generate_results(stock,stockUrl)
        fileName='mglu3'
    elif stock=='JBSS3.SA':
        stockUrl='/jbs-on-nm-news'
        data=generate_results(stock,stockUrl)
        fileName='jbss3'
    elif stock=='CVCB3.SA':
        stockUrl='/cvc-brasil-on-news'
        data=generate_results(stock,stockUrl)
        fileName='cvcb3'
    else:
        print('Argumento incorreto')
        return None
    '''
    countNews,links=utils.investingScraping(stockUrl)        
    for i in range(countNews):
        link='https://br.investing.com'+links[i]
        print(link)
        date,hour,title,text=utils.newsScraping(link)
        # Converte a data para um objeto datetime
        obj = datetime.strptime(date, '%d.%m.%Y')
        # Formata a data de acordo com (MM/DD/AAAA) 
        date_format= obj.strftime('%Y-%m-%d')
        sentimentBefore, sentimentAfter=utils.analiseSentimento(text)
        valueBefore, value, valueAfter=precos.marketValue(stock, date_format)
        line=[]
        
        line.append(stock)
        line.append(title)
        line.append(link)
        line.append(date_format)
        line.append(hour)
        line.append(sentimentBefore)
        line.append(sentimentAfter)
        line.append(valueBefore)
        line.append(value)
        line.append(valueAfter)


        
        
        #dates.append(date_format)
        #hours.append(hour)
        #titles.append(title)
        #texts.append(text)
        
        #print(line)
        data.append(line)

        
    '''
    columns_names = ["Ação","Título", "URL", "Data", "Horário", "Sentimento antes PLN", "Sentimento depois PLN", "Preço anterior",  "Preço", "Preço Posterior "]



    df = pd.DataFrame(data, columns=columns_names)

    file = f"{fileName}.csv"
    df.to_csv(file, index=False)

    print(f"Os dados foram gravados com sucesso no arquivo {file}.")


if __name__ == "__main__":
    main('CVCB3.SA')

