file = open("./day3/input.txt", "r")
input = file.read()

batteries = [[int(n) for n in line] for line in input.split("\n")]

sum = 0
for battery in batteries:
    first_index = battery.index(max(battery[:-1]))
    joltage = int(str(battery[first_index]) + str(max(battery[first_index + 1 :])))
    print(joltage)
    sum += joltage

print(sum)
