file = open("./day7/input.txt", "r")
input = file.read()

lines = input.split("\n")
beams = {lines[0].index("S")}

splits = 0
for i in range(1, len(lines)):
    for j in beams.copy():
        if lines[i][j] == "^":
            splits += 1
            beams.remove(j)
            if j > 0:
                beams.add(j - 1)
            if j < len(lines[0]) - 1:
                beams.add(j + 1)

print(splits)
