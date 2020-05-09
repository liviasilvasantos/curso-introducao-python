lista1 = [1,2,3,4,5,6,7]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = [2.0, 3.99,1.99 ]

for numero, nome in zip(lista1, lista2):
    print(numero, nome)


for numero, nome, preco in zip(lista1, lista2, lista3):
    print(numero, nome, preco)