#!/usr/bin/python3

"""
Daniel Suarez Muñoz
Grado en Ing. en Sistemas de Telecomunicaciones
Ejercicio: Calculadora
"""

import sys

def suma(num1,num2):
	return num1 + num2


def resta(num1,num2):
	return num1 - num2


def division(num1,num2):
	return num1/num2
		


def multiplicacion(num1,num2):
	return num1*num2



operaciones = {
	'suma': suma,
	'resta': resta,
	'division': division,
	'multiplicacion': multiplicacion
}



if __name__ == "__main__":

	len_args = len(sys.argv)
	if len_args != 4:
		sys.exit("Se ha producido un error, introduce 3 parámetros")

		operacion = sys.argv[1] 
		num1 = float(sys.argv[2])
		num2 = float(sys.argv[3])

		resultado = operaciones[operacion](num1,num2)
		print("Resultado: ", resultado)


 #ASIGNAMOS NOMBRES A LOS ARGUMENTOS PARA TRABAJAR MAS COMODOS
