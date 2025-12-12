import z3

type Machine = tuple[list[bool], list[list[int]], list[int]]

file = open("./day10/input.txt", "r")
input = file.read()
machines: list[Machine] = []
for line in input.split("\n"):
    split0 = line.find("] (")
    split1 = line.find(") {")
    lights_str = line[1:split0]
    buttons_str = line[split0 + 2 : split1 + 1]
    joltages_str = line[split1 + 3 : -1]
    lights = [char == "#" for char in lights_str]
    buttons = [
        [int(char) for char in button_str[1:-1].split(",")]
        for button_str in buttons_str.split(" ")
    ]
    joltages = [int(char) for char in joltages_str.split(",")]
    machines.append((lights, buttons, joltages))

total = 0
for machine in machines:
    presses = 0
    while True:
        presses += 1
        s = z3.Solver()
        x = [z3.Int("x"+str(i)) for i in range(len(machine[1]))]
        s.add([var >= 0 for var in x])
        s.add(z3.Sum(x) == presses) 
        for j in range(len(machine[2])):
            s.add(z3.Sum([x[i] for i in range(len(machine[1])) if j in machine[1][i]]) == machine[2][j])
        if s.check() == z3.sat:
            model = s.model()
            total += sum([model[xn].as_long() for xn in x])
            break
print(total)