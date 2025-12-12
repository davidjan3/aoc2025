type Space = list[list[bool]]
type Shape = Space
type Region = tuple[tuple[int, int], list[int]]

file = open("./day12/input.txt", "r")
input = file.read()
shapes: list[Shape] = [[[char == "#" for char in line] for line in block.split("\n")] for block in [block[3:] for block in input.split("\n\n")][:-1]]
regions: list[Region] = [(tuple(int(n) for n in line.split(": ")[0].split("x")), [int(n) for n in line.split(": ")[1].split(" ")]) for line in (input.split("\n\n")[-1]).split("\n")]

# def make_variations(shape):
#     variations = []
#     for _ in range(2):
#         new_shape = shape.copy()
#         if _ == 1:
#             new_shape = [e for e in reversed(new_shape)]
        
#         variations.append(new_shape.copy())
#         for r in range(3):
#             new_shape = list(zip(*new_shape[::-1]))
#             variations.append(new_shape.copy())
#     return variations

# def draw_shape(shape):
#     return "\n".join(["".join(["#" if el else "." for el in line]) for line in shape])

# def place(space, shape, at_x, at_y) -> bool:
#     for y in range(len(shape)):
#         for x in range(len(shape[0])):
#             if shape[y][x]:
#                 if space[y+at_y][x+at_x]:
#                     return False
#                 space[y+at_y][x+at_x] = True
#     return True


# shapes_var = [make_variations(shape) for shape in shapes]

# def recurse(space, to_place):
#     s_w = len(space[0])
#     s_h = len(space)
#     for shape in shapes_var[to_place[0]]:
#         w = len(shape[0])
#         h = len(shape)
#         for x in range(s_w-w+1):
#             for y in range(s_h-h+1):
#                 new_space = [[el for el in row] for row in space]
#                 if place(new_space, shape, x, y):
#                     if len(to_place) > 1:
#                         if recurse(new_space, to_place[1:]):
#                             return True
#                     else:
#                         return True

#     return False

# count = 0
# for region in regions:
#     space = [[False for _ in range(region[0][0])] for _ in range(region[0][1])]
#     to_place = [i for i in range(len(region[1])) for _ in range(region[1][i])]
#     count += int(recurse(space, to_place))

count = 0
for region in regions:
    if sum(region[1]) * 9 <= region[0][0] * region[0][1]:
        count += 1
print(count)

# Fuck me what did I do all this work for