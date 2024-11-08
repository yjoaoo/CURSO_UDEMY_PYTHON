# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
# Criar um sistema bancário (extremamente simples) que tem clientes, contas e
# um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
# possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

from abc import ABC, abstractmethod



class Conta (ABC):
    def __init__(self, agencia, numero, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
    @abstractmethod
    def saque(self, valor):
        ...
    def depositar(self, valor):
        self.saldo += valor
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta
class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo=0, limite_extra=0):
        super().__init__(agencia, numero, saldo)
        self.limite_extra = limite_extra

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        
class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo=0, taxa_juros=0.01):
        super().__init__(agencia, numero, saldo)
        self.taxa_juros = taxa_juros

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    
class Banco:
    def __init__(self):
        self.lista_clientes = []
        self.lista_contas = []

    def adicionar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.lista_contas.append(conta)

    def autenticar(self, cliente, conta):
        if cliente not in self.clientes:
            return False
        
        if cliente not in self.clientes:
            return False

        if conta not in self.contas:
            return False

        if cliente.conta != conta:
            return False
    def sacar(self, cliente, conta, valor):
        if self.autenticar(cliente, conta):
            if conta.saque(valor):
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Falha na autenticação. Saque não autorizado.")

    def depositar(self, cliente, conta, valor):
        if self.autenticar(cliente, conta):
            conta.depositar(valor)
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Falha na autenticação. Depósito não autorizado.")    


    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
# Dicas:
# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#     polimorfismo - as subclasses que implementam o método sacar)
# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.
