import json

pessoa = {
    'nome': 'Joao Pedro',
    'sobrenome': 'Brasil',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.7,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open("AULA120.json", "w", encoding="utf8") as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open("AULA120.json", "r", encoding="utf8") as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa["nome"])