from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


p1 = Pessoa('Wesley', 'Nogueira')
p1.nome_completo = 'Naiara Soares Silva'
print(p1)
print(p1.nome_completo)
