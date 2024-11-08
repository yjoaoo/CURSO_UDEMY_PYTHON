# Dictionary Comprehension e Set Comprehension

produto = {
    "nome": "caneta azul",
    "preco": 1.50,
    "categoria": "escitorio",
}

dictionary_comprehension = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != "categoria"
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(6)}
print(s1)