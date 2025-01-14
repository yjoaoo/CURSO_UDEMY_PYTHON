from CURSO_UDEMY_PYTHON.python_testes.src.calculadora import soma

print(soma(10,20))
try:
    print(soma("15", 15))
except AssertionError as erro:
    print(f"Conta invalida: {erro}")
