# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def converter_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade
        }
        
pessoa1 = Pessoa("Joao", 19)
pessoa2 = Pessoa("Pedro", 30)

print(pessoa1.nome)
print(pessoa1.idade)

print(vars(pessoa1))
print(vars(pessoa2))

pessoas = [pessoa1.converter_dict(), pessoa2.converter_dict()]

with open("EXERCICIO_18_CLASSES_JSON_2", "w") as json_file:
    json.dump(pessoas, json_file, indent=4)


print("Dados salvos em 'EXERCICIO_18_CLASSES_JSON_2'")

