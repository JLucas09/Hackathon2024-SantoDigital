"""Desafio 0 - Lógica de programação."""

def asteriscos(n):
    retorno = list()
    for i in range(n):
        retorno.append('*' * (i + 1))
    return retorno

def menor_diff(array, duplicar, cresente, unicos):
    array = [int(i) for i in array.split(', ')]
    array.sort(reverse = not cresente)
    retorno = []
    menor = float('inf')

    for i in range(len(array) - 1):
        diff = abs(array[i] - array[i + 1])

        if diff == menor:
            retorno.append((array[i], array[i + 1]))

        elif diff < menor:
            menor = diff
            retorno = [(array[i], array[i + 1])]

    if unicos:
        # Remove os duplicados ao converter cada par em tupla ordenada apos converte em lista.
        retorno = list(set(tuple(sorted(temp)) for temp in retorno))

    if not duplicar:
        # Para cada elemento na lista verifica se os par e igual.
        retorno = [x for x in retorno if x[0] != x[1]]

    if cresente:
        # Para cada par na lista ordena garantindo que cada par seja representado como (menor, maior)
        # Depois ordena a lista de pares resultante.
        retorno = sorted((min(a, b), max(a, b)) for a, b in retorno)

    return retorno


def subconjuntos(conjunto, maximo, minimo, distinto, sort_sub):
    conjunto = [int(i) for i in conjunto.split(', ')]
    retorno = []

    if distinto:
        conjunto = list(set(conjunto))

    if sort_sub:
        conjunto.sort()

    sub_conjunto = [[]]

    for i in conjunto:
        sub_conjunto.extend([temp + [i] for temp in sub_conjunto])

    retorno = [x for x in sub_conjunto if minimo <= len(x) <= maximo]

    if sort_sub:
        retorno.sort(key=lambda x:(len(x), x))

    return retorno
