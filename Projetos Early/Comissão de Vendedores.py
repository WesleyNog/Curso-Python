meta_loja = 50000
texto = ''
vendedoras = []
total_venda = []
lojas = []
y = 0

print('COMISÃO')
print()

def calculo(vendedora, taxa_comissao):
    print(f'A comissão da {vendedora} é de R$ {taxa_comissao:.2f}')
    print('-' * 30)


def resultado():
    print()
    print(f'O total da {loja} é R$ {sum(total_venda):.2f}')
    print(f'A comissão da {loja} é R$ {sum(total_venda) * 0.015:.2f}')
    print('Fim!')

def comissao(venda):
    if venda <= 25000:
        0.007
    elif venda >= 25000 and venda <= 35000:
        0.011
    elif venda >= 35000 and venda <= 50000:
        0.025
    elif venda > 50000:
        0.03

def ler_string(texto):
    str = ''
    while (size(str) < 3):
        str = input(texto)
    return str

qnt_vendedora = int(input('Quantas vendedoras? '))
while y < qnt_vendedora:
    # solicitar nome da loja
    loja = ler_string('Loja: ')
    lojas.append(loja)
    # solicitar nome da vendadora
    vendedora = ler_string('Vendedor(a): ')
    vendedoras.append(vendedora)
    # solicitar valor da venda
    venda = input('Valor da Venda: ')
    venda = float(venda)
    # calcula comissao da vendedora
    taxa_comissao = comissao()
    # exibir comissao da vendadora
    calculo(vendedora, taxa_comissao)
    total_venda.append(venda)
    y += 1

for a, b in zip(vendedoras, total_venda):
    texto += f'\nA comissão de {a} é R$ {b}'
print(texto)
resultado()
