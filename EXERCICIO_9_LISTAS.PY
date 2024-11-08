# Exiba os índices da lista
# 0 Thanos
# 1 Loki
# 2 Ultron

lista = ["Thanos", "loki", "Ultron"]
lista.append("Kang")
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type (lista[indice]))