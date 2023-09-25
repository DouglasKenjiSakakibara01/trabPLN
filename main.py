import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# URL da página da web que você deseja extrair
url = 'https://exame.com/invest/mercados/cvc-dispara-17-com-derrocada-da-123-milhas/'

# Enviar uma solicitação HTTP para a página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (código de status 200 indica sucesso)
if response.status_code == 200:
    # Parsear o conteúdo HTML da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #texto = soup.get_text() #Extrair todo o texto do conteúdo HTML
    h1= soup.find("h1", class_="sc-c4a67c2e-0 bEYuXH")
    h2= soup.find("h2", class_="sc-aa737d12-2 bSTVNX")
    body=soup.find("div", id="news-body")
    '''
    print(h1.get_text())
    print(h2.get_text())
    print(body.get_text())
    '''
    texto=h1.get_text()+h2.get_text()+body.get_text()
    #print(texto)
    
    sia = SentimentIntensityAnalyzer()
    sentimento = sia.polarity_scores(texto)
    print("Avaliacao do sentimento antes do uso de tecnicas pln:")
    print(sentimento)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-**-*-**-**")
    texto=texto.lower() #converte para minusculo as palavras do texto
    tokens = word_tokenize(texto) #Dividi o texto em unidades menores
    simbolos=['.',',',';', '-', '"', '(', ')']
    tokens= [palavra for palavra in tokens if palavra not in simbolos] #retira os simbolos de pontuacao
    final = [palavra for palavra in tokens if palavra.lower() not in stopwords.words('portuguese')] # retira os stopwords
    texto_revertido = ' '.join(final)
    sentimento = sia.polarity_scores(texto_revertido)

    print("Avaliacao do sentimento apos o uso de tecnicas pln:")
    print(sentimento)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-**-*-*-**-*-**-**")
    print(texto_revertido)
    

   
else:
    print(f"A solicitação falhou com o código de status {response.status_code}")
