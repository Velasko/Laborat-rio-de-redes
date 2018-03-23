#!/usr/bin/python3

import socket as sk
import requests as req

def questao1():

    #descobrindo hostname, iplocal e nome de usuario
    hostname = sk.gethostname()
    local_ip = sk.gethostbyname(hostname)
    username = os.getlogin()
    print("{}@{}\n  IP da máquina:{}".format(username, hostname, local_ip))

    #varredura de portas de 0 até 999
    for porta in range(1000):

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
            print("    {0:<2}\tserviço: {1:<10}\tprotocolo: TCP/UDP".format(porta, tcp[1]))
        elif tcp:
            print("    {0:<2}\tserviço: {1:<10}\tprotocolo: TCP".format(porta, tcp))
        elif udp:
            print("    {0:<2}\tserviço: {1:<10}\tprotocolo: UDP".format(porta, udp))


def questao2():

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

if __name__ == "__main__":
    print("Execução da questão 1")
    questao1()
    print("Fim da execução da primeira questão\n\nInício da execução da questão 2")
    questao2()
    print("Fim da execução da segunda questão")
