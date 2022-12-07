import timeit

def work():
    with open("06.txt") as f:
        line = f.readline().rstrip()
        found = False
        #i=4 # Part 1
        i=14 # Part 2
        while not found:
            # subline=line[i-4:i] # Part 1
            subline=line[i-14:i] # Part 2
            #print("checking ", subline, len(set(subline)), len(subline))
            if len(subline) == len(set(subline)):
                print("Found marker at ", i)
                found = True
            i+=1

print(timeit.timeit(work, number=100))