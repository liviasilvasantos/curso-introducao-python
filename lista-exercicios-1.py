import math

#1. Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   
idade_usuario = int(input("Qual a sua idade? "))

maior_menor = ""

if idade_usuario >= 18:
    maior_menor = "maior"
else:
    maior_menor = "menor"
print("você é", maior_menor, "de idade")

#2. Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) /2

if media >= 6:
    print("média:", media, "- aprovado")
else:
    print("média:", media, "- reprovado")

#3. Escreva um programa que resolva uma equação de segundo grau.   
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b * b - 4 * a * c
print(delta)

if delta<0:
    print("Delta negativo")
else:
    x1 = (-1 * b - math.sqrt(delta)) / 2 * a
    x2 = (-1 * b + math.sqrt(delta)) / 2 * a

    print("x1=", x1, ", x2=", x2)

#4. Escreva um programa que ordene uma lista numérica com três elementos.   
lista_numerica = []
lista_numerica.append(int(input("Digite um número inteiro:")))
lista_numerica.append(int(input("Digite um número inteiro:")))
lista_numerica.append(int(input("Digite um número inteiro:")))

lista_numerica.sort()
print(lista_numerica)

#5. Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.  
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
sinal = input("Digite o sinal:")

if sinal == "+":
    print(n1 + n2)
elif sinal == "-":
    print(n1 - n2)
elif sinal == "*":
    print(n1*n2)
elif sinal == "/":
    print(n1/n2)
else:
    print("operação inválida")