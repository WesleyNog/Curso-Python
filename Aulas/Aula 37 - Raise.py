def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não pode ser zero!')
    return True


def int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n}" Deve int ou float. '
            f'"{tipo_n.__name__}" enviado'
        )
    return True

def divide(n, d):
    int_ou_float(n)
    int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0'))