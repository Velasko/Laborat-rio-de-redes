"""Código para entrega do dia 02/05/2018 de Redes de Computadores I.
Dupla:
     Felipe Araújo Magalhães - 378599
     Luís Filipe Velasco da Silva - 390193
"""

import socket as sk

def main():
    print("Iniciando servidor")
    serv_addr = ('127.0.0.1', 5001)

    udp = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)#criando o socket
    udp.bind(serv_addr)#diz que é servidor
    
    try:
        while True:            
            data, addr = udp.recvfrom(2048)#data recebe a mensagem digitada no cliente e addr o endereço do cliente
            name, time = data.decode('utf-8').split('\n') #name recebe data, e time recebe o tempo que o cliente mandou a msg
            time = int(time)#convertendo para int 
            #verificando as horas e suas respectivas mensagens
            if time <= 5:
                msg = 'Bom noite, {}'
            elif time < 12:
                msg = 'Bom dia, {}'
            elif time <= 17:
                msg = 'Boa tarde, {}'
            else:
                msg = "Boa noite, {}"

            udp.sendto(msg.format(name).encode(), addr)#Enviand para o cliente a mensagem de acordo com o tempo que o cliente enviou

    except KeyboardInterrupt:
        print("Parando execução do servidor")

if __name__ == '__main__':
    main()
