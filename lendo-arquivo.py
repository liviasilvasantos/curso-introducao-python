# -*- coding: utf-8 -*-

arquivo = open("lendo_arquivo.txt")

linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
  print("linha = ", linha)

arquivo.close()



w = open("arquivo2.txt", "a")

w.write("esse é o meu arquivo")
w.close()
