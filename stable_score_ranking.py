# Challenge: Stable Score Ranking
# You are given a list of integers representing players’ scores.
# Rules
# 1-The highest score gets rank 1
# 2-The second highest score gets rank 2, and so on
# 3-Equal scores must receive the same rank
# 4-The ranking must be stable, meaning the output must preserve the original order of the input list

def score_ranking(array):
    filtered = sorted(set(array), reverse=True)
    rankings = {
        score : index + 1 for index, score in enumerate(filtered)
    }
    return [rankings[score] for score in array]

def run_tests(test, expected):
    success, error  = 0 ,0
    for test, exp in zip(test, expected):
        if score_ranking(test) == exp:
            success +=1
        else:
            error += 1
    print( f"Passed tests: {success} \nFailed tests:{error}")


#If tests are changed please also match the expected outcome
tests = [[10, 5, 10, 8], [1, 2, 3, 4, 5], [50, -10, 50, 50, 0]]
expected = [[1, 3, 1, 2], [5, 4, 3, 2, 1], [1, 3, 1, 1, 2]]
run_tests(tests, expected)