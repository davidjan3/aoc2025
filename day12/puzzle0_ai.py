# Proper working solution with AI assistance
from functools import cache

type Shape = list[list[bool]]
type Region = tuple[tuple[int, int], list[int]]
type Variant = tuple[tuple[int, ...], int, int, int]
type Placement = tuple[tuple[int, int], ...]


def rotate(shape: Shape) -> Shape:
    return [list(row) for row in zip(*shape[::-1])]


def make_variations(shape: Shape) -> list[Shape]:
    variations: list[Shape] = []
    seen: set[tuple[tuple[bool, ...], ...]] = set()
    for flip in (False, True):
        current = [row[:] for row in shape]
        if flip:
            current = list(reversed(current))
        rotated = current
        for _ in range(4):
            key = tuple(tuple(row) for row in rotated)
            if key not in seen:
                seen.add(key)
                variations.append([r[:] for r in rotated])
            rotated = rotate(rotated)
    return variations


def shape_to_variant(shape: Shape) -> Variant:
    rows: list[int] = []
    area = 0
    for line in shape:
        mask = 0
        for idx, cell in enumerate(line):
            if cell:
                mask |= 1 << idx
                area += 1
        rows.append(mask)
    return (tuple(rows), len(shape[0]), len(shape), area)


def placement_fits(space: tuple[int, ...], placement: Placement) -> bool:
    for row_idx, mask in placement:
        if space[row_idx] & mask:
            return False
    return True


def iter_new_states(space: tuple[int, ...], placements: list[Placement]):
    for placement in placements:
        rows = list(space)
        for row_idx, mask in placement:
            if rows[row_idx] & mask:
                break
            rows[row_idx] |= mask
        else:
            yield tuple(rows)


def count_options(space: tuple[int, ...], placements: list[Placement], best_so_far: int | None) -> int:
    count = 0
    for placement in placements:
        if placement_fits(space, placement):
            count += 1
            if best_so_far is not None and count >= best_so_far:
                break
    return count


def draw_state(state: tuple[int, ...], width: int) -> str:
    return "\n".join(
        "".join("#" if row & (1 << x) else "." for x in range(width))
        for row in state
    )


with open("./day12/input.txt", "r", encoding="utf-8") as handle:
    raw_input = handle.read().strip()

sections = [section for section in raw_input.split("\n\n") if section.strip()]
shape_sections = sections[:-1]
region_section = sections[-1]

shapes: list[Shape] = []
for block in shape_sections:
    _, grid = block.split(":\n", 1)
    shapes.append([[char == "#" for char in line] for line in grid.splitlines()])

regions: list[Region] = []
for line in region_section.splitlines():
    line = line.strip()
    if not line:
        continue
    dims, payload = line.split(": ")
    width, height = (int(n) for n in dims.split("x"))
    counts = [int(n) for n in payload.split()]
    regions.append(((width, height), counts))

shape_variants: list[list[Variant]] = []
shape_areas: list[int] = []
for shape in shapes:
    variants: list[Variant] = []
    for variant_shape in make_variations(shape):
        variant = shape_to_variant(variant_shape)
        if variant not in variants:
            variants.append(variant)
    shape_variants.append(variants)
    shape_areas.append(variants[0][3])


def build_placements(variant: Variant, width: int, height: int) -> list[Placement]:
    rows, v_w, v_h, _ = variant
    placements: list[Placement] = []
    if v_w > width or v_h > height:
        return placements

    for top in range(height - v_h + 1):
        for left in range(width - v_w + 1):
            placement = tuple((top + idx, rows[idx] << left) for idx in range(v_h))
            placements.append(placement)
    return placements


def solve_region(dims: tuple[int, int], counts: list[int]):
    width, height = dims
    counts_tuple = tuple(counts)

    placements_by_shape: list[list[Placement]] = []
    for variants in shape_variants:
        placements: list[Placement] = []
        for variant in variants:
            placements.extend(build_placements(variant, width, height))
        placements_by_shape.append(placements)

    needed_cells = sum(count * shape_areas[idx] for idx, count in enumerate(counts_tuple))
    if needed_cells > width * height:
        return False, tuple(0 for _ in range(height))

    empty_state = tuple(0 for _ in range(height))

    @cache
    def search(state: tuple[int, ...], remaining: tuple[int, ...]):
        if not any(remaining):
            return True, state

        best_shape = -1
        best_options = None

        for idx, left in enumerate(remaining):
            if left == 0:
                continue
            placements = placements_by_shape[idx]
            if not placements:
                return False, state

            option_count = count_options(state, placements, best_options)
            if option_count == 0:
                return False, state
            if best_options is None or option_count < best_options:
                best_shape = idx
                best_options = option_count
                if best_options == 1:
                    break

        next_remaining = list(remaining)
        next_remaining[best_shape] -= 1
        next_remaining_tuple = tuple(next_remaining)

        for new_state in iter_new_states(state, placements_by_shape[best_shape]):
            solved, solved_state = search(new_state, next_remaining_tuple)
            if solved:
                return True, solved_state

        return False, state

    return search(empty_state, counts_tuple)


solved_regions = 0
for idx, (dims, counts) in enumerate(regions):
    solved, final_state = solve_region(dims, counts)
    print(f"Region {idx} ({dims[0]}x{dims[1]})")
    if solved:
        solved_regions += 1
        print(draw_state(final_state, dims[0]))
    else:
        print("No tiling found")
    print()

print(solved_regions)