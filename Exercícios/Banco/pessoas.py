import conta

# Outra Classe Abstata
class People:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'

class Client(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.conta: conta.Conta | None = None


if __name__ == '__main__':
    c1 = Client('Wesley', 34)
    c1.conta = conta.ContaCorrente(111, 222 ,0 ,0)
    print(c1)
    print(c1.conta)
    print()
    c2 = Client('Naiara', 29)
    c2.conta = conta.ContaPoupanca(333, 444, 0)
    print(c2)
    print(c2.conta)