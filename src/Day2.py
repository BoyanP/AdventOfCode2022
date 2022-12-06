import os.path
from enum import Enum


data_path = os.path.join("..", "input", "Day02.txt")


class RockPaperScissors(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


# the key beats the value
win_map = {RockPaperScissors.Rock: RockPaperScissors.Scissors,
           RockPaperScissors.Paper: RockPaperScissors.Rock, RockPaperScissors.Scissors: RockPaperScissors.Paper}


def shapeFactory(letter):
    if letter == "A" or letter == "X":
        return RockPaperScissors.Rock
    elif letter == "B" or letter == "Y":
        return RockPaperScissors.Paper
    elif letter == "C" or letter == "Z":
        return RockPaperScissors.Scissors


totalScore = 0
with open(data_path) as f:
    for _line in f:
        line = _line.rstrip()
        roundScore = 0
        roundInput = line.split(' ')
        opponent = shapeFactory(roundInput[0])
        me = shapeFactory(roundInput[1])
        if opponent.value == me.value:
            roundScore += 3
        elif win_map[me] == opponent:
            roundScore += 6

        roundScore += me.value
        totalScore += roundScore

print(totalScore)
