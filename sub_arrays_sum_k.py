# Challenge — Subarray Sum Equals K
# Problem Statement
# You are given an integer array nums and an integer k.
# Return the total number of continuous subarrays whose sum equals k.
# A subarray is a contiguous part of an array.
# Example 2
# Input: nums = [1,2,3], k = 3
# Output: 2

def subarray_sum_k(case):
    nums = case[0]
    k = case[1]
    prefix = 0
    freq = {0:1}
    count = 0

    for num in nums:

        prefix += num

        if prefix - k in freq:
            count += freq[prefix-k]

        freq[prefix] = freq.get(prefix, 0) +1 
    return count

def run_tests(tests, expected):
    success, error =  0, 0
    for i in range(len(tests)):
        result = subarray_sum_k(tests[i])
        if result == expected[i]:
            success += 1
            continue
        error += 1
        print(f"Error in test: {tests[i]}. Result: {result} of expected: {expected[i]}")

    print( f"Passed tests: {success} \nFailed tests:{error}")
    

cases = [
    # ([1,1,1], 2),           # expected: 2
    # ([1,2,3], 3),           # expected: 2
    # ([3,4,7,2,-3,1,4,2], 7), # expected: 4
    # ([1,-1,0], 0),          # expected: 3
    # ([0,0,0,0], 0),         # expected: 10
    # ([5], 5),               # expected: 1
    # ([-1,-1,1], 0),         # expected: 1
     ([2,-2,2,-2], 0),       # expected: 4
]
expected = [2, 2, 4, 3, 10, 1, 1, 4]

run_tests(cases, expected)
    