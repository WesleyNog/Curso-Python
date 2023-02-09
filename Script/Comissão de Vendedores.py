meta_loja = 50000
texto = ''
vendedoras = []
total_venda = []
lojas = []
y = 0

print('COMISÃO')
print()

def calculo(vendedora, venda):
    print(f'A comissão da {vendedora} é de R$ {calcular_comissao(venda):.2f}')
    print('-' * 30)


def resultado():
    print()
    print(f'O total da KEDMA é R$ {sum(total_venda):.2f}')
    print(f'A comissão da KEDMA é R$ {sum(total_venda) * comissao(sum(total_venda)):.2f}')
    print('Fim!')

def calcular_comissao(venda):
    return venda * comissao(venda)
    
def comissao(venda):
    if venda <= 25000:
        return 0.007
    elif venda >= 25000 and venda <= 35000:
        return 0.011
    elif venda >= 35000 and venda <= 50000:
        return 0.025
    else:
        return 0.03


def ler_string(texto):
    str = ''
    while (len(str) < 3):
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
    # exibir comissao da vendadora
    calculo(vendedora, venda)
    total_venda.append(venda)
    y += 1

for a, b in zip(vendedoras, total_venda):
    texto += f'\nA comissão de {a} é R$ {b * comissao(b):.2f}'
print(texto)
resultado()
