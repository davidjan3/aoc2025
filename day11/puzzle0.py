file = open("./day11/input.txt", "r")
input = file.read()
links: dict[str, list[str]] = {split[0]: split[1].split(" ") for split in (line.split(": ") for line in input.split("\n"))}

paths: list[list[str]] = [["you"]]

while len([path for path in paths if path[-1] != "out"]):
    for i in reversed(range(len(paths))):
        cur = paths[i][-1]
        if cur == "out":
            continue
        nxt = [link for link in links[cur] if not (link in paths[i])]
        if not len(nxt):
            paths.pop(i)
        for j in range(len(nxt)):
            if j == 0:
                paths[i].append(nxt[j])
            else:
                paths.append(paths[i].copy() + [nxt[j]])

print(len(paths))