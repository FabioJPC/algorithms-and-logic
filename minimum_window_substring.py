# Challenge — Minimum Window Substring (FAANG Classic)
# Problem Statement
# You are given two strings s and t.
# Your task is to find the smallest substring in s that contains all the characters of t (including duplicates).
# Return the minimum window substring.
# If there is no such substring, return an empty string "".
# Example
# Input:
# s = "ADOBECODEBANC"
# t = "ABC"
# Output:
# "BANC"
# Explanation:
# The substring "BANC" is the smallest window that contains all characters of "ABC".


def solution(case):
    s = case[0]
    t = case[1]
    if s == "" or len(s) < len(t): return ""

    left = 0
    freq = {}
    t_freq = {}
    best = ""
    min_len = float("inf")
    subs = ""
    matches = 0

    for c in t:
        t_freq[c] = t_freq.get(c, 0) + 1

    

    for right, char in enumerate(s):
        freq[char] = freq.get(char, 0) +1 

        if char in t_freq and freq[char] == t_freq[char]:
            matches += 1

        while matches == len(t_freq):
            subs = s[left: right + 1]
            if len(subs) < min_len:
                best = subs
                min_len = len(best)
            freq[s[left]] -= 1
            if s[left] in t_freq and freq[s[left]] < t_freq[s[left]]:
                matches -= 1
            left += 1
   
    return best
            

def run_tests(tests, expected):
    success, error =  0, 0
    for case, ans in zip(tests, expected):
        result = solution(case)
        if result == ans:
            success += 1
            continue
        error += 1
        print(f"Error in test: {case}. Result: {result} of expected: {ans}")

    print( f"Passed tests: {success} \nFailed tests:{error}")


cases = [
    ("ADOBECODEBANC", "ABC"),   # expected: "BANC"
    ("a", "a"),                 # expected: "a"
    ("a", "aa"),                # expected: ""
    ("ab", "b"),                # expected: "b"
    ("aa", "aa"),               # expected: "aa"
    ("abc", "ac"),              # expected: "abc"
    ("aaflslflsldkalskaaa", "aaa"), # expected: "aaa"
    ("this is a test string", "tist"), # expected: "t stri"
    ("abcdef", "xyz"),          # expected: ""
    ("bdab", "ab"),             # expected: "ab"
]

expected = [
    "BANC",
    "a",
    "",
    "b",
    "aa",
    "abc",
    "aaa",
    "t stri",
    "",
    "ab",
]

run_tests(cases, expected)
