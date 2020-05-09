# -*- coding: utf-8 -*-

minha_lista = ["abacaxi", "melancia", "abacate"]
print(minha_lista)

minha_lista_2 = [1,2,3,4,5]
print(minha_lista_2)

minha_lista_3 = ["abacaxi", 1, 2, True]
print(minha_lista_3)

print(minha_lista[1])

for item in minha_lista:
    print(item)

minha_lista.append("limão")
print(minha_lista)

if 3 in minha_lista_2:
    print("3 está na lista")

del minha_lista[2:]
print(minha_lista)

del minha_lista
#print(minha_lista)

minha_lista_4 = []
print(minha_lista_4)

minha_lista_4.append(4)
print(minha_lista_4)

lista = [123,159,45,65,2,8,1,55,48,1000]
print(lista)

sorted(lista)
print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista.reverse()
print(lista)

lista2 = ["bola", "sapato", "livro"]
print(lista2)

lista2.sort()
print(lista2)

lista2.sort(reverse=True)
print(lista2)