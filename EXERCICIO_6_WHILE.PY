#Interando strings com while
nome = "Joao Pedro"
print(nome)

nova_str = ''
contador = 0
 
while contador < len(nome):
    nova_str += '*' + nome[contador]
    contador += 1
 
print(nova_str)

