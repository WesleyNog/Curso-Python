class Animal():
    def __init__(self, nome) -> None:
        self.nome = nome


    def comendo(self, alimento):
        return f'O {self.nome} está comendo um(a) {alimento}'


    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('Abacate'))
print(leao.executar('Maçã'))