# Manipulando chaves e valores em dicionarios
pessoa = {}

##
##

chave = "Nome"

pessoa[chave] = "João Pedro"
pessoa["Sobrenome"] = "Brasil"

print(pessoa[chave])

pessoa[chave] = "Pedro"

del pessoa["Sobrenome"]
print(pessoa)
print(pessoa["Nome"])

#print(pessoa.get("Sobrenome"))
if pessoa.get("Sobrenome") is None:
    print("NÃO EXISTE")
else:
    print(pessoa["Sobrenome"])

# print("ISSO NÃO VAI!")
