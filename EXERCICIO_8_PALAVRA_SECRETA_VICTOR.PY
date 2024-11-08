"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

#palavra_secreta = 'roçando na fivela'
#palavra_secreta = list(palavra_secreta)
palavra_secreta = 'Hilux'
palavra = '*' * len(palavra_secreta)
palavra = list(palavra)
tentativas = 0
indice_valor = list(enumerate(palavra_secreta))

while True:
    digite = input('Digite uma letra: ')

    if digite in palavra_secreta and len(digite) == 1 and digite.isalpha() and digite not in palavra:
        for i, v in indice_valor:
            if v.lower() == digite:
                palavra[i] = v            

    elif len(digite) != 1 or not digite.isalpha():
        tentativas += 1
        print(f'Erro. Digite apenas uma letra. Você fez {tentativas} tentativa(s)')

    elif digite in palavra:
        tentativas += 1
        print(f'Erro, letra já digitada. Você fez {tentativas} tentativa(s)')

    else:
        tentativas += 1
        print(f'Errado. Você fez {tentativas} tentativa(s)')
    
    
    if palavra == palavra_secreta:
        print('Palavra encontrada. Virgindade protegida com sucesso!')
        break

    print(''.join(palavra))

# while True:
#     if sua_descoberta in palavra_secreta:
#         for posicao1 in range(len(palavra_secreta)):
#             for posicao2 in range(len(palavra)):
#                 if sua_descoberta == palavra_secreta[posicao2]:
#                     palavra[posicao2] = sua_descoberta
#                     print(palavra) 
#                     sua_descoberta = input('Digite uma letra: ')
#             break
#     else:
#         tentativas += 1
#         print(f'Errado.Você fez {tentativas} tentativa(s).')
#         sua_descoberta = input('Digite uma letra: ')              