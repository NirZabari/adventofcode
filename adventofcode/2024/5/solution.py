from collections import defaultdict
import heapq

file = "./input.txt"
with open(file, "r") as f:
    lines = f.readlines()

sep_lind_ind = [i for i, line in enumerate(lines) if line.strip() == '']
ordering_rules_input = lines[:sep_lind_ind[0]]
updates_input = lines[sep_lind_ind[0]+1:]


# =================================================================
# Part 1
# =================================================================

total = 0
# Store ordering rules
ordering_rules = set()
for line in ordering_rules_input:
    X, Y = map(int, line.split('|'))
    ordering_rules.add((X, Y))

# Process updates
for update in updates_input:
    pages = list(map(int, update.split(',')))
    page_positions = {page: idx for idx, page in enumerate(pages)}
    is_valid = True
    for X, Y in ordering_rules:
        if X in page_positions and Y in page_positions:
            if page_positions[X] >= page_positions[Y]:
                is_valid = False
                break
    if is_valid:
        middle_page = pages[len(pages) // 2]
        total += middle_page

print(total)

# =================================================================
# Part 2
# =================================================================

total = 0
# Store ordering rules
ordering_rules = set()
for line in ordering_rules_input:
    X, Y = map(int, line.split("|"))
    ordering_rules.add((X, Y))


def reorder_update(pages, ordering_rules):
    # Build graph and compute indegrees
    graph = defaultdict(list)
    indegree = defaultdict(int)
    pages_set = set(pages)
    for page in pages:
        indegree[page] = 0  # Initialize indegree

    for X, Y in ordering_rules:
        if X in pages_set and Y in pages_set:
            graph[X].append(Y)
            indegree[Y] += 1

    # Use a max-heap to select the page with the highest page number
    heap = [-page for page in pages if indegree[page] == 0]
    heapq.heapify(heap)

    sorted_pages = []
    while heap:
        current = -heapq.heappop(heap)
        sorted_pages.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(heap, -neighbor)

    return sorted_pages


# Process updates
for update in updates_input:
    pages = list(map(int, update.split(",")))
    page_positions = {page: idx for idx, page in enumerate(pages)}
    is_valid = True
    for X, Y in ordering_rules:
        if X in page_positions and Y in page_positions:
            if page_positions[X] >= page_positions[Y]:
                is_valid = False
                break
    if not is_valid:
        pages = reorder_update(pages, ordering_rules)
        middle_page = pages[len(pages) // 2]
        total += middle_page

print(total)
