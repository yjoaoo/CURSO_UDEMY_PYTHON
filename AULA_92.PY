import sys

iterable = ["Eu", "tenho", "__iter__"]
iterator = iter(iterable)
lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print(generator)

# for n in generator:
#     print(n)