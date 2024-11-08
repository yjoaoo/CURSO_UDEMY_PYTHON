# Lembre-se de desempacontameto


x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#   return x + y

def soma(*args):
    total = 0
    for numero in args:
        print("Total", total, numero)
        total = total + numero
        print("Total", total)
    print(total)

soma(1, 2, 3, 4, 5, 6, 7)