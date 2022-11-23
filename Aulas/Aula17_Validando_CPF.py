# Validando CPF

CPF = input('Digite um CPF: ')
novo_cpf = CPF[:9]
reverso = 10
total = 0
for new in range(19):
    if new > 8:
        new -= 9

    total += int(novo_cpf[new]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)
if novo_cpf == CPF:
    print('CPF Válido!')
else:
    print('CPF Invalido!')
