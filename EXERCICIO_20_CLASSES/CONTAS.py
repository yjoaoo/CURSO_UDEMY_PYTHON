import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    
    @abc.abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f"(DEPOSITO {valor})")

    def detalhes(self, msg=""):
        print(f"O seu saldo é {self.saldo:.2f} {msg}")
        print("---")
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.agencia!r}, {self.conta!r}, {self.saldo!r}"
        return f"{class_name}{attrs}"

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo
        
        print("NÂO FOI POSSIVEL SACAR")
        self.detalhes(f"SAQUE NEGADO {valor}")

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo
        
        print("NÂO FOI POSSIVEL SACAR")
        print(f"Seu limite é {-self.limite:.2f}")
        self.detalhes(f"SAQUE NEGADO {valor}")
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.agencia!r}, {self.conta!r}, {self.saldo!r}, "\
            f"{self.limite!r}"
        return f"{class_name}{attrs}"

if __name__ == "__main__":
    conta_poupanca_1 = ContaPoupanca (111, 222, 0) 
    conta_poupanca_1.sacar(1)
    conta_poupanca_1.depositar(1)
    conta_poupanca_1.sacar(1)
    conta_poupanca_1.sacar(1)
    print("==================")
    conta_corrente_1 = ContaCorrente (111, 222, 0, 100) 
    conta_corrente_1.sacar(1)
    conta_corrente_1.depositar(1)
    conta_corrente_1.sacar(1)
    conta_corrente_1.sacar(1)
    conta_corrente_1.sacar(98)
    conta_corrente_1.sacar(1)
    print("===================")
