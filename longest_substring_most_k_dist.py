# Challenge — Longest Substring with At Most K Distinct Characters
# Problem Statement
# You are given a string s and an integer k.
# Your task is to find the length of the longest substring that contains at most k distinct characters.
# A substring is a contiguous sequence of characters within a string.
# Return the maximum length of such a substring.
# If k is 0, return 0.
# Examples
# Example 1
# Input:
# s = "eceba"
# k = 2
# Output:3
# Explanation:
# The longest substring with at most 2 distinct characters is:
# "ece"
# Length = 3.

def challenge(case):
    s = case[0]
    k = case[1]
    if not s or k == 0: return 0

    freq = {}
    left = 0
    best = 0

    for right, char in enumerate(s):
        freq[char] = freq.get(char, 0) + 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        best = max(best, right - left +1)
    return best    


def tests(cases, expected):
    success, error =  0, 0
    for case, ans in zip(cases, expected):
        result = challenge(case)
        if result == ans:
            success += 1
            continue
        error += 1
        print(f"Error in test: {case}. Result: {result} of expected: {ans}")

    print( f"Passed tests: {success} \nFailed tests:{error}")



cases = [
    ("eceba", 2),        # expected: 3
    ("aa", 1),           # expected: 2
    ("a", 1),            # expected: 1
    ("a", 0),            # expected: 0
    ("abcabcbb", 2),     # expected: 4
    ("abcabcbb", 3),     # expected: 8
    ("aaaa", 1),         # expected: 4
    ("abcd", 1),         # expected: 1
    ("abaccc", 2),       # expected: 4
    ("", 2),             # expected: 0
    ("aabbcc", 2),       # expected: 4
    ("aabbcc", 3),       # expected: 6
]
expected = [3, 2, 1, 0, 4, 8, 4, 1, 4, 0, 4, 6]
tests(cases, expected)