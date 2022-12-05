prio1 = 0

def calc_prio(letter):
    if letter.isupper():
        return(ord(letter)-38)
    else:
        return(ord(letter)-96)

with open("03.txt") as file:
    for line in file:
        str1=line[:len(line)//2]
        str2=line[len(line)//2:]
        print(line)
        for letter in str1:
            if letter in str2:
                print("The common letter is: ", letter)
                prio1+=calc_prio(letter)
                break



prio=0

with open("03.txt") as file:
    lines = file.read().splitlines()
    i=0
    while i < len(lines):
        rucksack1=lines[i]
        rucksack2=lines[i+1]
        rucksack3=lines[i+2]
        for letter in rucksack1:
            if (letter in rucksack2) and (letter in rucksack3):
                print("The common letter is: ", letter)
                prio+=calc_prio(letter)
                break
        i+=3

print(prio1)
print(prio)

print(calc_prio("a"), calc_prio("A"), calc_prio("z"), calc_prio("Z"))