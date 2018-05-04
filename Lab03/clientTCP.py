"""Código para entrega do dia 02/05/2018 de Redes de Computadores I.
Dupla:
     Felipe Araújo Magalhães - 378599
     Luís Filipe Velasco da Silva - 390193
"""

import socket as sk
from datetime import datetime

def main():
    addr = ('127.0.0.1', 5002)#host e port

    tcp = sk.socket(sk.AF_INET, sk.SOCK_STREAM)#criando o socket

    tcp.connect(addr)#conectando o tcp ao endereço
    print('connected')
    nome = input("Seu nome: ")#digita a mensagem
    
    #tcp.send vai enviar a mensagem e a hora que o cliente enviou isso
    tcp.send('{0}\n{1}'.format(nome,
                               datetime.now().hour).encode())
    rec = tcp.recv(4096).decode('utf-8')#recebendo os dados do serverTCP
    print(rec)#mostrando esses dados
    tcp.close()#encerrando o cliente


if __name__ == '__main__':
    main()
