# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    ...

p1 = Pessoa("João", "Pedro")
p1.nome = "João"
p1.sobrenome = "Brasil"

p2 = Pessoa("Eduarda", "Maria")
p2.nome = "João"
p2.sobrenome = "Silva"

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

