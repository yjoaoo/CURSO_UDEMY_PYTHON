class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("João", "Brasil")
# p1.nome = "João"
# p1.sobrenome = "Brasil"

p2 = Pessoa("Maria", "Eduarda")
# p2.nome = "Maria"
# p2.sobrenome = "Eduarda"

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)