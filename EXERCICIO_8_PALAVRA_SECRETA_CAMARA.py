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

palavra_secreta = 'Mr Pacifier'
maximo_tentativas = 3

tentativas = 0
letras_reveladas = [False] * len(palavra_secreta)

def print_palavra_mascarada():
    palavra_mascarada = ''
    for posicao in range(len(palavra_secreta)):
        if letras_reveladas[posicao]:
            palavra_mascarada += palavra_secreta[posicao]
        else:
            palavra_mascarada += '*'
    print(palavra_mascarada)
        

def tentativa(letra):
    letra_revelada = False
    for posicao in range(len(palavra_secreta)):
        if palavra_secreta[posicao] == ' ':
            letras_reveladas[posicao] = True
        if palavra_secreta[posicao].upper() == letra.upper():
            letras_reveladas[posicao] = True
            letra_revelada = True
    return letra_revelada

while True:
    entrada = input('Digite uma letra: ')
    if len(entrada) != 1 or not entrada.isalpha():
        print("Entrada inválida")
        continue
    if tentativa(entrada):
        print_palavra_mascarada()
    else:
        tentativas += 1
        print(f'Você gastou {tentativas} tentativas')
    if all(estado == True for estado in letras_reveladas):
        print(f'Você conseguiu! O nome é {palavra_secreta}')
        break
    if tentativas >= maximo_tentativas:
        print("Você fracassou")
        break