## Em Python, assertions são usados para criar condições que devem 
# ser verdadeiras em um ponto específico do código. Se a condição 
# for falsa, o programa lança uma exceção do tipo AssertionError. 
# Elas são úteis para depuração, permitindo verificar suposições 
# feitas durante o desenvolvimento.

## Usos comuns
# Validação durante o desenvolvimento:

def dividir(a, b):
    assert b != 0, "Divisor nao pode ser zero"
    return a / b

try:
    print(dividir(2,0))
except AssertionError as erro:
    print(erro)

print(dividir(4,4))

## Verificação de invariantes:

def incrementar(lista):
    assert isinstance(lista, list), "Entrada deve ser uma lista"
    lista.append(1)

dados = [1, 2, 3]
incrementar(dados)
print(dados)

incrementar(23)