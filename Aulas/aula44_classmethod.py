class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('Wesley', 35)
p2 = Pessoa.criar_com_50_anos('Eurides')
p3 = Pessoa.criar_sem_nome(26)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)