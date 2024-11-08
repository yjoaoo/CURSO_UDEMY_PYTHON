#################### de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s1 = set() # vazio
# s1 = {"João", 1, 2, 3} # Com dados 

# l1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print (1 not in s1)
# for i in s1:
#     print(i)


#################### Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('joao')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá mundo')
# s1.discard('joao')
# print(s1)
# # print(s1)


#################### Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)

