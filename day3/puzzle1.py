file = open("./day3/input.txt", "r")
input = file.read()

BATT_COUNT = 12

batteries = [[int(n) for n in line] for line in input.split("\n")]

sum = 0
for battery in batteries:
    joltage = ""
    prev_index = -1
    for i in range(BATT_COUNT):
        prev_index = (prev_index + 1) + battery[prev_index + 1 :].index(
            max(battery[prev_index + 1 : -(BATT_COUNT - i - 1) or None])
        )
        joltage += str(battery[prev_index])
    print(joltage)
    sum += int(joltage)

print(sum)
