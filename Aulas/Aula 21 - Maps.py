from Dados import produtos, pessoas, lista

# Iterado com os preços:
def aumento_de_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novos_produtos = map(aumento_de_preco, produtos)

for produto in novos_produtos:
    print(produto)

# Iterado com os pessoas:
nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
