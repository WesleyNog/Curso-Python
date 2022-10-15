print('COMISÃO')
print()

meta_loja = 50000
taxa_comissao = ''
total_loja = []
y = 0

qnt_vendedora = int(input('Quantas vendedoras? '))
while True:
    if qnt_vendedora >= y:
        loja = input('Loja: ')
        vendedora = input('Vendedor(a): ')
        venda = input('Valor da Venda: ')
        if not venda.isalpha():
            venda = float(venda)
            break
        else:
            print('APENAS NÚMEROS!')
        print(f'A comissão da {vendedora} é de R$ {venda * float(taxa_comissao):.2f}')
    else:
        print(f'O total de vendas é de R$ {venda * float(taxa_comissao):.2f}')
    y += 1

    
    if venda <= 25000:
        taxa_comissao = 0.007
    elif venda >= 25000 and venda <= 35000:
        taxa_comissao = 0.011
    elif venda >= 35000 and venda <= 50000:
        taxa_comissao = 0.025
    elif venda > 50000:
        taxa_comissao = 0.03
