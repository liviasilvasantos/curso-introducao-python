dicionario_sites = {"Diego":"diegomariano.com"}

print(dicionario_sites["Diego"])

sobrenomes = {"Lívia":"Silva Santos", "Rafael": "Pereira de Sousa", "Elvis": "Pequenos Leões"}

print(sobrenomes)

for chave in sobrenomes:
    print(chave + " - " + sobrenomes[chave])

for i in sobrenomes.items():
    print(i)

for valor in sobrenomes.values():
    print(valor)