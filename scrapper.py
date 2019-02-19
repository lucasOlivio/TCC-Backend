from googlesearch import search_news # biblioteca para obter os resultados de busca no google
from bs4 import BeautifulSoup # Transforma páginas html em objetos BeautifulSoup para melhor manipulação
from urllib.parse import urlparse # biblioteca para manipulação de URLs
import requests # Acessa os links

def criaPasta(pasta):
    # Cria a pasta caso já não exista
    import os, errno

    try:
        os.makedirs(pasta)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    return True

def logErros(e):
    from datetime import datetime
    try:
        data = datetime.today().strftime('%d-%m-%Y')
        with open('log_erros.txt','a+') as file:
            file.write('\n\n------- '+data+' -------\n\
                                '+str(e))
    except Exception as e:
        raise


class Scrapper:
    '''Classe para extração de informações e manipulação de uma página web'''
    _whois = "http://who.is/whois/"
    _class_name = "rawWhois"  # Classe para extração
    def __init__(self, header = { 'User-Agent': '', 'From': '' }):
        # empresa: empresa buscada
        #
        # Headers - para identificação do usuário no acesso da página
        # nome: nome para acesso a página (header)
        # email: email de contato (header)
        self._header = header
        self._resultados = None

        try:
            # Module lxml para extração rápida
            import lxml
            self.parser = 'lxml'
        except:
            # Caso não tenha lxml utiliza o built-in Html Parser - extração mais lenta
            self.parser = "html.parser"
    
    def validaResultados(self):
        if self._resultados is None:
            print('Realize uma busca primeiro...')
            return False
        else:
            return True

    def getSoup(self, pagina):
        try:
            return BeautifulSoup(pagina, self.parser) # transforma o conteúdo da página em um objeto
        except Exception as e:
            logErros(e)
    
    def salvaPaginas(self, pasta = 'sites/'):
        if not self.validaResultados():
            return False

        if criaPasta(pasta):
            for resultado in self._resultados:
                try:
                    pagina = self.getPagina(resultado)
                    soup = self.getSoup(pagina.text)
                    dominio = self.getDominio(resultado)
                    with open(pasta+dominio+'.html', 'w+') as file:
                        file.write(str(soup))
                except Exception as e:
                    logErros(e)
        
        return True

    def getPagina(self, link):
        # Conecta ao site para pegar a página
        try:
            return requests.get(link, headers = self._header)
        except Exception as e:
            logErros(e)
    
    def getLinks(self):
        if not self.validaResultados():
            return False

        # retorna o array de links buscados
        return self._resultados
    
    def getDominio(self, link):
         # Pega apenas o domínio do site
        try:
            return '{uri.netloc}'.format(uri=urlparse(link))
        except Exception as e:
            logErros(e)

    def getTitulos(self):
        if not self.validaResultados():
            return False

        # retorna um array com o título de todas as notícias encontradas pela busca
        titulos = []

        try:
            for resultado in self._resultados:
                pagina = self.getPagina(resultado)
                soup = self.getSoup(pagina.text)
                #print("Título: "+soup.title.string.strip())

                titulos.append(soup.title.string.strip())
        except Exception as e:
            logErros(e)
        
        return titulos
    
    def buscar(self, busca, parSearch = {'tbs':"qdr:m", 'num':10, 'stop':1, 'pause':2}):
        # Realiza a busca de notícias no google
        # parSearch: Parâmetros para a busca
        try:
            self._resultados = search_news(busca, **parSearch) #tbs: limite de tempo
        except Exception as e:
            logErros(e)
            
        return True