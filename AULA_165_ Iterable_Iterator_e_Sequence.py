# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence

class Mylist(Sequence):
    def __init__(self):
        self.dados = {}
        self._index = 0
        self._next_index += 1
    
    def append(self, *values):
        for v in values:
            self._dados[self._index] = v
            self._index

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._dados[index]

    def __setitem__(self, index, value):
        self._dados[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._dados[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = Mylist()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')         