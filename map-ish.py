def dobro(x):
    return x * x

valor = 2
print(dobro(valor))

valor = [1,2,3,4,5]

valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)