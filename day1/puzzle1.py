import math


file = open("./day1/input.txt", "r")
input = file.read()

rotations = input.split("\n")
dial_len = 100
current = 50

zero_count = 0

for rotation in rotations:
    dir = -1 if rotation[:1] == "L" else 1
    dist = int(rotation[1:])
    pre_move = current
    passes_through_zero = (
        math.ceil((current + dir * dist) // dial_len)
        if dir == 1
        else math.ceil((dial_len - current + -dir * dist) // dial_len)
        - (1 if pre_move == 0 else 0)
    )
    current = (current + dir * dist) % dial_len
    print(pre_move, rotation, passes_through_zero, current)
    zero_count += abs(passes_through_zero)

print(zero_count)
