"""Código para entrega do dia 02/05/2018 de Redes de Computadores I.
Dupla:
     Felipe Araújo Magalhães - 378599
     Luís Filipe Velasco da Silva - 390193
"""

import socket as sk
from datetime import datetime

def main():
    udp = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)#Criando o socket

    nome = input('Seu nome: ')
    dados = '{0}\n{1}'.format(nome, datetime.now().hour)#dados recebendo que foi digitado no teclado e a hora que o cliente esta usando
    addr = ("127.0.0.1",5001)#host e port
    print("Enviando")

    udp.sendto(dados.encode(),addr)#enviando os dados para o endereço em questão
    msg, server = udp.recvfrom(2048)#recebendo os dados do server e a variavel server recebe o host e port do server
    print("mensagem: {0}" .format(msg.decode('utf-8')))#mostrando a msg recebida
    udp.close()#encerrando o cliente


if __name__ == '__main__':
    main()
