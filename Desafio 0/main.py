"""Desafio 0 - Lógica de programação."""

from exercicios import asteriscos, menor_diff, subconjuntos



while True:
    escolha = int(input("Digite o número do exercício: "))

    if escolha == 1:
        n = int(input("n: "))
        resposta = asteriscos(n)
        print(resposta)


    elif escolha == 2:
        array = input("Digite os números separando por vírgula (1, 2, 3, N): ")
        allow_duplicates = bool(input("Permitir valores duplicados? Digite qualquer coisa para sim, ou pressione 'Enter' para não: "))
        sorted_pairs = bool(input("Ordenar de forma crescente? Digite qualquer coisa para sim, ou pressione 'Enter' para não: "))
        unique_pairs = bool(input("Retornar apenas pares únicos? Digite qualquer coisa para sim, ou pressione 'Enter' para não: "))
        resposta = menor_diff(array, allow_duplicates, sorted_pairs, unique_pairs)
        print(resposta)

    elif escolha == 3:
        conjunto = input("Digite os números do conjunto separando por vírgula (1, 2, 3, N): ")
        max_size = int(input("Limite o tamanho máximo dos subconjuntos:"))
        min_size = int(input("Defina o tamanho mínimo dos subconjuntos:"))
        distinct_only = bool(input("Permitir valores duplicados?? Digite qualquer coisa para sim, ou pressione 'Enter' para não: "))
        sort_subsets = bool(input("Ordenar de forma crescente? Digite qualquer coisa para sim, ou pressione 'Enter' para não: "))

        resposta = subconjuntos(conjunto, max_size, min_size, distinct_only, sort_subsets)
        print(resposta)
