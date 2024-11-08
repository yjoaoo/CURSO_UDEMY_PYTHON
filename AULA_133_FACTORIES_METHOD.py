# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

# class Pessoa:
#     ano = 2023 # ATRIBUTO DE CLASSE

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     @classmethod
#     def metodo_de_classe(cls):
#         print("Hey")

#     @classmethod
#     def criar_com_50_anos(cls, nome):
#         return cls(nome, 50)
    
#     @classmethod
#     def criar_sem_nome(cls, idade):
#         return cls("Anônima", idade)

# p1 = Pessoa('João', 34)
# p2 = Pessoa.criar_com_50_anos('Helena')
# p3 = Pessoa('Anônima', 23)
# p4 = Pessoa.criar_sem_nome(25)
# print(p2.nome, p2.idade)
# print(p3.nome, p3.idade)
# print(p4.nome, p4.idade)
# # print(Pessoa.ano)
# # Pessoa.metodo_de_classe()


# ===============================================================================


class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def mostrar_saldo(self):
        print(f"Saldo atual de {self.nome}: R$ {self.saldo:.2f}")

    @classmethod
    def criar_com_bonus(cls, nome, saldo):
        saldo_com_bonus = saldo + 100
        return cls(nome, saldo_com_bonus)
    

# Criando uma conta bancária normalmente
conta1 = ContaBancaria("João", 500.0)
conta1.mostrar_saldo()

# Criando uma conta bancária com bônus usando o método fábrica
conta2 = ContaBancaria.criar_com_bonus("Maria", 500.0)
conta2.mostrar_saldo()

# Depositando dinheiro na conta com bônus
conta2.depositar(200)
conta2.mostrar_saldo()

