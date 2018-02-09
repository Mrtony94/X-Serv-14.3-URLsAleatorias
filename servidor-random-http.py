#!/usr/bin/python3

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        url = random.randint(1, 1000000000000)
        recvSocket.send(bytes('HTTP/1.1 200 Ok \r\n\r\n' +
                        '<html><body><h1>Hola.</h1>' +
                        '<a href="http://localhost:1234/' +
                        str(url) +
                        '" >Dame otra<a/>' +
                        "</p>" +
                        '</body></html>', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
