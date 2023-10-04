import pandas as pd
import pandas_datareader.data as pdr
import yfinance
from datetime import datetime

yfinance.pdr_override()



data_inicial = "2017-09-12"
data_final = "2017-09-15"

tabela_cotacoes = pdr.get_data_yahoo("JBSS3.SA", data_inicial, data_final)

tabela_cotacoes['Variação de Preço'] = tabela_cotacoes['Close'] - tabela_cotacoes['Open']

print(tabela_cotacoes)
#print(tabela_cotacoes.iloc[2, 6])
