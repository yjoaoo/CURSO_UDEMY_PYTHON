# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = "1234"

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = "cpf aluno"

cliente1 = Cliente("João", "Brasil")
cliente1.falar_nome_class()

aluno1 = Aluno("Pedro", "Nascimento")
aluno1.falar_nome_class()
print(aluno1.cpf)