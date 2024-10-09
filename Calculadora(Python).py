#calculadora
print("Olá! bem vindo a minha calculadora.")
print("\n")
nome1 = input("Por favor digite seu primeiro nome: \n")
nome2 = input("Por favor digite último sobrenome nome: \n")

print("\n")
print("Olá ", nome1 + " " + nome2)
print("\n")

num1 = int(input("Por favor digite o primeiro número de 0 a 9: \n"))
print("O primeiro número é: ", num1, "\n")
while (num1 > 9) or (num1 < 0):
  num1 = int(input("Por favor digite um número de 0 a 9: \n"))

num2 = int(input("Por favor digite o segundo número de 0 a 9: \n"))
print("O segundo número é: ", num2, "\n")
while (num2 > 9) or (num2 < 0):
  num2 = int(input("Por favor digite um número de 0 a 9: \n"))

soma = num1 + num2
print("O resultado da soma é do tipo ",(type(soma)))
print("\n")

subtracao = num1 - num2
print("O resultado da subtração é do tipo ",(type(subtracao)))
print("\n")

multiplicacao = num1 * num2
print("O resultado da Multiplicação é do tipo ",(type(multiplicacao)))
print("\n")

divisao = num1 / num2
print("O resultado da Divisão é do tipo ",type(divisao))
print("\n")

inteiro = num1 // num2
print("O resultado da Divisão do tipo inteiro e sempre ",type(inteiro))
print("\n")

resto = num1 % num2
print("O resto da divisão é um numro do tipo", type(resto))
print("\n")

exponenciacao = num1 ** num2
print("O resultado da exponenciação e do tipo", type(exponenciacao))
print("\n")

if (num1 == num2):
  print("O primeiro número é igual ao segundo")
else:
  print("O primeiro número não é igual ao segundo")
print("\n")

if(num1 != num2):
  print("O primeiro número é diferente do segundo")
else:
  print("O primeiro número não é diferente do segundo")
print("\n")

if (num1 > num2):
  print("O primeiro número é maior que o segundo")
else:
  print("O primeiro número não é maior que o segundo")
print("\n")

if (num1 < num2):
  print("O primeiro número é menor que o segundo")
else:
  print("O primeiro número não é menor que o segundo")
print("\n")

if (num1 >= num2):
  print("O primeiro número é maior ou igual que o segundo")
else:
  print("O primeiro número não é maior ou igual que o segundo")
print("\n")

if (num1 <= num2):
  print("O primeiro número é menor ou igual que o segundo")
else:
  print("O primeiro número não é menor ou igual que o segundo")
print("\n")

print("A soma do primeiro com o segundo é ", soma)
print("A subtração do primeiro com o segundo é ", subtracao)
print("A multiplicação do primeiro com o segundo é ", multiplicacao)
print("A divisão do primeiro com o segundo é ", divisao)
print("A divisão inteira do primeiro com o segundo é ", inteiro)
print("O resto da divisão do primeiro com o segundo é ", resto)
print("A exponenciação do primeiro com o segundo é ", exponenciacao)
print("O primeiro número é igual ao segundo? ", num1 == num2)
print("O primeiro número é diferente do segundo? ", num1 != num2)
print("O primeiro número é maior que o segundo? ", num1 > num2)
print("O primeiro número é menor que o segundo? ", num1 < num2)
print("O primeiro número é maior ou igual que o segundo? ", num1 >= num2)
print("O primeiro número é menor ou igual que o segundo? ", num1 <= num2)
