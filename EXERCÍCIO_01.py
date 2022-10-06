print('ANÁLISE DE EMPRÉSTIMO')

nome = input('Nome: ')
nascimento = input('Nascimento: ')
emprego = input('Trabalha? ')
if  emprego == 'Sim':
    renda = input('Salário: ')
else:
    renda = 0
estado_civil = input('Estado Civil: ')
filhos = input('Tem filhos? ')
if filhos == "Sim":
    input('Quantos? ')
idade = 2022 - int(nascimento)
margem_minima = 1200
margem_maior = 4000
renda = int(renda)

if idade >= 18 and idade <= 40 and emprego == 'Sim' and renda > margem_minima:
    print('Elegível')
else:
    print('NÃO Elegível')
