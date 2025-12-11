type Coord = tuple[int, int]
type Edge = tuple[Coord, Coord]

file = open("./day9/input.txt", "r")
input = file.read()
coords: list[Coord] = [
    (int(split[0]), int(split[1]))
    for split in [line.split(",") for line in input.split("\n")]
]
edges: list[Edge] = [
    (coords[i], coords[(i + 1) % len(coords)]) for i in range(len(coords))
]


def contains_point(point: Coord, edges: list[Edge]) -> bool:
    count = 0

    for edge in edges:
        if (
            (edge[0][0] > point[0] and edge[1][0] > point[0])
            or min(edge[0][1], edge[1][1]) > point[1]
            or max(edge[0][1], edge[1][1]) < point[1]
        ):
            continue

        if edge[0][1] == edge[1][1]:
            intersection_x = min(edge[0][0], edge[1][0])
            if point[1] == edge[0][1] and min(edge[0][0], edge[1][0]) <= point[
                0
            ] <= max(edge[0][0], edge[1][0]):
                return True
        else:
            intersection_x = edge[0][0]

        if intersection_x == point[0]:
            return True
        elif intersection_x < point[0]:
            if (edge[0][1] != point[1] and edge[1][1] != point[1]) or (
                edge[1][1] != edge[0][1] and point[1] == max(edge[0][1], edge[1][1])
            ):
                count += 1
    return count % 2 == 1


def intersects(edge0: Edge, edge1: Edge):
    if edge0[0][0] == edge0[1][0] and edge1[0][1] == edge1[1][1]:
        return (
            min(edge0[0][1], edge0[1][1]) < edge1[0][1]
            and max(edge0[0][1], edge0[1][1]) > edge1[0][1]
            and min(edge1[0][0], edge1[1][0]) < edge0[0][0]
            and max(edge1[0][0], edge1[1][0]) > edge0[0][0]
        )
    elif edge0[0][1] == edge0[1][1] and edge1[0][0] == edge1[1][0]:
        return (
            min(edge0[0][0], edge0[1][0]) < edge1[0][0]
            and max(edge0[0][0], edge0[1][0]) > edge1[0][0]
            and min(edge1[0][1], edge1[1][1]) < edge0[0][1]
            and max(edge1[0][1], edge1[1][1]) > edge0[0][1]
        )
    return False


max_area = 0
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        corners = [
            coords[i],
            (coords[i][0], coords[j][1]),
            coords[j],
            (coords[j][0], coords[i][1]),
        ]
        rect_edges: list[Edge] = [
            (corners[k], corners[(k + 1) % len(corners)]) for k in range(len(corners))
        ]
        inner_point = (
            min(coords[i][0], coords[j][0]) + 1,
            min(coords[i][1], coords[j][1]) + 1,
        )
        if contains_point(inner_point, edges):
            if len([True for corner in corners if contains_point(corner, edges)]) == 4:
                has_intersection = False
                for rect_edge in rect_edges:
                    for edge in edges:
                        if intersects(edge, rect_edge):
                            has_intersection = True
                            break
                    if has_intersection:
                        break
                if not has_intersection:
                    max_area = max(
                        max_area,
                        (abs(coords[i][0] - coords[j][0]) + 1)
                        * (abs(coords[i][1] - coords[j][1]) + 1),
                    )
print(max_area)
