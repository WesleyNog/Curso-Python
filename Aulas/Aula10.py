while True:
    print()
    num_1 = input('Nº 01: ')
    num_2 = input('Nº 02: ')
    operador = input('Operação: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Digite um número!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido')
