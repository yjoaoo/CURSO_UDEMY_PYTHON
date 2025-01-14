# Doctests são uma funcionalidade do Python que permite incorporar 
# testes diretamente na documentação das funções, métodos ou módulos. 
# Eles utilizam exemplos de uso, escritos em formato de sessão 
# interativa do Python, para validar automaticamente o comportamento 
# esperado do código.

# Os doctests ficam nos comentários (docstrings) e podem ser executados 
# para verificar se o código funciona conforme documentado.

def soma(a, b):
    """
    Retorna a soma de dois numeros
    Exemplo:
    >>> soma(2, 3)
    5
    >>> soma(-1, 1)
    0
    >>> soma(0, 0)
    0
    >>> soma(2, 3) 
    6"""
    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)