"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=} {z=}", x + y)

soma(55, 10)
soma(123, 1010)
soma(31, 10)
soma(2, 12)
soma(y=9, z=2, x=6)