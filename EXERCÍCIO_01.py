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
    n_de_filhos = input('Quantos? ')
else:
    n_de_filhos = 0
idade = 2022 - int(nascimento)
margem_minima = 1200
margem_maior = 4000
renda = float(renda)
n_de_filhos = int(n_de_filhos)


if idade >= 18 and idade <= 40 and emprego == 'Sim' and renda > margem_minima:
    valor_emprestimo = input('Valor do Empréstimo: ')
else:
    valor_emprestimo = 0
    print('No momento não podemos atender a sua solicitação, tente novamete daqui à 3 (três) meses!')
    print('Obrigado por usar nossos serviços.')

valor_emprestimo = float(valor_emprestimo)

if estado_civil == 'Casado':
    renda_familiar = renda / 2
else:
    renda_familiar = renda

if filhos == 'Sim':
    renda_familiar = renda / n_de_filhos
else:
    renda_familiar = renda
renda_familiar = float(renda_familiar)

if estado_civil != 'Sim' and filhos != 'Sim':
    parcela_emprestimo = input('Parcela: ')
    parcela_emprestimo = float(parcela_emprestimo)
    juros = (0.085 * parcela_emprestimo)
    divida_emprestimo = valor_emprestimo * juros + valor_emprestimo
    valor_parcela = divida_emprestimo / parcela_emprestimo

    print(divida_emprestimo)
    print(valor_parcela)
else:
    parcela_emprestimo = input('Parcela: ')
    parcela_emprestimo = float(parcela_emprestimo)
    juros = (0.067 * parcela_emprestimo)
    divida_emprestimo = valor_emprestimo * juros + valor_emprestimo
    valor_parcela = divida_emprestimo / parcela_emprestimo

    print(divida_emprestimo)
    print(valor_parcela)
