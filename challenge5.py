stackCount = 9
drawingLines = 8

with open("supplystacks.txt") as f:
    # step 1: get the files to split at the newline seperating instructions
    instructions = f.read()[:-1].split("\n\n")
    drawing = instructions[0].split("\n")

    stacks = [[] for _ in range(stackCount)]

    for i in range(drawingLines):
        line = drawing[i]
        crates = line[1::4]
        for j in range(len(crates)):
            if crates[j] != " ":
                stacks[j].append(crates[j])


# reverse the stacks
stacks = [stack[::-1] for stack in stacks]

# begin to go through the instructions and start moving stacks around

for line in instructions[1].split("\n"):
    val_location = line.split(" ")
    quant, start, destination = map(
        int, [val_location[1], val_location[3], val_location[5]]
    )
    start -= 1
    destination -= 1

    """ #uncomment for part 1 answer
    
    for _ in range(quant):
        extract = stacks[start].pop()
        stacks[destination].append(extract)
        
    """

    """#part 2 begins here... uncomment the following block to get part2 answer
    
    stacks[destination].extend(stacks[start][-quant:])
    stacks[start] = stacks[start][:-quant]
    
    """
part = [stack[-1] for stack in stacks]
print("".join(part))
