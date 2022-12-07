import os.path

data_path = os.path.join("..", "input", "Day03.txt")

keys = {}
LOWERCASE_ORDINANCE_OFFSET = 96
UPPERCASE_ORDINANCE_OFFSET = 38
priority_score_dictionary = {}

# To help prioritize item rearrangement,
# every item type can be converted to a priority:
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.


def init_keys_dict():
    for n in range(ord("a"), ord("z")+1):
        keys[chr(n)] = 0
        priority_score_dictionary[chr(n)] = n - LOWERCASE_ORDINANCE_OFFSET

    for n in range(ord("A"), ord("Z")+1):
        keys[chr(n)] = 0
        priority_score_dictionary[chr(n)] = n - UPPERCASE_ORDINANCE_OFFSET


init_keys_dict()

priorityScore = 0


with open(data_path) as f:
    for _line in f:
        line = _line.rstrip()
        firstRucksack = line[:len(line)//2]
        for character in firstRucksack:
            if keys[character] == 1:
                continue
            keys[character] = keys[character] + 1

        secondRucksack = line[len(line)//2:]
        for character in secondRucksack:
            if keys[character] == 1:
                keys[character] = keys[character] + 1
        for letter, count in keys.items():
            if count == 2:
                score = priority_score_dictionary[letter]
                priorityScore += score
                break
        keys = dict.fromkeys(keys, 0)

print(priorityScore)
