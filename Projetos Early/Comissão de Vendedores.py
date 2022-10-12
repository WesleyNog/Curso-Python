print('COMISÃO')
print()

meta_loja = 50000
taxa_comissao = ''
ifood = 8022,60
rappi = 205,80

vendedora = input('Vendedor(a): ')
loja = input('Loja: ')
venda = input('Valor da Venda: ')

if float(venda) <= 25000:
    taxa_comissao = 0.007
elif float(venda) >= 25000 and float(venda) <= 35000:
    taxa_comissao = 0.011
elif float(venda) >= 35000 and float(venda) <= 50000:
    taxa_comissao = 0.025
elif float(venda) > 50000:
    taxa_comissao = 0.03

print(f'A comissão da {vendedora} é de R$ {float(venda) * float(taxa_comissao):.2f}')
