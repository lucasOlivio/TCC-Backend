from bs4 import BeautifulSoup # Transforma páginas html em objetos BeautifulSoup para melhor manipulação
from urllib.parse import urlparse # biblioteca para manipulação de URLs
import requests # Acessa os links

class Scrapper:
    '''Classe para extração de informações e manipulação de uma página web'''
    _whois = "http://who.is/whois/"
    _class_name = "rawWhois"  # Classe para extração
    def __init__(self, link, header = { 'User-Agent': '', 'From': '' }):
        # link: link da página que será acessada
        #
        # Headers - para identificação do usuário no acesso da página
        # nome: nome para acesso a página (header)
        # email: email de contato (header)
        self._link   = link
        self._header = header

        # Pega apenas o domínio do site
        parsed_uri = urlparse(self._link)
        self._domain = '{uri.netloc}'.format(uri=parsed_uri)

        self._pagina = requests.get(self._link, headers = self._header) # acessa o link para pegar o conteúdo

    def whois(self):
        # Conectando ao server whois
        pagina_whois = requests.get(self._whois + self._domain, headers = self._header)

        try:
            # Module lxml para extração rápida
            import lxml
            parse = BeautifulSoup(pagina_whois.text,'lxml')
        except:
            # Caso não tenha lxml utiliza o built-in Html Parser - extração mais lenta
            parse = BeautifulSoup(pagina_whois.text, "html.parser")

        try:
            container = parse.findAll("div",{'class':self._class_name})
            sections = container[1:]
            for section in sections:
                extract = section.findAll('div')
                heading = extract[0].text
                print('\n[ ',heading,' ]')
                for i in extract[1].findAll('div'):
                    fortab = '\t|'
                    for j in i.findAll('div'):
                        fortab = fortab+'----'
                        line = j.text.replace('\n', ' ')
                        print(fortab,'>', line)
        except Exception as e:
            print("[ Error ] ", e)
    
    def getTitulo(self):
        soup = BeautifulSoup(self._pagina.text, 'html.parser') # transforma o conteúdo da página em um objeto BeautifulSoup para melhor manipulação

        print("Título: "+soup.title.string.strip())