# count é um iterador sem fim (itertools)

from itertools import count

contador1 = count()
range1 = range(50)

print("contador1", hasattr(contador1,'__iter__'))
print("contador1", hasattr(contador1,'__next__'))
print("range1", hasattr(range1,'__iter__'))
print("range1", hasattr(range1,'__next__'))

print("CONTADOR")
for i in contador1:
    if i >= 50:
        break
    print(i)

print()
print("RANGE")
for i in range1:
    print(i)