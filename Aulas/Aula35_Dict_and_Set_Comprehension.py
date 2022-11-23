dict = {
    'nome': 'caneta',
    'preco': 2.5,
    'categoria': 'escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in dict.items()
    if chave != 'categoria'
}

print(dc)

s1 = {i for i in range(10)}

print (s1)