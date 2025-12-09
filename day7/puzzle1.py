file = open("./day7/input.txt", "r")
input = file.read()

lines = input.split("\n")
splitters: list[dict[int, int]] = []

for i in range(len(lines)):
    current: dict[int, int] = {}
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            current[j] = 0
    if len(current):
        splitters.append(current)

for i in reversed(range(len(splitters))):
    for j in splitters[i]:
        left = 1
        right = 1
        k = i + 1
        while (left == 1 or right == 1) and k < len(splitters):
            if left == 1:
                left = splitters[k][j - 1] if (j - 1) in splitters[k] else 1
            if right == 1:
                right = splitters[k][j + 1] if (j + 1) in splitters[k] else 1
            k += 1
        splitters[i][j] = left + right


print(splitters[0][lines[0].index("S")])
