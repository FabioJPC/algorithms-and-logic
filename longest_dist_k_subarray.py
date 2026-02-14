# Challenge — Longest Subarray with At Most K Distinct Numbers
# Problema
# Você recebe:
# um array de inteiros nums
# um inteiro k
# Sua tarefa é encontrar o comprimento do maior subarray contínuo que contém no máximo k números distintos.
# Exemplo
# Exemplo 1
# nums = [1,2,1,2,3]
# k = 2
# Saída:
# 4
# Explicação:
# O maior subarray válido é [1,2,1,2].



def challenge(case):
    nums = case[0]
    k = case[1]
    if not nums : return 0

    left = 0
    best = 0
    freq = {}   

    for right, num in enumerate(nums):
        freq[num] = freq.get(num, 0) +1

        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        best = max(best, right - left +1)

    return best


def run_tests(cases, expected):
    success, error =  0, 0
    for case, ans in zip(cases, expected):
        result = challenge(case)
        if result == ans:
            success += 1
            continue
        error += 1
        print(f"Error in test: {case}. Result: {result} of expected: {ans}")

    print( f"Passed tests: {success} \nFailed tests:{error}")

tests = [
    ([1,2,1,2,3], 2),   # expected: 4
    ([1,2,3,4], 1),     # expected: 1
    ([1,1,1,1], 1),     # expected: 4
    ([1,2,1,3,4,2,3], 2), # expected: 3
    ([], 2),            # expected: 0
    ([1,2], 3),         # expected: 2
]

expected = [4, 1, 4, 3, 0, 2]

run_tests(tests, expected)