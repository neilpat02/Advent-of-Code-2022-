from string import ascii_letters

with open("rucksacks.txt") as f:
    rucksacks = [i for i in f.read().strip().split("\n")]
    
listOfType = []
sum = 0
for rucksack in rucksacks:
    split  = len(rucksack)//2
    
    first_half = set(rucksack[0:split])
    second_half = set(rucksack[split:])
    
    for key, value in enumerate(ascii_letters):
        if value in first_half and value in second_half:
            sum += key+1
    
    
print("part 1 answer is: ", sum)


#part 2 begins here
part2sum = 0 
j = 3
for i in range(0,len(rucksacks),3):
    splitSacks = rucksacks[i:j]
    j += 3
    
    for key, value in enumerate(ascii_letters):
        if value in splitSacks[0] and value in splitSacks[1] and value in splitSacks[2]:
            part2sum += key+1
lines = [i for i in f.read().strip().split("\n")]