import sys
import utils
import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import urllib.request
import spacy
from translate import Translator
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0'}

def newsScraping(url):
        req = urllib.request.Request(url=url, headers=headers) 
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response, 'html.parser')
        #text = soup.get_text() #Extrai todo o texto do conteúdo HTML
        span=soup.find_all("div", class_="contentSectionDetails")
        
        h1= soup.find("h1", class_="articleHeader").text
        
        body= soup.find("div",class_="WYSIWYG articlePage")
        div = body.find_all('p')
        
        
        for element in span:
                span_text = element.get_text()
                if 'Publicado' in span_text:
                    span_text=span_text.split('\n')
                    span_text=" ".join(span_text)
                    span_text=span_text.split()
                    date=span_text[1]
                    hour=span_text[2]

                    #print(data)
                    #print(hour)
        text = []
        for i, t in enumerate(div):
            if 'Posição adicionada com êxito a' not in t.text:#fica aparecendo no comeco do texto
                text.append(t.text)
        text=' '.join(text)
        #print(h1)         
        #print(text)

        return date, hour, h1, text
   


def investingScraping(stockUrl):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0'}
    links = []
    countNews=0
    for i in range(1,15,2):#para pegar mais noticias no site
            urlInvesting='https://br.investing.com/equities'+f"{stockUrl}"+f"/{i}"
            req = urllib.request.Request(url=urlInvesting, headers=headers) 
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                soup = BeautifulSoup(response, 'html.parser') 
                div=soup.find_all("div", class_="mb-4")
                element = div[0]
                ul = element.find('ul')
                li = ul.find_all('a', href=True)#cada li representa um link para a noticia                
                countAux=0
                    
                for aux in li:
                    link = aux['href']
                    link = link.split("#")
                    link = link[0]
                    
                    
                    #print(link)#por algum motivo o mesmo link esta sendo gerado 2 vezes
                    if countAux % 2 == 0: #gambiarra para na pegar o mesmo link 2 vezes
                        
                        countNews=countNews+1
                        #print(i)
                        #print(link) 
                        links.append(link)
                                
                    countAux=countAux+1
                       
            else:
                print("Erro HTTP:", response.status_code)
    return countNews,links       

def sentiment_analyze(text):
    sia = SentimentIntensityAnalyzer()
    nlp = spacy.load('pt_core_news_sm')
    sentiment = sia.polarity_scores(text)
    compoundBefore = sentiment["compound"]#pega a pontuacao geral do sentimento antes da aplicacao das tecnicas pln
    print("Avaliacao do sentimento antes do uso de tecnicas pln:")
    print(compoundBefore)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-**-*-**-**")
    text=text.lower() #converte para minusculo as palavras do texto
    text = word_tokenize(text) #Dividi o texto em unidades menores
    simbols=['.',',',';', '-', '"', '(', ')', '”','“', '<', '>', '``',"''", ':']
    text= [word for word in text if word not in simbols] #retira os simbolos de pontuacao
    text = [word for word in text if word.lower() not in stopwords.words('portuguese')] # retira os stopwords
    '''
    translator = Translator(to_lang="pt")#objeto Translator
    for i in range(text):
        text[0]=translator.translate(text[0])
    '''
    text=' '.join(text)
    doc = nlp(text)
    text = [token.lemma_ for token in doc]#lematizacao
    print('\n')
    print(text)
    text=' '.join(text)
    sentiment= sia.polarity_scores(text)
    compoundAfter = sentiment["compound"]#pega o a pontuacao geral do sentimento depois da aplicacao das tecnicas pln
    print("Avaliacao do sentimento apos o uso de tecnicas pln:")
    print(compoundAfter)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-**-*-**-**")
    
    return compoundBefore, compoundAfter


#countNews, links=utils.investingScraping('/cvc-brasil-on-news')
#print(countNews)
#print(links)

