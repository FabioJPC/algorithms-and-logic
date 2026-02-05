# Challenge — Longest Substring Without Repeating Characters
# Problem Statement
# Given a string s, find the length of the longest substring without repeating characters.
# Return both the size and the substring itsef.

def largest_substring(s):
    last = {}
    left = 0
    max_len = 0
    best_substring = ""

    for right, char in enumerate(s):
        if char in last and last[char] >= left:
            left = last[char] + 1

        last[char] = right
        new_size = right - left + 1

        if new_size > max_len:
            max_len = new_size
            best_substring = s[left:right+1]

    return max_len, best_substring
        

def test(cases, expected):
    success, error = 0 , 0
    for i in range(len(cases)):
        size, string = largest_substring(cases[i])
        if size == expected[i]:
            success += 1
            print(f"Test case: {i}: Correct substring: {string} with size {size}")
            continue
        error += 1

    print( f"Passed tests: {success} \nFailed tests:{error}")


cases = [
    "abcabcbb",   # expected: 3
    "bbbbb",      # expected: 1
    "pwwkew",     # expected: 3
    "",           # expected: 0
    "abcdefg",    # expected: 7
]
expected = [3, 1, 3, 0, 7]
test(cases, expected)
