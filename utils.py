import sys
import utils
import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import urllib.request



def newsScraping(response):
    if response.getcode() == 200:
         
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
                    span_text=" ".join(span_text)  # Use um espaço em branco como separador
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
    else:
        print("Erro HTTP:", response.status_code)
        return None


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

def analiseSentimento(texto):
    sia = SentimentIntensityAnalyzer()
    sentimento = sia.polarity_scores(texto)
    print("Avaliacao do sentimento antes do uso de tecnicas pln:")
    print(sentimento)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-**-*-**-**")
    texto=texto.lower() #converte para minusculo as palavras do texto
    texto = word_tokenize(texto) #Dividi o texto em unidades menores
    simbolos=['.',',',';', '-', '"', '(', ')', '”','“', '<', '>', '``',"''"]
    texto= [palavra for palavra in texto if palavra not in simbolos] #retira os simbolos de pontuacao
    texto = [palavra for palavra in texto if palavra.lower() not in stopwords.words('portuguese')] # retira os stopwords
    texto_revertido = ' '.join(texto)
    sentimento = sia.polarity_scores(texto_revertido)
    
    print("Avaliacao do sentimento apos o uso de tecnicas pln:")
    print(sentimento)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-**-*-**-**")
    print(texto_revertido)

