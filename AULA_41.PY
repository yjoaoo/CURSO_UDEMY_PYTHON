# WHILE / ELSE 
# i = index

strint = "Valor qualquer"

i = 0 
while i < len (strint):
    letra = strint[i]

    if letra == " ":
        break

    print(letra)
    i += 1
else:
    print("Não encontrei um espaço na string.")
print("Fora do while.")