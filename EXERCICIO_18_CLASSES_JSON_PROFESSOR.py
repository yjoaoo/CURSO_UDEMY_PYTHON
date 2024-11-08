#======================================= AULA_A ==============================

import json

CAMINHO_ARQUIVO = "aula127.json"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa("joão", 20)
p2 = Pessoa("Helena", 21)
p3 = Pessoa("Joana", 11)
bd = [vars(p1), p2.__dict__,vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, "w") as arquivo:
        print("FAZENDO DUMP")
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print("ELE É O __MAIN__")
    fazer_dump()

#======================================= AULA_B ==============================

import json

# from aula127_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

with open(CAMINHO_ARQUIVO, "r") as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)


#======================================= AULA_JSON ==============================

[
  {
    "nome": "João",
    "idade": 33
  },
  {
    "nome": "Helena",
    "idade": 21
  },
  {
    "nome": "Joana",
    "idade": 11
  }
]
