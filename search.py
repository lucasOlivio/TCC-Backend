from googlesearch import search_news # biblioteca para obter os resultados de busca no google
from scrapper import Scrapper
import csv

# Lê o arquivo com o nome das empresas a serem buscadas
with open('empresas.csv',newline='', encoding='utf-8') as f:
    dados = csv.reader(f)
    empresas = [row[0] for row in dados]
print(empresas)

headers = {
    'User-Agent': 'TCC - UNIP 2019',
    'From': 'lucas27_olivio@hotmail.com'
}

for empresa in empresas:
    print('----------------- Resultados empresa "'+empresa+'" -----------------')
    resultados = search_news(empresa, tbs="qdr:m", num=10, stop=1, pause=2) #tbs: limite de tempo
    for i, resultado in enumerate(resultados):
        scrap = Scrapper(resultado, headers)
        print('\n')
        scrap.getTitulo()
        scrap.whois()
    print('\n\n')
  
