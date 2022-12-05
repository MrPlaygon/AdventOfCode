towers =[[]]

def divide_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def move_crates(fromm, too, numberz):
    for i in range(numberz):
        towers[too].append(towers[fromm].pop())
    
def move_crates_9001(fromm, too, numberz):
    towers[too].extend(towers[fromm][len(towers[fromm])-numberz:])
    towers[fromm] = towers[fromm][:len(towers[fromm])-numberz]


with open("05.txt") as f:
    #stupid parsing >__>
    lines = []
    line = f.readline().rstrip()
    while line:
        lines.append(line)
        line=f.readline().rstrip()
    lines = lines[:len(lines)-1] #lines contains the "towers" of data
    lines = lines[::-1] #reverse order. top element in tower should be last in list

    for l in lines:
        i = 0
        for s in list(divide_list(l, 4)):
            s = s.replace(" ", "").replace("[","").replace("]","")
            if s != "":
                if(i>=len(towers)):
                    towers.append([s])
                else:
                    towers[i].append(s)
            i+=1
    print(towers)
    
    #GOGO ACTION
    for line in f:
        line = line.rstrip().replace("move ","").replace(" from ", ",").replace(" to ", ",")
        instructions = line.split(",")
        print(instructions)
        #move_crates(int(instructions[1])-1,int(instructions[2])-1, int(instructions[0])) #Part 1
        move_crates_9001(int(instructions[1])-1,int(instructions[2])-1, int(instructions[0])) #Part 2
    
    print("\n\n")

    print(towers)
    for arr in towers:
        print(arr[-1],end="") if arr else None