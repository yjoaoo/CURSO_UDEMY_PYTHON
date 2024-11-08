# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
lista = []
desfeitos = []

while True:
    print("\n--- Lista de Tarefas ---")
    print("Comandos: 'Listar', 'Desfazer', 'Refazer'")
    print("Escolha uma Tarefa ou Comando")

    comando = str(input("Comando ou Tarefa: ")).strip()

    if comando.lower() == "lsita" or comando.lower() == "l":
        print("Aqui está sua lista: ")
        for item in lista:
            print(item)
    elif comando.lower() == "desfazer":
        if lista:
            ultimo_item = lista.pop()
            desfeitos.append(ultimo_item)
            print(f"Desfeitos: {ultimo_item}")
        else:
            print("Não há itens para desfazer.")
    elif comando.lower() == "refazer":
        if desfeitos:
            item_refeito = desfeitos.pop()
            lista.append(item_refeito)
            print(f"Refeito: {item_refeito}")
        else:
            print("Não há itens para refazer.")

    else:
        lista.append(comando)
        desfeitos.clear()  

    sair = input("Quer sair? [s]im ou [n]ão: ").strip().lower()
    if sair == 's':
        print("Você saiu da lista de tarefas. Até a próxima!")
        break   

   



