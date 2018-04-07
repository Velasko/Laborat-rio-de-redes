"""Código para entrega do dia 13/04/2018 de Redes de Computadores I.
Dupla:
     Felipe Araújo Magalhães - 378599
     Luís Filipe Velasco da Silva - 390193
"""

import sys
import urllib as url
from urllib import request

def questao1():
    print("{}Execução da questão 1{}\n".format(bolt_in, bolt_out))

    sites = ("pudim.com.br",            #1
             "google.com",              #2
             "facebook.com",            #3
             "amazon.com.br",           #4
             "amazon.com",              #5
             "packtpub.com",            #6
             "si3.ufc.br",              #7
             "python.org",              #8
             "store.playstation.com",   #9
             "github.com",              #10
             )

    requests_returns = {} #dicionario para receber o código e metainformações de cada página
    #preenchimento de requests_returns e print das metainformações
    for site in sites:
        try:
            req = request.urlopen("http://{}".format(site))
            requests_returns[site] = [str(req.info()), req.getcode()]
            print('{2}{0}{3}\n\n{1}'.format(site, requests_returns[site][0], bolt_in, bolt_out))
        except url.error.HTTPError as e:
            requests_returns[site] = [e, req.getcode()]
            print('{2}{0}:{3} {1}\n\n'.format(site, e, bolt_in, bolt_out))

    #print do código de cada página
    for site, (info, code) in requests_returns.items():
        print("Site: {:<30} código: {}".format(site, code))

    print("{}Fim da execução da primeira questão{}\n".format(bolt_in, bolt_out))


def process_data(data):
    '''método para retornar o logradouro de data'''
    datas = data.decode('utf-8').split('\n')[1:-1]
    for data in datas:
        key, item = data.split(':')
        if key.split('"')[1] == "logradouro":
            return item.split('"')[1]

def questao2a():

    print("{}Execução da questão 2(a){}\n".format(bolt_in, bolt_out))

    main_link = "http://viacep.com.br/ws/{}/json"
    ceps = ('60130301',
            '60130304',
            '60130130',
            '60125001'
            )

    #cada cep em ceps é acessado e é printado seu logadouro
    for cep in ceps:
        data = request.urlopen(main_link.format(cep)).read()
        log = process_data(data)
        print("CEP: {:<10} Logradouro: {}".format(cep[:5]+"-"+cep[5:],
                                                  log))

    print("\n{}Fim da execução da segunda questão(a){}\n".format(bolt_in, bolt_out))

def questao2b():

    print("{}Execução da questão 2(b){}\n".format(bolt_in, bolt_out))

    research_main = 'https://www.google.com.br/search?q={}'
    termo_pesquisa = ('batata',)

    #criação de um opener que diz ser um browser firefox
    opener = request.FancyURLopener()
    opener.version = "Mozilla/5.0"

    for termo in termo_pesquisa:
        try:
            pesquisa = research_main.format(termo)
            x = request.urlopen(pesquisa)
            return(x.read())
        except url.error.HTTPError as e:
            print("Pesquisa por \"{0}\", gera o link\n{1}\nretornou {2}\n".format(termo,
                                                                             pesquisa,
                                                                             e))
        except url.error.URLError as e:
            print(e)

        research = opener.open(research_main.format(termo))

    print("{}Fim da execução da segunda questão(b){}\n".format(bolt_in, bolt_out))



if __name__ == "__main__":

    if sys.platform == 'linux' and "idlelib" not in sys.modules:
    #se executado em um terminal de linux: adicionar negrito
        bolt_in = "\033[1m"
        bolt_out = "\033[0m"
    else:
        bolt_in = ""
        bolt_out = ""

    questao1()
    questao2a()
    questao2b()
