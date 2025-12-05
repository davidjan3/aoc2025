file = open("./day5/input.txt", "r")
input = file.read()

fresh = [
    (int(row.split("-")[0]), int(row.split("-")[1]))
    for row in input.split("\n\n")[0].split("\n")
]

avail = [int(n) for n in input.split("\n\n")[1].split("\n")]

count = 0

for product in avail:
    for range in fresh:
        if product >= range[0] and product <= range[1]:
            count += 1
            break

print(count)
