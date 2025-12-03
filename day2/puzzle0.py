file = open("./day2/input.txt", "r")
input = file.read()

ranges_str = input.split(",")
print(ranges_str)


def is_invalid(n: int):
    n_str = str(n)
    return len(n_str) % 2 == 0 and n_str[: len(n_str) // 2] == n_str[len(n_str) // 2 :]


ranges_n: list[list[int]] = []
for range_str in ranges_str:
    range_n: list[int] = [int(n) for n in range_str.split("-")]
    ranges_n.append(range_n)

sum = 0
for range_n in ranges_n:
    for i in range(range_n[0], range_n[1] + 1):
        if is_invalid(i):
            sum += i

print(sum)
