import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade})"

with open("EXERCICIO_18_CLASSES_JSON_2", "r") as json_file:
    dados = json.load(json_file)

pessoas = [Pessoa(d['nome'], d['idade']) for d in dados]


for pessoa in pessoas:
    print(pessoa)
        
        