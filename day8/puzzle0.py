import math

file = open("./day8/input.txt", "r")
n = 1000
input = file.read()

lines = input.split("\n")
boxes = [[int(x) for x in line.split(",")] for line in lines]


def distance(b0: list[int], b1: list[int]):
    return math.sqrt((b1[0] - b0[0]) ** 2 + (b1[1] - b0[1]) ** 2 + (b1[2] - b0[2]) ** 2)


distances: list[tuple[tuple[list[int], list[int]], float]] = []

for i0 in range(len(boxes)):
    b0 = boxes[i0]
    for i1 in range(i0 + 1, len(boxes)):
        b1 = boxes[i1]
        distances.append(((b0, b1), distance(b0, b1)))

distances.sort(key=lambda dist: dist[1])
distances = distances[:n]

circuits = [[box] for box in boxes]

for pair in distances:
    b0 = pair[0][0]
    b1 = pair[0][1]
    c0 = next(circuit for circuit in circuits if (b0 in circuit))
    c1 = next(circuit for circuit in circuits if (b1 in circuit))
    if c0 == c1:
        continue
    circuits[circuits.index(c0)] += c1
    circuits.remove(c1)

circuits.sort(key=lambda circ: -len(circ))

print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
