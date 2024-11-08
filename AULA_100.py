import importlib

import AULA_100_M

print(AULA_100_M.variavel)

for i in range(10):
    importlib.reload(AULA_100_M)
    print(i)

print('Fim')
