# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

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

def inverte_str(str):
    return str[::-1]

def e_str(parametro):
    if not isinstance(parametro, str):
        raise TypeError("Parametro deve ser str")


inverte_str_checando_parametro = criar_funcao(inverte_str)
invertida = inverte_str_checando_parametro("123")
print(invertida)