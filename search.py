from scrapper import Scrapper # Classe criada para buscar no google informações da empresa
from datetime import datetime
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

scrap = Scrapper(headers)
date = {
    'from':"07-01-2017", 
    'to':'07-02-2017'
}

for empresa in empresas:
    if scrap.buscar(empresa, date = date):
        print(empresa+' -> '+str(scrap.salvaPaginas('sites/'+empresa+'/'+date['from']+'_'+date['to']+'/')))