file = open("./day1/input.txt", "r")
input = file.read()

rotations = input.split("\n")
dial_len = 100
current = 50

zero_count = 0

for rotation in rotations:
    dir = -1 if rotation[:1] == "L" else 1
    dist = int(rotation[1:])
    current = (current + dist * dir) % dial_len
    if current == 0:
        zero_count += 1

print(zero_count)
