# LIST COMPREHEINSION COM MAIS DE UM FOR

lista = []
for i in range(3):
    for x in range(3):
        lista.append((i, x))

lista = [
    (i, x)
    for i in range(3)
    for x in range(3)
]

# lista = [
#     [(i, letra) for letra in "Joao"]
#     for i in range (3)
# ]

print(lista)