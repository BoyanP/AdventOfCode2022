import os.path


data_path = os.path.join("..", "input", "Day01.txt")

global highestCalories
highestCalories = 0
global currentCalculatedCalories
currentCalculatedCalories = 0


def main():
    global currentCalculatedCalories
    print("hello?>")

    def resetCalculatedCalories():
        global currentCalculatedCalories
        currentCalculatedCalories = 0

    def checkAndSetHighestCalories():
        global currentCalculatedCalories
        global highestCalories
        if currentCalculatedCalories > highestCalories:
            highestCalories = currentCalculatedCalories
            resetCalculatedCalories()

    with open(data_path) as f:
        for line in f:
            if line == "\n":
                resetCalculatedCalories()
                continue

            calories = int(line)
            currentCalculatedCalories += calories
            print(calories)
            checkAndSetHighestCalories()
    print("Day 1 answer is : ", highestCalories)
    return highestCalories


main()
