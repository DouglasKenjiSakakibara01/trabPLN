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
url='https://br.investing.com/news/stock-market-news/petrobras-avalia-possibilidade-de-reajuste-de-diesel-e-gasolina-antes-do-fim-do-ano-diz-ceo-1162147'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0'}
req = urllib.request.Request(url=url, headers=headers) 
response = urllib.request.urlopen(req)
date, hour, h1, text=utils.newsExtract(response)
# Converte a data para um objeto datetime
obj = datetime.strptime(date, '%d.%m.%Y')

# Formata a data de acordo com (MM/DD/AAAA) 
date_format= obj.strftime('%m-%d-%Y')

print(date_format)
print(hour)
print(h1)
utils.analiseSentimento(text)



