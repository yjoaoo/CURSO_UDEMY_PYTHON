# Faça uma lista de compras com listas
# O usuário deve ter a possibilidade de 
# inserir, apagar e listar valores da sua lista
lista = []
while True:
    entrada = input("Escolha: Inserir[i] Apagar[a] Listar[l]: ")

    if len(entrada) > 1:
        print("Digite apenas i , a ou l.")

    elif entrada == "i":
        item = input("Escolha um item para inserir: ")
        lista.append(item)
        print("Item inserido! Ui")
        

    elif entrada == "a":
        item = input("Escolha um item para Apagar: ")
        if item in lista:
            lista.remove(item)
            print("Item removido com sucesso! :(")
    
    elif entrada == "l":
        if lista:
            print("Aqui está sua lista:")
            print(lista)
    else:
        print("Por escolha 'i', 'a' ou 'l'")

        sair = input("Quer sair? [s]im ou [N]ão: ")
        sair = sair.lower()
        sair = sair.startswith("s")
        print(sair)

        if sair is True:
            print("Você saiu da lista de compras por favor não volte mais!")
            break




        
    
  

