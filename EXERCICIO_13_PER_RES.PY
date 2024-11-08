# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
   },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
       'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

while True:
    
    for pergunta in perguntas:
        print(f'Pergunta:', pergunta["Pergunta"])
        print(f'Opções:', pergunta["Opções"])
        resposta_usul = input("Digite uma das opções: ")
        if resposta_usul == pergunta["Resposta"]:
            print("Você acertou")
        else:
            print("Resposta errada burro!")
            break
    else:
        print("Você conseguiu!!!")
        break
      














# while respostas:
#     gabarito = ["4", "25", "5"]
#     resposta_usu = input("Qual a sua resposta: ")
#     if resposta_usu in gabarito:
#         print("Parabéns")
#         resposta_usu == False
#     break
            






    