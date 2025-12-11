file = open("./day9/input.txt", "r")
input = file.read()
coords = [
    (int(split[0]), int(split[1]))
    for split in [line.split(",") for line in input.split("\n")]
]

max_area = 0
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        max_area = max(
            max_area,
            (abs(coords[i][0] - coords[j][0]) + 1)
            * (abs(coords[i][1] - coords[j][1]) + 1),
        )
print(max_area)
