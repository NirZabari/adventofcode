file = "./input.txt"
with open(file, 'r') as f:
    graph = f.read()

graph = [line.strip() for line in graph.split('\n') if line.strip()]

directions = [
    (0, 1),   # right
    (1, 1),   # down-right  
    (1, 0),   # down
    (1, -1),  # down-left
    (0, -1),  # left
    (-1, -1), # up-left
    (-1, 0),  # up
    (-1, 1)   # up-right
]

def check_word(grid, row, col, direction, target='XMAS'):
    """Check if word exists starting at row,col going in direction"""
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        return False
        
    word = ''
    curr_row, curr_col = row, col
    
    # Build word in this direction until we hit boundary or word length
    for _ in range(len(target)):
        if not (0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])):
            return False
        word += grid[curr_row][curr_col]
        curr_row += direction[0]
        curr_col += direction[1]
        
    return word == target

# Count total occurrences
count = 0
for row in range(len(graph)):
    for col in range(len(graph[0])):
        # From each position, check all 8 directions
        for direction in directions:
            if check_word(graph, row, col, direction):
                count += 1

print(f"Found {count} occurrences of XMAS")


# find all MAS in shape of X
def check_xmas(grid, row, col):
    def in_range(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
    
    def is_valid_diag(n1_value, n2_value):
        return n1_value == 'M' and n2_value == 'S' or n1_value == 'S' and n2_value == 'M'
    
    # Validate input grid and position
    if not grid or not grid[0]:
        return False
    
    if not in_range(row, col):
        return False

    # Must have 'A' at center
    if grid[row][col] != 'A':
        return False

    top_left_indices = row-1, col-1
    bottom_right_indices = row+1, col+1
    
    value_top_left_indices = graph[top_left_indices[0]][top_left_indices[1]]
    value_bottom_right_indices = graph[bottom_right_indices[0]][bottom_right_indices[1]]
    valid_left_diag = is_valid_diag(value_top_left_indices, value_bottom_right_indices)
    
    top_right_indices = row-1, col+1
    bottom_left_indices = row+1, col-1
    value_top_right_indices = graph[top_right_indices[0]][top_right_indices[1]]
    value_bottom_left_indices = graph[bottom_left_indices[0]][bottom_left_indices[1]]
    valid_right_diag = is_valid_diag(value_top_right_indices, value_bottom_left_indices)

    return valid_left_diag and valid_right_diag

count = 0
for row in range(1, len(graph) - 1):
    for col in range(1, len(graph[0]) - 1):
        if check_xmas(graph, row, col):
            count += 1
            
print(f"Found {count} X-MAS patterns")
