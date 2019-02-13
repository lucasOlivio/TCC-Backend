from googlesearch import search
import csv

# Lê o arquivo com o nome das empresas a serem buscadas
with open('empresas.csv',newline='', encoding='utf-8') as f:
    dados = csv.reader(f)
    empresas = [row[0] for row in dados]
print(empresas)

for empresa in empresas:
    print('Resultados empresa "'+empresa+'":')
    for j in search(empresa, tld="co.in",lang="pt-br",tbs="qdr:m", num=10, stop=1, pause=2): #tbs: limite de tempo
        print(j) 
    
    print('\n\n')
  
