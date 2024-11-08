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

palavra = "Historia"
palavra_adivinhada = ""
letras_digitadas = ""
tentativas = 0
 
while True:
    letra = input("Digite uma letra da palavra secreta:  ").lower()
    tentativas += 1
 
    if len(letra) > 1:
        print("Escreva apenas uma letra!! \n")
        continue
 
    if letra in letras_digitadas:
        print("Já você digitou essa letra, digite outra: \n")
        continue
 
    if letra not in letras_digitadas:
        letras_digitadas += letra
 
    for i in palavra.lower():
        if i in letras_digitadas:
            palavra_adivinhada += i
        else:
            palavra_adivinhada += "*"     
 
    print(f"Palavra = {palavra_adivinhada}\n")
 
    if palavra_adivinhada == palavra.lower():
        print("Você ganhou, achou a palavra secreta!!")
        break
 
    if palavra != palavra_adivinhada:
        palavra_adivinhada = ""
    
    print(f"Você já usou {tentativas} tentativas \n")