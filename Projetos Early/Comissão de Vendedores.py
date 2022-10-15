print('COMISÃO')
print()

meta_loja = 50000
taxa_comissao = ''
total_venda = []
y = 0

qnt_vendedora = int(input('Quantas vendedoras? '))
while y < qnt_vendedora:
    loja = input('Loja: ')
    vendedora = input('Vendedor(a): ')
    venda = input('Valor da Venda: ')
    venda = float(venda)
    if venda <= 25000:
        taxa_comissao = 0.007
    elif venda >= 25000 and venda <= 35000:
        taxa_comissao = 0.011
    elif venda >= 35000 and venda <= 50000:
        taxa_comissao = 0.025
    elif venda > 50000:
        taxa_comissao = 0.03
    print(f'A comissão da {vendedora} é de R$ {venda * float(taxa_comissao):.2f}')
    total_venda.append(venda)
    y += 1

print()
print('O valor total é R$%.2f'%sum(total_venda))
print('Fim!')
