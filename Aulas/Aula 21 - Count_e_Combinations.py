from itertools import count, combinations, permutations, product

# Primeiro Exemplo
contador = count()
lista = ['wesley', 'naiara', 'helloa']
listar = zip(contador, lista)
print(dict(listar))

# Segundo exemplo
contador2 = count(start=1, step=0.2)

for valor in contador2:
    print(valor)

    if valor >= 10:
        break


# Combinations
contador = count()
lista = ['wesley', 'naiara', 'helloa', 'eurides', 'valnides', 'valter', 'valjunior']

for grupo in combinations(lista, 2):
    print(grupo)
