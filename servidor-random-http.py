#!/usr/bin/python3

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1235))
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        url = str(random.randint(1, 1000000000000))
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><p>Hola. <a href =‘"
                        ‘url’ +
                        " ' >Dame otra</a></p></body></html>" +
                    	"\r\n", 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
   
    