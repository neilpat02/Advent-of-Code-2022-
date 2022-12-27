with open("rockPaperscissors.txt") as f:
    lines = [i for i in f.read().strip().split("\n")]

points_part1 = 0
points_part2 = 0
possible_outcomes_part1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
possible_outcomes_part2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


for string in lines:

    points_part1 += possible_outcomes_part1[string]
    points_part2 += possible_outcomes_part2[string]


print("Part 1 Answer: " + str(points_part1))
print("Part 2 Answer: " + str(points_part2))
