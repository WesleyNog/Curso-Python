print('COMISÃO')
print()


def calculo():
    print(f'A comissão da {vendedora} é de R$ {comissao():.2f}')
    print('-' * 30)


def resultado():
    print()
    print(f'O total da {loja} é R$ {sum(total_venda):.2f}')
    print(f'A comissão da {loja} é R$ {sum(total_venda) * 0.015:.2f}')
    print('Fim!')


def comissao():
    if venda <= 25000:
        taxa_comissao = 0.007
    elif venda >= 25000 and venda <= 35000:
        taxa_comissao = 0.011
    elif venda >= 35000 and venda <= 50000:
        taxa_comissao = 0.025
    elif venda > 50000:
        taxa_comissao = 0.03
    return venda * taxa_comissao

meta_loja = 50000
taxa_comissao = ''
texto = ''
vendedoras = []
total_venda = []
lojas = []
y = 0

qnt_vendedora = int(input('Quantas vendedoras? '))
while y < qnt_vendedora:
    loja = input('Loja: ')
    lojas.append(loja)
    vendedora = input('Vendedor(a): ')
    vendedoras.append(vendedora)
    venda = input('Valor da Venda: ')
    venda = float(venda)
    comissao()
    calculo()
    total_venda.append(venda)
    y += 1

for a, b in zip(vendedoras, total_venda):
    texto += f'\nA comissão de {a} é R$ {b}'
print(texto)
resultado()
