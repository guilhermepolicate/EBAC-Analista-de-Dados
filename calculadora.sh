#!/bin/bash

print("ola, bem vindo a minha calculadora \n")

num1 = float(input("informe o primeiro número \n"))

num2 = float(input("informe o segundo número \n"))

operacao = input("+ = soma, - = subtração, * = multiplicação, / = divisão")

if operacao == "+":
	resultado = num1 + num2

elif operacao == "-":
	resultado = num1 - num2

elif operacao == "*":
	resultado = num1 * num2

elif operacao == "/":
	if num2 != 0:
		resultado = num1 / num2
	else:
		resultado = "essa é uma operação invalida"

print ("resultado =", resultado)
