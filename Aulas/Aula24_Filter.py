from Dados import produtos, pessoas, lista

def filtrar(pessoa):
    if pessoa['idade'] < 18:
        return True
    else:
        return False

nova_lista = filter(filtrar, pessoas)

for a in nova_lista:
    print(a)
