import sys
import utils
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
    def __init__(self, name, url,title,date,hour):
        self.name=name
        self.url=url
        self.title=title
        self.date=date
        self.hour=hour
        
def main(stock):
    stockUrl=None
    if stock=='PETR4.SA':
        stockUrl='/petrobras-pn-news'
    elif stock=='JBSS3.SA':
        stockUrl='/jbs-on-nm-news'
    elif stock=='CVCB3.SA':
        stockUrl='/cvc-brasil-on-news'
    else:
        print('Argumento incorreto')
        return None
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
        line=[]
        
        line.append(stock)
        line.append(title)
        line.append(link)
        line.append(date_format)
        line.append(hour)
        line.append(sentimentBefore)
        line.append(sentimentAfter)
        
        petr=line_stock('Petr4',link,title,date_format,hour)
        
        #dates.append(date_format)
        #hours.append(hour)
        #titles.append(title)
        #texts.append(text)
        
        #print(line)
        data.append(line)

        

    columns_names = ["Ação","Título", "URL", "Data", "Horário", "Sentimento antes PLN", "Sentimento depois PLN"]



    df = pd.DataFrame(data, columns=columns_names)

    file = "dados.csv"
    df.to_csv(file, index=False)

    print(f"Os dados foram gravados com sucesso no arquivo {file}.")


if __name__ == "__main__":
    main('JBSS3.SA')

