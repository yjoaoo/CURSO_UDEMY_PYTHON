# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(funcao):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_str(arg)
        resultado = funcao(*args, **kwargs)
        print(f"O seu resultado foi {resultado}")
        print("Ok, aogra você foi decorado")
        return resultado
    return interna

@criar_funcao
def inverte_str(str):
    print(f"{inverte_str.__name__}")
    return str[::-1]

def e_str(parametro):
    if not isinstance(parametro, str):
        raise TypeError("Parametro deve ser str")


invertida = inverte_str("123")
print(invertida)