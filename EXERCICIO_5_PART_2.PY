"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#horario = int(input("Quantas horas são para voce agora?"))

#manha = horario >= 0 and horario <=11
#tarde = horario >= 12 and horario <=17
#noite = horario >=18 and horario <=23

#if manha:
    #print (f'O horario que você digitou: {manha} siginifica que está de manha'))
#elif tarde:
    #print(f'O horario que você digitou: {tarde} siginifica que está de tarde')
#else:
    #print(f'O horario que você digitou: {noite} siginifica que está de noite')

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')