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

palavras = ["python", "programacao", "computador", "jogo", "codigo", "algoritmo"]
palavra_secreta = "python"  # Escolha fixa para simplificar

letras_corretas = set(palavra_secreta)
letras_digitadas = set()
tentativas = 0
max_tentativas = 6

print("Bem-vindo ao jogo da palavra secreta!")
print("A palavra secreta tem", len(palavra_secreta), "letras.")

while letras_corretas:
    if tentativas >= max_tentativas:
        print("\nVocê excedeu o número máximo de tentativas. A palavra secreta era:", palavra_secreta)
        break

    tentativa = input("\nDigite uma letra: ").lower()

    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue

    if tentativa in letras_digitadas:
        print("Você já tentou esta letra. Tente outra.")
        continue

    letras_digitadas.add(tentativa)

    if tentativa in letras_corretas:
        print("A letra", tentativa, "está na palavra secreta!")
        letras_corretas.remove(tentativa)
    else:
        print("A letra", tentativa, "não está na palavra secreta.")
        tentativas += 1

if letras_corretas:
    print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)
else:
    print("\nParabéns! Você descobriu a palavra secreta:", palavra_secreta)






