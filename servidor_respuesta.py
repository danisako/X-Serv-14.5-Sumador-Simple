#!/usr/bin/python3

"""
Daniel Suarez Muñoz
Grado en Ing. en Sistemas de Telecomunicaciones
Ejercicio: Servidor-Simple
"""

import socket
import random	
import calculadora
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysocket.bind(('localhost', 1237))
mysocket.listen(5)


try:
	while True:
		print('Waiting a request')
		(recvSocket, address) = mysocket.accept()
		#proceso peticion
		print('HTTP request received:')
		peticion = str(recvSocket.recv(1024),'utf-8')
		print(peticion)
		recurso = peticion.split()[1] 
		print('Resource:',recurso)
		_,op1,operando,op2=recurso.split('/') 
		print(op1,operando,op2)
		
		
		num1=int(op1)
		num2=int(op2)
		resultado = calculadora.operaciones[operando](num1,num2)

		respuesta = bytes('HTTP/1.1 200 OK\r\n\r\n' + str(resultado), 'utf-8')

		recvSocket.send(respuesta)
		recvSocket.close()
except KeyboardInterrupt:
    print('Closing binded socket')
mysocket.close()

