def resultado():
    print(f'Você acertou {respostas_certas} perguntas.')
    print(f'Seu percentual de acerto é de {percentual()}%')


def percentual():
    return respostas_certas / qtd_perguntas * 100


perguntas = {
    'pergunta1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': 3,
            'b': 1,
            'c': 4,
            'd': 9,
        },
        'resposta certa!': 'c',
    },
    'pergunta2': {
        'pergunta': 'Quanto é 3*4? ',
        'respostas': {
            'a': 6,
            'b': 12,
            'c': 7,
            'd': -1,
        },
        'resposta certa!': 'b',
    },
    'pergunta3': {
        'pergunta': 'Quanto é 8/4? ',
        'respostas': {
            'a': 4,
            'b': 7,
            'c': 12,
            'd': 2,
        },
        'resposta certa!': 'd',
    },
    'pergunta4': {
        'pergunta': 'Quanto é 7-2? ',
        'respostas': {
            'a': 6,
            'b': 14,
            'c': 5,
            'd': 9,
        },
        'resposta certa!': 'c',
    },
    'pergunta5': {
        'pergunta': 'Quanto é 1*7? ',
        'respostas': {
            'a': 7,
            'b': 10,
            'c': 0,
            'd': 8,
        },
        'resposta certa!': 'a',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Diga sua resposta: ')

    if resposta_usuario == pv['resposta certa!']:
        print('Aew, Acertou!!!')
        respostas_certas += 1
    else:
        print('Iii, errou oh!')

    print()

qtd_perguntas = len(perguntas)
percentual()
resultado()
