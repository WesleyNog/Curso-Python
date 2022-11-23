# Aula 01
try:
    a = 1/0
except NameError as erro:
    print('Erro do desenvolvedor!')
except (IndexError, KeyError) as erro:
    print('Erro no indice ou chave')
except Exception as erro:
    print('Erro inesperado!')
else:
    print('Seu código foi executado com sucesso')
finally:
    print("Finalmente.")

print('Bora continuar!')

# Aula 02

def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')
    return n1 / n2

try:
    print(divide(n1=1, n2=0))
except ValueError as error:
    print('Você está querendo dividir por 0!')
    print('Log: ', error)
