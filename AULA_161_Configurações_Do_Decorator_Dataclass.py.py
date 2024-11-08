from dataclasses import dataclass


@dataclass(init=False)
@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(p1)
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)

# ================================== asdict e astuple em dataclasses =====================

print()
from dataclasses import dataclass
from dataclasses import asdict, astuple, dataclass


@dataclass(repr=True)
@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])