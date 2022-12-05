print(sum("B X\nC Y\nA Z\nA X\nB Y\nC Z\nC X\nA Y\nB Z\n".index(line)//4 + 1 for line in open("02.txt")))

print(sum("B X\nC X\nA X\nA Y\nB Y\nC Y\nC Z\nA Z\nB Z\n".index(line)//4 + 1 for line in open("02.txt")))