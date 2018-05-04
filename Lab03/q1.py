"""Código para entrega do dia 02/05/2018 de Redes de Computadores I.
Dupla:
     Felipe Araújo Magalhães - 378599
     Luís Filipe Velasco da Silva - 390193
"""

import socket as sk

def main():
    site = 'si3.ufc.br'#host
    server_ip = sk.gethostbyname(site)#pegando ip pelo nome do host usando uma função do socket 

    #Como o cliente faz uso do protocolo TCP, é usado o SOCK_STREAM
    #Caso fosse UDP, seria usado o SOCK_DGRAM
    s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)#criando o socket

    request = "GET / HTTPS/1.1\nHost: {0} \n\n".format(server_ip)#requesição 

    s.connect((server_ip, 80))#conectando ao ip do server e dizendo que é uma aplicação http
    s.send(request.encode())#enviando o requerimento para o site
    result = s.recv(1024).decode('utf-8')#esperando pelo retorno
    s.close()#encerrando o socket
    print("HTTP code de {0}: {1}\n".format(site, result.split(' ')[1]))#mostra o codigo do erro, na mensagem, depois do espaço tem o codigo do erro

def portScan(site, ports=None, q2c=False):

    server_ip = sk.gethostbyname(site)#pegando ip pelo nome do host usando uma função do socket 
    if ports is None:
        ports = [20, 21, 22, 25, 53, 110, 443, 8080, 3306]#portas para serem verificadas

    if q2c: #Caso seja a questão 2, item C
        ports.append(5001)
        ports.append(5002)

    for port in ports:
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)#criando um socket tcp
   #     s.settimeout(3)
        try:
            s.connect((server_ip, port))#ele tenta conectar no servidor e a porta em questão

            if q2c:
                print("Porta {}: está executando {}".format(port,
                                                   sk.getservbyport(port)))
            else:
                print("Porta {} está executando uma aplicação não identificado".format(porta))#digita qual é a porta
            
            s.close()#encerra o socket
        except OSError as e:
            code = str(e).split(' ')[1][:-1] #code recebe o codigo do erro que possa acontecer para ser usado na verificação
            if code in ('10061', '111') :#codigo de erro para windows e para linux respectivamente
                print("Recusado: porta {0} está fechada".format(port))
            elif code in ('10060', '110') or str(e) == 'timed out':#agora analisando se o erro é por timed out
                print("Timeout: porta {0} deve estar fechada".format(port))
            else:
                raise OSError(e)#Algum outro erro do sistema operacional


if __name__ == '__main__':
##    main()
    portScan('facebook.com')
