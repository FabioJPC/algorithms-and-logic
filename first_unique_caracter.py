# Challenge — First Unique Character
# You are given a string s.
# Your task is to find the index of the first non-repeating character in the string.
# If no such character exists, return -1.
# Do not use regex
# Do not use collections.Counter
# You may use dictionaries and loops

def unique(s):
    letters = {}
    for l in s:
        if l not in letters:
            letters[l] = 1
        else:
            letters[l] +=1

    for i, value in enumerate(s):
        if letters[value] == 1:
            return i
    return -1

def tests(cases, expected):
    success , error = 0 ,0
    for case, exp in zip(cases, expected):
        res = unique(case)
        print(res)
        if res == exp:
            success += 1
        else:
            error +=1
    print( f"Passed tests: {success} \nFailed tests:{error}")

cases = ['asdasd', 'abcba', 'abc', 'abcabcd']
expected = [-1, 2, 0, 6]
tests(cases, expected)