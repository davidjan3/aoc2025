import re

file = open("./day6/input.txt", "r")
input = file.read()

lines = [re.split(r"\s+", line.strip()) for line in input.split("\n")]

sum = 0
for i in range(len(lines[-1])):
    op = lines[-1][i]
    result = int(lines[0][i])
    for n in range(1, len(lines) - 1):
        if op == "+":
            result += int(lines[n][i])
        else:
            result *= int(lines[n][i])
    sum += result

print(sum)
