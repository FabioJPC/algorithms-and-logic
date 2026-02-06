#Challenge — Merge Intervals
# You are given a list of intervals, where each interval is represented as:
# [start, end]
# Your task is to merge all overlapping intervals and return a new list of non-overlapping intervals.

def merge_intervals(intervals):
    merged = []
    sorted_intervals = sorted(intervals)
    merged.append(sorted_intervals[0])
    for i in range(1, len(sorted_intervals)):
        last_merged = merged[-1]
        if(last_merged[-1] >= sorted_intervals[i][0]):
            merged[-1] = [min(last_merged[0], sorted_intervals[i][0]), max(last_merged[-1], sorted_intervals[i][-1])]
            continue
        merged.append(sorted_intervals[i])
    return merged
        
def test(intervals, expected):
    success, error = 0, 0
    for i in range(len(intervals)):
        result = merge_intervals(intervals[i])
        if result != expected[i]:
            error += 1
            print(f"Error in interval {intervals[i]} with result {result}.")
            continue
        success += 1
        
    print( f"Passed tests: {success} \nFailed tests:{error}")

intervals = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
    [[5,7],[1,2],[3,4]],
    [[1,10],[2,3],[4,8]],
    [[1,2]],
]

expected = [
    [[1,6],[8,10],[15,18]],
    [[1,5]],
    [[1,2],[3,4],[5,7]],
    [[1,10]],
    [[1,2]],
]
test(intervals, expected)
