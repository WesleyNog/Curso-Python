from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(
     default='Missing'    
    )
    sobrenome: str = 'Not Send'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)