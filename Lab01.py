#!/usr/bin/python3

import socket as sk
import requests as req
import os, sys

def getlocalip(hostname):
    ip = sk.gethostbyname(hostname)

    #Em sistemas linux, e comum ser retornado 127.0.x.x
    #Caso não ocorra isso, souponho que seja retornado algo do tipo 192.168.x.x
    #Entao retorno o valor
    if ip.split('.')[0] != '127':
        return(ip)

    #Caso seja de fato 127.0.x.x, um socket e criado e le-se o ip deste: o ip da maquina
    s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    return(ip)

def getglobalip():
    #le o site que simplesmente diz o ip global
    try:
        return( req.get('https://api.ipify.org').text )
    except Exception:
        return("Não foi possível descobrir o ip global")

def questao1():

    print("{}Execução da questão 1{}".format(bolt_in, bolt_out))

    #descobrindo hostname, iplocal e nome de usuario
    hostname = sk.gethostname()

    local_ip = getlocalip(hostname)
    global_ip = getglobalip()

    username = os.getlogin()
    print("{}@{}\n  IP local: {}\n  IP global:{}".format(username, hostname, local_ip, global_ip))

    #varredura de portas de 0 até 9999
    for porta in range(10000):

##        Caso OSError seja levantado, ao tentar definir as variaveis tcp e udp,
##        significa que nao sao utilizados naquela porta. Caso isto ocorra,
##        as variaveis serao nulas, equivalenta a 0 em condicionais
        
        try:
            tcp = sk.getservbyport( porta, 'tcp' )
        except OSError:
            tcp = None

        try:
            udp = sk.getservbyport( porta, 'udp' )
        except OSError:
            udp = None

##        Caso tcp e udp, nenhuma das variaveis sao nulas, implicando que OSError nao foi
##        levantado para nenhum dos protocolos. implicando que a porta usa ambos.

##        Caso tcp, significa que udp nulo, entao OSError foi levantado para o udp
##        e a porta entao nao faz uso do prootocolo upd.

##        Caso udp, forma analoga do caso tcp.

##        else: ambos sao nulos, implicando que a porta nao faz uso de nenhum dos dois protocolos.

        if tcp and udp:
            print("    {0:<2}\tserviço: {1:<10}\tprotocolo: TCP/UDP".format(porta, tcp))
        elif tcp:
            print("    {0:<2}\tserviço: {1:<10}\tprotocolo: TCP".format(porta, tcp))
        elif udp:
            print("    {0:<2}\tserviço: {1:<10}\tprotocolo: UDP".format(porta, udp))

    print("{}Fim da execução da primeira questão{}\n".format(bolt_in, bolt_out))

def questao2():

    print("{}Início da execução da questão 2{}".format(bolt_in, bolt_out))

    #link base para descobrir a regiao do ip/link
    base_link = "http://freegeoip.net/json/{}"

    #link a serem verificados
    links = ("lipe.velasco.one",        #1
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

    for link in links:
        #link_ip = sk.gethostbyname(link) #Descobrindo o ip de um link
        dados = req.get( base_link.format(link) ).json()
        print(link)
        print("\tIP:\t{}\n\tPaís:\t{}\n\tRegião:\t{}\n".format(dados["ip"],
                                                             dados["country_name"],
                                                             dados["region_name"]))

    print("{}Fim da execução da segunda questão{}\n".format(bolt_in, bolt_out))

if __name__ == "__main__":

    if sys.platform == 'linux' and "idlelib" not in sys.modules:
    #se executado em um terminal de linux: adicionar negrito
        bolt_in = "\033[1m"
        bolt_out = "\033[0m"
    else:
        bolt_in = ""
        bolt_out = ""

    questao1()
    questao2()
