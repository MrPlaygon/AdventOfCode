# max = 0
# current = 0
# with open("01.txt") as file:
#     for line in file:
#         print(line, end="")
#         if(line == "\n"):
#             if max < current:
#                 max = current
#             current = 0
#         else:
#             current += int(line)
#     print("Done:" + str(max))
    

calories = []
current = 0
with open("01.txt") as file:
    for line in file:
        print(line, end="")
        if(line == "\n"):
            calories.append(current)
            current = 0
        else:
            current += int(line)

calories.sort(reverse=True)
print(calories)
print(calories[0]+calories[1]+calories[2])