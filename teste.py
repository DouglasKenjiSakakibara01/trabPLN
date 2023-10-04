import sys
import utils
import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import urllib.request


urlInvesting='https://br.investing.com/equities/petrobras-pn-news'


def investingScraping(response):
    if response.getcode() == 200:
        soup = BeautifulSoup(response, 'html.parser') 
        div=soup.find_all("div", class_="mb-4")
        element = div[0]
        ul = element.find('ul')
        li = ul.find_all('a', href=True)#cada li representa um link para a noticia
        
        links = []
        countNews=len(li)
        #print(li)
        for aux in li:
            link = aux['href']
            link = link.split("#")
            link = link[0]
            #print(link)
            
            links.append(link)
            
        return countNews,links
        
        


    else:
        print("Erro HTTP:", response.status_code)
        return None
    

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0'}
req = urllib.request.Request(url=urlInvesting, headers=headers) 
response = urllib.request.urlopen(req)    
investingScraping(response)