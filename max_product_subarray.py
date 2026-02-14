# Challenge — Maximum Product Subarray (nível hard)
# Problem Statement
# Given an integer array nums, find the contiguous subarray within an array that has the largest product, and return the product.
# Rules
# The subarray must be contiguous.
# The array contains at least one number.
# Time complexity target: O(n).
# You are NOT allowed to use brute force O(n²).
# Example
# Input:
# nums = [2,3,-2,4]
# Output:
# 6
# Explanation:
# The subarray [2,3] has the largest product = 6.

def max_product_subarray(case):
    max_prod = case[0]
    min_prod = case[0]
    best = case[0]

    print(f"--------------------- \ntestando: {case}")

    for n in case[1:]:
        if n < 0:
            max_prod, min_prod = min_prod , max_prod

        max_prod = max(n, max_prod * n)
        min_prod = min(n, min_prod * n)

        print( f"Max_prod: {max_prod} e min_prod: {min_prod}")

        best = max(best, max_prod)
    return best


        

def run_tests(tests, expected):
    success, error =  0, 0
    for i in range(len(tests)):
        result = max_product_subarray(tests[i])
        if result == expected[i]:
            success += 1
            continue
        error += 1
        print(f"Error in test: {tests[i]}. Result: {result} of expected: {expected[i]}")

    print( f"Passed tests: {success} \nFailed tests:{error}")


cases = [
    [2,3,-2,4],          # expected: 6
    [-2,0,-1],           # expected: 0
    [-2,3,-4],           # expected: 24
    [0,2],               # expected: 2
    [-2],                # expected: -2
    [-1,-3,-10,0,60],    # expected: 60
    [6,-3,-10,0,2],      # expected: 180
    [-2,-3,0,-2,-40],    # expected: 80
]
expected = [6, 0, 24, 2, -2, 60, 180, 80]
run_tests(cases, expected)