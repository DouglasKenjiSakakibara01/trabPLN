import pandas as pd
import pandas_datareader.data as pdr
import yfinance

yfinance.pdr_override()

data_inicial = "2023-08-30"
data_final = "2023-09-06"

tabela_cotacoes = pdr.get_data_yahoo("CVCB3.SA", data_inicial, data_final)

tabela_cotacoes['Variação de Preço'] = tabela_cotacoes['Close'] - tabela_cotacoes['Open']

print(tabela_cotacoes)
#   print(tabela_cotacoes.iloc[2, 6])
