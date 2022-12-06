nome = 'Wesley Nogueira'
idade = 36
altura = 1.75
peso = 65
imc = peso / altura ** 2
ano_atual = 2022
ano_de_nascimento = ano_atual-idade

print('{} tem, {} anos, {} de altura e pesa {}kg.'.format(nome, idade, altura, peso))
print('O IMC de {} é {:.2f}.'. format(nome, imc))
print('{} nasceu em {}.'. format(nome, ano_de_nascimento))
