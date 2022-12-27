with open("ranges.txt") as f:
    lines = [i for i in f.read().strip().split("\n")]


counter = 0

for line in lines:
    first_interval, second_interval = line.split(",")

    first_interval = [int(i) for i in first_interval.split("-")]
    second_interval = [int(i) for i in second_interval.split("-")]

    if (
        first_interval[0] <= second_interval[0]
        and first_interval[1] >= second_interval[1]
    ):
        counter += 1

    elif (
        second_interval[0] <= first_interval[0]
        and second_interval[1] >= first_interval[1]
    ):
        counter += 1


print("The answer to part 1 is: ", counter)


# part 2 begins here...
counter = 0
for line in lines:
    first_interval, second_interval = line.split(",")

    first_interval = [int(i) for i in first_interval.split("-")]
    second_interval = [int(i) for i in second_interval.split("-")]

    if first_interval[0] is range(
        second_interval[0], second_interval[1] + 1
    ) or first_interval[1] in range(second_interval[0], second_interval[1] + 1):
        counter += 1

    elif second_interval[0] is range(
        first_interval[0], first_interval[1] + 1
    ) or second_interval[1] in range(first_interval[0], first_interval[1] + 1):
        counter += 1

print("The answer to part 2 is: ", counter)
