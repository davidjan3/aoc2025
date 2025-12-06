file = open("./day6/input.txt", "r")
input = file.read()

lines = input.split("\n")


def get_num(x: int):
    num = 0
    exp = 0
    for i in range(len(lines) - 1):
        cur = lines[-(i + 2)][x]
        if cur != " ":
            num += int(cur) * 10**exp
            exp += 1
    return num if exp > 0 else -1


total = 0

op = ""
result = 0
for i in range(len(lines[-1])):
    num = get_num(i)
    if lines[-1][i] != " ":
        total += result
        op = lines[-1][i]
        result = num
    elif num > -1:
        if op == "+":
            result += num
        else:
            result *= num
total += result

print(total)
