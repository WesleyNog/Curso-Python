#LIST COMPREHENSION

l1 = [1, 2, 3, 4, 5, 6]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['wesley', 'naiara', 'helloa']
ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]

print(ex7)

#LIST COMPREHENSION 02

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novos_numeros = [numero for numero in numeros if numero > 5]
impares = [numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]
outro_if = [
    numero
    if numero != 6 else 600
    for numero in pares
]

print(numeros)
print(novos_numeros)
print(impares)
print(pares)
print(outro_if)

#LIST COMPREHENSION 03

nomes = ['wesley', 'naiara', 'helloa', 'eurides']
novos_nomes = [f'{nome[:-1]}{nome[-1].upper()}' for nome in nomes]

print(novos_nomes)

numeros = [[numero, numero ** 2] for numero in range(10)]

print(numeros)
