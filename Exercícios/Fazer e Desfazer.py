# lista de afazeres
lista = []
temp_list = []

# Definindo afazeres
def adicionar(acao):
    if acao != 'desfazer' or 'refazer' or 'sair':
        return lista.append(acao)

# Logica de Desfazer e Refazer
def undo_redo(acao):
    if 'desfazer' in lista:
        if not lista:
            print('Nada para desfazer!')
            print()
        else:
            temp_list.append(lista[-2])
            lista.remove(temp_list[-1])
    elif 'refazer' in lista:
        if not temp_list:
            print('Nada pra refazer!')
            print()
        else:
            lista.append(temp_list[-1])
            temp_list.pop()

# Código
while True:
    comando = adicionar(input('Digite um comando: ').lower())
    if 'sair' in lista:
        break


    undo_redo(comando)
    
    if 'desfazer' in lista:
        lista.remove('desfazer')
    elif 'refazer' in lista:
        lista.remove('refazer')

    print(*lista, sep='\n')
    print()
