# Used AI for this one, couldn't come up with anything that wouldn't blow up my RAM without looking up algorithms.
from collections import deque

file = open("./day11/input.txt", "r")
input = file.read()
links: dict[str, set[str]] = {split[0]: set(split[1].split(" ")) for split in (line.split(": ") for line in input.split("\n") if line)}

all_links = set(links.keys())
for nxt in links.values():
    all_links.update(nxt)
for link in all_links:
    links.setdefault(link, set())

indegree = {link: 0 for link in all_links}
for link, nxt in links.items():
    for dst in nxt:
        indegree[dst] += 1

order: list[str] = []
queue = deque(link for link in all_links if indegree[link] == 0)
while len(queue):
    cur = queue.popleft()
    order.append(cur)
    for dst in links[cur]:
        indegree[dst] -= 1
        if indegree[dst] == 0:
            queue.append(dst)

pos = {link: i for i, link in enumerate(order)}

def count(start: str) -> dict[str, int]:
    totals = {link: 0 for link in order}
    totals[start] = 1
    for link in order[pos[start]:]:
        cur = totals[link]
        if not cur:
            continue
        for dst in links[link]:
            if pos[dst] > pos[link]:
                totals[dst] += cur
    return totals

svr_paths = count("svr")
fft_paths = count("fft")
dac_paths = count("dac")

total = svr_paths["fft"] * fft_paths["dac"] * dac_paths["out"]
total += svr_paths["dac"] * dac_paths["fft"] * fft_paths["out"]
print(total)