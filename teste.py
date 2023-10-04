'''
Arquivo para testar as funcoes de scraping e verificar outras funcoes
'''
import sys
import utils
import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import urllib.request
import pandas as pd

urlInvesting='https://br.investing.com/equities/petrobras-pn-news'

'''
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
'''

'''
import pandas as pd

# Defina os nomes das colunas
nomes_colunas = ["Ação","Título", "URL", "Data", "Horário"]

# Crie um DataFrame com colunas nomeadas
dados = [
    ["Alice", 28, "São Paulo"],
    ["Bob", 35, "Rio de Janeiro"],
    ["Carol", 22, "Belo Horizonte"]
]

df = pd.DataFrame(dados, columns=nomes_colunas)

nome_arquivo = "dados.csv"
df.to_csv(nome_arquivo, index=False)

print(f"Os dados foram gravados com sucesso no arquivo {nome_arquivo}.")

'''