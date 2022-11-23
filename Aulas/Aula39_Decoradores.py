def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print('Ok, agora foi decorado.')
        return resultado
    return interna
    
@criar_funcao
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param te que ser uma String')



invertida = inverte_string('Wesley')
print(invertida)