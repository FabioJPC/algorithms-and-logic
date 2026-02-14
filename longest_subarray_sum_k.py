# Challenge — Longest Subarray with Sum K
# Problem Statement
# You are given an integer array nums and an integer k.
# Your task is to find the length of the longest contiguous subarray whose sum equals k.
# A subarray is a contiguous part of an array.
# Return the maximum length of such a subarray.
# If no such subarray exists, return 0.
# Example
# Input:
# nums = [1, -1, 5, -2, 3]
# k = 3
# Output:
# 4
# Explanation:
# The longest subarray with sum = 3 is:
# [1, -1, 5, -2]

def longest_subarray_sum_k(case):

    nums = case[0]
    k = case[1]
    if len(nums) == 0: return 0

    largest = 0
    current_sum = 0
    seen = {0 : -1}

    for index, num in enumerate(nums):
        current_sum += num
        target = current_sum - k

        if target in seen:
            lenght = index - seen[target]
            largest = max(largest, lenght)
        if current_sum not in seen:
            seen[current_sum] = index

    return largest
    
    
        

def run_tests(tests, expected):
    success, error =  0, 0
    for i in range(len(tests)):
        result = longest_subarray_sum_k(tests[i])
        if result == expected[i]:
            success += 1
            continue
        error += 1
        print(f"Error in test: {tests[i]}. Result: {result} of expected: {expected[i]}")

    print( f"Passed tests: {success} \nFailed tests:{error}")


cases = [
    ([1, -1, 5, -2, 3], 3),      # expected: 4
    ([-2, -1, 2, 1], 1),         # expected: 2
    ([1, 2, 3], 3),              # expected: 2
    ([3, 1, -1, 2, -2, 4], 3),   # expected: 5
    ([0, 0, 0, 0], 0),           # expected: 4
    ([1, -1, 1, -1, 1, -1], 0),  # expected: 6
    ([5], 5),                    # expected: 1
    ([5], 3),                    # expected: 0
    ([], 0),                     # expected: 0
    ([2, -2, 2, -2, 2], 0),      # expected: 4
    ([10, -10, 10, -10, 10], 10) # expected: 5
]

expected = [4, 2, 2, 5, 4, 6, 1, 0, 0, 4, 5]
run_tests(cases, expected)