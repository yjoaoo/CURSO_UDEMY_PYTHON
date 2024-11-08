 # Lista de listas e seus índices

salas = [
    ["Steve", "Alanzoka", ],
    ["Maethe", ],
    ["tony", "Triz", "joão", ],
]
# print(salas[0][1])
# print(salas[1][0])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f"A sala e {sala}")
    for aluno in sala:
        print(aluno)