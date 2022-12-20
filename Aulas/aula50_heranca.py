class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente('Wesley', 'Nogueira')
c1.falar_nome_class()
a1 = Aluno('Helloa', 'Soares')
a1.falar_nome_class()