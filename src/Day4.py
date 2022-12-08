import os.path
from operator import itemgetter

data_path = os.path.join("..", "input", "Day04.txt")

"""
for each pair, 
evaluate if one of the outside number is less than the other
if that's true take the pair with the outside number 
then check if their right most number is also bigger than the other pairs right most
https://adventofcode.com/2022/day/4
"""

def extract_ranges(line: str):
    list_of_ranges = line.split(",")
    ranges = []
    for range in list_of_ranges:

        ranges.append([int(x) for x in range.split("-")])
    return ranges


def evaluate_for_smallest_initial_range_and_return_index(ranges):
    if ranges[0][0] < ranges[1][0]:
        return 0
    elif ranges[0][0] > ranges[1][0]:
        return 1
    else:
        return None


def sort_ranges_by_smallest_initial_value(ranges):
    return sorted(ranges, key=lambda x: x)


totalScore = 0

with open(data_path) as f:
    for _line in f:
        line = _line.rstrip()
        ranges = extract_ranges(line)
        sorted_ranges = sort_ranges_by_smallest_initial_value(ranges)
        if (sorted_ranges[0][0] >= sorted_ranges[1][0] and sorted_ranges[0][1] <= sorted_ranges[1][1]) or (sorted_ranges[1][0] >= sorted_ranges[0][0] and sorted_ranges[1][1] <= sorted_ranges[0][1]):

            totalScore += 1

print(totalScore)
