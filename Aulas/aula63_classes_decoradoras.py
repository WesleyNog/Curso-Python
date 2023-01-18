class Multiplicar:
    def __init__(self, multiplicador) -> None:
        self.multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interna

@Multiplicar(5)
def soma(x, y):
    return x + y

result = soma(2, 4)
print(result)