produtos = {'arroz': 2.5, 'feijão': 4.75,
            'macarrão': 1.25, 'suco': 0.50,
            'frango': 15
            }
qnt = ''
prod = ''
somado = []
y = 0

print('Mercearia')
print()

def saudacao():
    print()
    print(f'Total da compra: R$ {sum(somado):.2f}')
    print('Volte SEMPRE!')


def soma():
    somar = produtos[prod] * float(qnt)
    print(somar)
    somado.append(somar)
    print('-' * 30)


while True:
    repeat = input('Terminar[1] ou Continuar[ENTER]')
    if repeat != '1':
        prod = input('Escolha o produto:').lower()
        qnt = input('Quantidade: ')
        soma()
    else:
        saudacao()
        break
        
