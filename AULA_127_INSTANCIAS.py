# Métodos em instâncias de classes Python
# Hard coded = É algo que foi escrito diretamente no codígo

class Carro:
    def __init__(self, nome):
        self.nome = nome # HARD CODED

    def acelerar(self):
        print(f"{self.nome} está acelerando...")
        

fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()

celta = Carro("Celta")
print(celta.nome)
celta.acelerar()