lista = [
    {'nome': 'Wesley', 'sobrenome': 'Nogueira'},
    {'nome': 'Naiara', 'sobrenome': 'Soares'},
    {'nome': 'Helloa', 'sobrenome': 'Alves'},
    {'nome': 'Eurides', 'sobrenome': 'Nogueira'},
]


# lista.sort(key=lambda item: item['sobrenome'])
# for item in lista:
#     print(item)

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
