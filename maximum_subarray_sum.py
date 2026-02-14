# Problem Set — Maximum Subarray Sum
# Problem Statement
# You are given an integer array nums.
# Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Examples
# Example 1
# Input:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output:
# 6
# Explanation:
# The subarray [4, -1, 2, 1] has the largest sum = 6.

def max_subarray_sum(test):
    if len(test) == 0:
        return 0

    best = test[0]
    current = test[0]

    for n in test[1:]:
        current = max(n, current + n)
        best = max(best, current)
    return best


def run_tests(tests, expected):
    success, error =  0, 0
    for i in range(len(tests)):
        result = max_subarray_sum(tests[i])
        if result == expected[i]:
            success += 1
            continue
        error += 1
        print(f"Error in test: {tests[i]}. Result: {result} of expected: {expected[i]}")

    print( f"Passed tests: {success} \nFailed tests:{error}")



cases = [
    [-2,1,-3,4,-1,2,1,-5,4],   # expected: 6
    [4, 3, -2, -1, -5],        # expected: 7
    [-5, -2, 3, 4, 6],         # expected: 13
    [10],                      # expected: 10
    [-10],                     # expected: -10
    [-8, -3, -6, -2, -5, -4],  # expected: -2
    [0, 0, 0, 0],              # expected: 0
    [3, -2, 5, -1],            # expected: 6
    [1, -3, 2, 1, -1],         # expected: 3
    [2, 3, -10, 4, 5],         # expected: 9
    [5, 6, -100, 7, 8],        # expected: 15
    [-1, 2, 3, -2, 5, -10, 4, 6],  # expected: 10
    [],                        # expected: 0
]

expected = [6, 7, 13, 10, -10, -2, 0, 6, 3, 9, 15, 10, 0]

run_tests(cases, expected)