# importacao das bibliotecas
from socket import * # sockets
import subprocess

def readFile():      # funcao que retorna conteudo do arquivo
    with open('arquivo.txt') as f:
        line = f.read()
    f.close()
    return line

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

while 1:
    connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
    request = connectionSocket.recv(1024) #recebe dados do cliente
    request = request.decode('utf-8')
    response = subprocess.check_output(request, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
    print ('Cliente %s enviou: %s, transformando em: %s' % (addr, request, response))
    connectionSocket.send(response.encode('utf-8'))
    connectionSocket.close() #encerrra o socket com cliente
# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor