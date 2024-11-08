while True:
    
        numero_1 = input ("Digite um número: ")
        numero_2 = input ("Digite outro numero: ")
        operador = input ("Digte um operador que você queira usar EX -, +, /, *: ")

        try:
            int_numero_1 = int (numero_1)
            int_numero_2 = int (numero_2)
        except ValueError:
            print("Erro: Certifique-se de inserir apenas números.")

        if operador == "-" :
            print ({int_numero_1 - int_numero_2})

        elif operador == "+" :
            print ({int_numero_1 + int_numero_2})

        elif operador == "*" :
            print ({int_numero_1 * int_numero_2})

        elif operador == "/" :
            print ({int_numero_1 / int_numero_2})
    

        sair = input("Quer sair? [s]im: ")
        sair = sair.lower()
        sair = sair.startswith("s")
        print(sair)

        if sair is True:
            break
   
    