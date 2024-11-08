import CONTAS

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome 
        self.idade = idade 

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome 

    @property
    def idade (self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade 

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.nome!r}, {self.idade!r}"
        return f"{class_name} {attrs}"

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: CONTAS.Conta | None = None

if __name__ == "__main__":
    cliente_1 = Cliente ("Joao", 19)
    cliente_1.conta = CONTAS.ContaCorrente(111, 222, 0, 0)
    print(cliente_1)
    print(cliente_1.conta)
    cliente_2 = Cliente ("Pedro", 25)
    cliente_2.conta = CONTAS.ContaCorrente(112, 223, 100, 100)
    print(cliente_2)
    print(cliente_2.conta)
