def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = saudacao('Bom dia')
falar_bom_noite = saudacao('Bom noite')

for nome in ['Wesley', 'Nayara', 'Helloa', 'Eurides']:
    print(falar_bom_dia(nome))
    print(falar_bom_noite(nome))