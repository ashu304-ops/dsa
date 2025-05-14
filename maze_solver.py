from collections import deque

maze = [
    ['S', '0', '1', '0'],
    ['1', '0', '1', '0'],
    ['0', '0', '0', '0'],
    ['1', '1', '0', 'E']
]

# Directions: right, down, left, up
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_start(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                return (row, col)
    return None

def is_valid_move(maze, row, col):
    return (0 <= row < len(maze) and 
            0 <= col < len(maze[0]) and 
            maze[row][col] != '1')

def solve_maze(maze):
    start = find_start(maze)
    if not start:
        print("No start point")
        return

    queue = deque([start])
    parent = {start: None}
    visited = set([start])

    while queue:
        current = queue.popleft()
        row, col = current

        if maze[row][col] == 'E':
            print("Found the exit!")
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Path:", path)
            return  # Stop after finding the path

        for dx, dy in direction:
            new_row, new_col = row + dx, col + dy
            next_pos = (new_row, new_col)

            if is_valid_move(maze, new_row, new_col) and next_pos not in visited:
                queue.append(next_pos)
                visited.add(next_pos)
                parent[next_pos] = current

    print("No path to the exit found.")

# Run the maze solver
solve_maze(maze)
