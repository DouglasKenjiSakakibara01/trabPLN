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

urlInvesting='https://br.investing.com/equities/petrobras-pn-news'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0'}
req = urllib.request.Request(url=urlInvesting, headers=headers) 
response = urllib.request.urlopen(req)
countNews, links=utils.investingScraping(response)
dates=[]
hours=[]
titles=[]
texts=[]
for i in range(countNews):
    link='https://br.investing.com'+links[i]
    print(link)
    date,hour,title,text=utils.newsScraping(link)
    # Converte a data para um objeto datetime
    obj = datetime.strptime(date, '%d.%m.%Y')
    # Formata a data de acordo com (MM/DD/AAAA) 
    date_format= obj.strftime('%Y-%m-%d')
    dates.append(date_format)
    hours.append(hour)
    titles.append(title)
    texts.append(text)
    


print(dates)
print(hours)
print(titles)
#utils.analiseSentimento(text)


