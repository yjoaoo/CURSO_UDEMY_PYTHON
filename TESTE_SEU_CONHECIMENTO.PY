"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Qual é o seu nome?: ',)
idade = input('Qual é a sua idade?: ',)

if nome and idade:

    print ('Sua idade é',idade)
    print ('Seu nome é',nome)
    print('Seu nome invertido é:',nome[::-1])
if ' ' in nome:
    print("Seu nome contém espaços")
else:
    print("Seu nome não contem espaços")

numero_letras = len(nome)
print(f"Seu nome tem {numero_letras} letras")

primeira_letra = nome[0]
print(f"A primeira letra do seu nome é {primeira_letra}")

ultima_letra = nome[-1]
print(f"A ultima letra do seu nome é {ultima_letra}")

if not nome or not idade:
    print("Desculpe, você deixou campos vazios.")
