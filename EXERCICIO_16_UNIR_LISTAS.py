# # Exercício - Unir listas
# # Crie uma função zipper (como o zipper de roupas)
# # O trabalho dessa função será unir duas
# # listas na ordem.
# # Use todos os valores da menor lista.
# # Resultado
# # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estado = ['BA', 'SP', 'MG', 'RJ']

# def zipper (lista1 , lista2):
#     for cidade, estado in zip(lista1, lista2):
#         print(f"Cidade: {cidade}, Estado: {estado}")


# zipper(cidade, estado)
# #---------------------------OU--------------------------------
# print()
# def zipper(lista1, lista2):
#     return list(zip(lista1, lista2))

# resultado = zipper(cidade, estado)
# print(resultado)

# #-------------------------------SOLUÇÂO--------------------------
# print()

# def zipper(lista1, lista2):
#     intervalo_minimo = min(len(lista1), len(lista2))
#     return[
#         (lista1[i], lista2[i]) for i in range(intervalo_minimo)
#     ]

# print(zipper(cidade, estado))

#==========================================================================

"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
#-----------------------------------------------------------
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
#-----------------------------------------------------------
# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)
#-----------------------------------------------------------

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)