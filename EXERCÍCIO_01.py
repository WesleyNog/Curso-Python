print('ANÁLISE DE EMPRÉSTIMO')

nome = input('Nome: ')
nascimento = input('Nascimento: ')
emprego = input('Trabalha? ')
if  emprego == 'Sim':
    renda = input('Salário: ')
else:
    renda = 0
    print('NÃO Elegível')
    exit

estado_civil = input('Estado Civil: ')
filhos = input('Tem filhos? ')
if filhos == "Sim":
    input('Quantos? ')
idade = 2022 - int(nascimento)

if idade < 18 || idade > 40:
  print('NÃO Elegível')
  exit

margem_minima = 1200
margem_maior = 4000
renda = int(renda)

if renda > margem_minima:
    print('Elegível')
else:
    print('NÃO Elegível')

