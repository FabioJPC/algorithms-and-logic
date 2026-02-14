# Problema: Subarray mais longo sem repetir elementos
# Dado um array de inteiros, encontre o comprimento do maior subarray contínuo que não contém elementos repetidos.
# Exemplo:
# Entrada:
# nums = [2, 3, 5, 3, 2, 4, 5]
# Saída:
# 4
# Explicação:
# O maior subarray sem repetição é:
# [3, 2, 4, 5]
# Comprimento = 4.
# Regras
# O subarray deve ser contínuo (sequencial).
# Não pode usar sort.
# Não pode usar força bruta O(n²) (se usar, depois otimiza).
# Tente chegar em O(n).

def largest_subarray(test):
    seen = {}
    largest = 0
    left = 0

    for index, value in enumerate(test):
        if value in seen and seen[value] >= left:
            left = seen[value] + 1

        seen[value] = index
        new_size = index - left + 1

        largest = max(largest, new_size)
    return largest


def tests(tests, expected):
    success, error =  0, 0
    for i in range(len(tests)):
        result = largest_subarray(tests[i])
        if result == expected[i]:
            success += 1
            continue
        error += 1
        print(f"Error in test: {tests[i]}. Result: {result} of expected: {expected[i]}")

    print( f"Passed tests: {success} \nFailed tests:{error}")


cases = [
    [1, 2, 3, 4, 5],        # 5
    [1, 1, 1, 1],           # 1
    [2, 3, 5, 3, 2, 4, 5],  # 4
    [7, 8, 9, 7, 10, 11],   # 5
    [],                     # 0
]
expected = [5,1,4,5,0]

tests(cases, expected)