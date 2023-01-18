class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 1234


call1 = CallMe('64351684654')
retorno = call1('Wesley Nogueira')
print(retorno)