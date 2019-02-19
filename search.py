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

for empresa in empresas:
    if scrap.buscar(empresa):
        data = datetime.today().strftime('%d-%m-%Y')
        print(empresa+' -> '+str(scrap.salvaPaginas('sites/'+empresa+'/'+data+'/')))