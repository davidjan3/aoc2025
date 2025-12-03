file = open("./day2/input.txt", "r")
input = file.read()

ranges_str = input.split(",")
print(ranges_str)


def is_invalid(n: int):
    n_str = str(n)
    for i in range(2, len(n_str) + 1):
        if len(n_str) % i == 0:
            step_size = len(n_str) // i
            first_part = n_str[:step_size]
            invalid = True
            for j in range(1, i):
                if n_str[step_size * j : step_size * (j + 1)] != first_part:
                    invalid = False
                    break
            if invalid == True:
                return True
    return False


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
