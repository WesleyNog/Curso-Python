secreto = 'catraca'
digitado = []
chances = 3

while True:
    if chances <= 0:
        print('VOCÊ PERDEU!!')
        break

    letra = input('Digite um Letra: ')

    if len(letra) > 1:
        print('Olha a trapaça, Digite apenas UMA letra!')
        continue
    digitado.append(letra)

    if letra in secreto:
        print(f'Acertou, a letra "{letra.upper()}" existe na palavra!')
    else:
        print(f'ERROU, a letra "{letra.upper()}" não existe na palavra!')
        digitado.pop()

    secreto_temporario = ''
    for letra_secreto in secreto:
        if letra_secreto in digitado:
            secreto_temporario += letra_secreto
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Uhull, VOCÊ GANHOU!!! A palavra era: "{secreto_temporario}"')
        break
    else:
        print(f'A palavra secreta está assim: "{secreto_temporario}"')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
