with open("tree.txt") as f:
    data = [row.strip() for row in f.readlines()]


num_ROWS = len(data)
num_COLUMNS = len(data[0])

edges = (num_ROWS*2) + ((num_COLUMNS - 2) * 2)
total = edges
scores = []

# need to iterate through all of the trees that aren't the edges

for row in range(1, num_ROWS-1):
    for column in range(1, num_COLUMNS-1):
        tree = data[row][column]

        #need to get all horizontal and vertical trees
        left = [data[row][column-i] for i in range(1,column+1)]
        right = [data[row][column+i] for i in range(1, num_COLUMNS-column)]
        up = [data[row-i][column] for i in range(1,row+1)]
        down = [data[row+i][column] for i in range(1, num_ROWS-row)]

        #part1 implementation 
        if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
            total+= 1

        #part2 implementation
        score = 1
        
        for list in (left, right, up, down):
            track  = 0 
            for i in range(len(list)):
                if list[i] < tree:
                    track += 1

                elif list[i] >= tree:
                    track += 1
                    break
                
        
            score *= track

        scores.append(score) 

        





print("Part 1 Answer: ", total)
print("Part 2 Answer: ", max(scores))