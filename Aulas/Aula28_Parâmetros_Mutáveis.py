def lista_de_clientes(clientes_iteraveis, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteraveis)
    return lista

cliente1 = lista_de_clientes(['Wesley', 'Nayara', 'Helloa'])
cliente2 = lista_de_clientes(['Valnides', 'Eurides', 'Valter'])
cliente3 = lista_de_clientes(['Valjunior', 'Jamile'])

print(cliente1)
print(cliente2)
print(cliente3)
