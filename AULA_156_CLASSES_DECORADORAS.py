# Classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
    
    def __call__(self, funcao):
        def interna(*args, **kwargs):
            resultado = funcao(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

@Multiplicar(2)
def soma (x, y):
    return x + y

funcao_soma = soma(2, 4)
print(funcao_soma)