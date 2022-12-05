badpairs=0

with open("04.txt") as file:
    for line in file:
        elfes=line.split(",")

        elf1=elfes[0].split("-")
        elf1arr=range(int(elf1[0]), int(elf1[1])+1)
        
        elf2=elfes[1].split("-")
        elf2arr=range(int(elf2[0]), int(elf2[1])+1)

        if(set(elf1arr).issubset(set(elf2arr)) or set(elf2arr).issubset(set(elf1arr))):
            badpairs+=1

print(badpairs)


badpairs2=0

with open("04.txt") as file:
    for line in file:
        elfes=line.split(",")

        elf1=elfes[0].split("-")
        elf1arr=range(int(elf1[0]), int(elf1[1])+1)
        
        elf2=elfes[1].split("-")
        elf2arr=range(int(elf2[0]), int(elf2[1])+1)

        if any(number in elf1arr for number in elf2arr):
            badpairs2+=1

print(badpairs2)