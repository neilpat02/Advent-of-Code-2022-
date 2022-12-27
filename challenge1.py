import sys
with open("reindeer_calories.txt") as f:
    numbers = [i for i in f.read().strip().split("\n")]
    
print(numbers)

#traverse through each line of data
onlyNum = []
counter = 0
for i in numbers: 
    if i == '':
        counter = 0
    else: 
        number = int(i)
        counter += number 
        onlyNum.append(counter)
        
onlyNum = sorted(onlyNum)

print(onlyNum[-1] + onlyNum[-2] + onlyNum[-3])


