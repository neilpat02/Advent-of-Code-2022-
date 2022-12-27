with open("terminalinput.txt") as f:
    commands = [command.strip() for command in f.readlines()]



path = "/home"
directories = {"/home":0}

for command in commands:
    if command[0] == "$":

        #nothing is needed when ls

        if command[2:4] == "ls":
            pass
        elif command[2:4] == "cd":

            if command[5:6] == "/":
                path = "/home"

            elif command[5:7] == "..":
                path = path[:path.rfind("/")]
            
            else:
                path = path + "/" + command[5:]
                directories.update({path:0})

    elif command[0:3] == "dir":
        pass

    else:
        size = int(command[:command.find(" ")])
        directory  = path
        for i in range(path.count("/")):
            directories[directory] += size
            directory = directory[:directory.rfind("/")]




total = 0 
lim = 30000000 - (70000000 - directories["/home"])
plausible_dirs = []
for dir in directories:
    #part 1 
    if directories[dir] <= 100000:
        total += directories[dir]

    #part 2
    if lim <= directories[dir]:
        plausible_dirs.append(directories[dir])

    smallest = min(plausible_dirs)

print("Part 1 Ans: ", total)
print("Part 2 Ans: ", smallest)




