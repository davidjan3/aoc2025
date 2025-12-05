file = open("./day5/input.txt", "r")
input = file.read()

fresh = [
    [int(row.split("-")[0]), int(row.split("-")[1])]
    for row in input.split("\n\n")[0].split("\n")
]

# Obvious move would be to just add all fresh items to a set and return the length of that set - but that's too easy and unefficient
fresh.sort(key=lambda entry: entry[0])

for i in reversed(range(1, len(fresh))):
    current = fresh[i]
    prev = fresh[i - 1]
    if current[0] == prev[0]:
        prev[1] = max(current[1], prev[1])
        fresh.pop(i)
        continue

for i in reversed(range(1, len(fresh))):
    current = fresh[i]
    prev = fresh[i - 1]
    if current[0] <= prev[1]:
        if current[1] <= prev[1]:
            fresh.pop(i)
            continue
        current[0] = prev[1] + 1

count = sum([range[1] - range[0] + 1 for range in fresh])
print(count)
