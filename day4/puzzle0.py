file = open("./day4/input.txt", "r")
input = file.read()

rolls = [
    [True if char == "@" else False for char in line] for line in input.split("\n")
]


def getAt(x: int, y: int) -> bool:
    global rolls
    if y < 0 or y >= len(rolls):
        return False
    if x < 0 or x >= len(rolls[y]):
        return False
    return rolls[y][x]


count = 0

for y in range(len(rolls)):
    for x in range(len(rolls[y])):
        if not getAt(x, y):
            continue
        c = 0
        for y1 in [-1, 0, 1]:
            for x1 in [-1, 0, 1]:
                if y1 == 0 and x1 == 0:
                    continue
                c += 1 if getAt(x + x1, y + y1) else 0
        count += 1 if c < 4 else 0

print(count)
