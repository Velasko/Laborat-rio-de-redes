
# coding: utf-8

# In[ ]:


import socket 

from datetime import datetime

print('#### Questão 2 ####\n')
print( '--- Criando serverUDP ---')



addr = '127.0.0.1'
porta = 5000

#CRIANDO SOCKET TCP
TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

end_port = (addr, porta)

TCP.bind(end_port)

TCP.listen()

print('Servidor TCP aguardadno conexões na porta %s, para encerrar pressione Ctrl+C' %porta)

while True: 
    
    con, cliente = TCP.accept()
    print("Conectado por: ", cliente)
    mensagem = con.recv(2048).decode('utf-8')
    print("Mensagem recebida: %s" %mensagem)
    
    tempo = datetime.now().hour
    
    if tempo < 12:
        con.send('Bom Dia, %s' %mensagem).encode()
    elif tempo < 18:
        con.send('Boa Tarde, %s' %mensagem).encode()
    else:
        con.send('Boa Noite, %s' %mensagem).encode()
        
    print("Finalizando conexão com o cliente: ", cliente)
    con.close()

