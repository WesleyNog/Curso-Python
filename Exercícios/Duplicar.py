## Minha Resolução!

# def duplicar(x):
#     return x * 2


# def triplicar(x):
#     return x * 3


# def quadruplicar(x):
#     return x * 4

# numero = int(input('Digite um número: '))

# print(f'O número {numero} quando:')
# print(f'Duplicado = {duplicar(numero)}')
# print(f'Triplicado = {triplicar(numero)}')
# print(f'Quadruplicado = {quadruplicar(numero)}')

## Resolição do Professor!

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))