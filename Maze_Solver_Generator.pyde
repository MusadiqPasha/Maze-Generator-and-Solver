
# Globals
global grid, XX, YY, start_time, auto_solve, cursor_row, cursor_col, maze_solution, elapsed_time, input_box_size, input_active_size, w
import random
import heapq

# Default maze dimensions
XX, YY = 50, 50
grid = []
auto_solve = False  # Toggle for auto-solving
cursor_row, cursor_col = 1, 1  # Start position
maze_solution = []
start_time = None
elapsed_time = 0  # Time tracking

# Input box state
input_box_size = "50"
input_active_size = False

class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = [[-2 for _ in range(size)] for _ in range(size)]  # Initialize maze with walls (-2)
        self.visited = [[False for _ in range(size)] for _ in range(size)]  # Track visited cells
        self.stack = []  # Stack for backtracking

    def is_valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and not self.visited[x][y]

    def generate(self, start_x, start_y):
        self.stack.append((start_x, start_y))
        self.visited[start_x][start_y] = True
        self.maze[start_x][start_y] = -1

        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        while self.stack:
            current_x, current_y = self.stack[-1]
            neighbors = []

            for dx, dy in directions:
                nx, ny = current_x + dx, current_y + dy
                if self.is_valid(nx, ny):
                    neighbors.append((nx, ny, dx, dy))

            if neighbors:
                nx, ny, dx, dy = random.choice(neighbors)
                self.maze[current_x + dx // 2][current_y + dy // 2] = -1
                self.maze[nx][ny] = -1
                self.visited[nx][ny] = True
                self.stack.append((nx, ny))
            else:
                self.stack.pop()

    def solve_maze(self, matrix, start, end):
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        pq = [(0, start[0], start[1])]
        distances = {start: 0}
        predecessors = {}
        visited = set()

        while pq:
            cost, x, y = heapq.heappop(pq)

            if (x, y) == end:
                path = []
                while (x, y) != start:
                    path.append((x, y))
                    x, y = predecessors[(x, y)]
                path.append(start)
                return cost, path[::-1]

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != -2:
                    new_cost = cost + 1
                    if (nx, ny) not in distances or new_cost < distances[(nx, ny)]:
                        distances[(nx, ny)] = new_cost
                        predecessors[(nx, ny)] = (x, y)
                        heapq.heappush(pq, (new_cost, nx, ny))

        return -1, []

# Initialize maze
def initialize_maze():
    global grid, maze_solution, w, elapsed_time, start_time,auto_solve
    maze = Maze(XX)
    maze.generate(1, 1)
    grid = maze.maze
    grid[1][1] = 1
    grid[XX - 1][XX - 1] = 1
    _, maze_solution = maze.solve_maze(grid, (1, 1), (XX - 1, XX - 1))
    elapsed_time = 0
    start_time = 0
    auto_solve = False 
    w = 900 // XX

initialize_maze()

# Setup and draw
def setup():
    size(950, 950)  # Extra height for buttons and input boxes

def draw():
    global cursor_row, cursor_col, maze_solution, auto_solve, start_time, elapsed_time, w
    background(200)
    
    # Draw maze
    x, y = 0, 0
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if row_index == cursor_row and col_index == cursor_col and not auto_solve:
                fill(0, 0, 255)
            elif col == -2:
                fill(0)
            elif col == 1:
                fill(255, 0, 0)
            elif col == 2:
                fill(125, 55, 125)
            else:
                fill(255)

            rect(x, y, w, w)
            x += w
        y += w
        x = 0

    # Auto-solve button
    fill(100, 200, 100) if auto_solve else fill(200, 100, 100)
    rect(320, 910, 200, 30)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(16)
    text("Auto-Solve" if not auto_solve else "Manual Solve", 425, 925)

    # Generate Maze button
    fill(150, 150, 250)
    rect(50, 910, 200, 30)
    fill(0)
    text("Generate Maze", 150, 925)

    # Time display
    fill(255)
    rect(560, 910, 150, 30)
    fill(0)
    textSize(16)
    text("Elapsed Time: " + str(elapsed_time) + "s", 640, 925)

    # Input box for maze size
    fill(150,250,0)
    rect(730, 910, 150, 30)
    fill(0)
    textSize(16)
    text("Maze Size: " + str(input_box_size), 810, 925)
    
    
    # Check completion
    if cursor_row == XX - 1 and cursor_col == YY - 1 and not auto_solve:
        cursor_row = 1
        cursor_col = 1
        auto_solve = False
        elapsed_time = 0
        start_time = 0
        
        #noLoop()
        
    # Auto-solve animation
    if auto_solve and maze_solution:
        nx, ny = maze_solution.pop(0)
        grid[nx][ny] = 2
        elapsed_time = millis() // 1000 - start_time  # Update elapsed time



def mousePressed():
    global auto_solve, start_time, elapsed_time, grid, maze_solution, cursor_row, cursor_col, XX, input_active_size, w

    if 320 <= mouseX <= 520 and 910 <= mouseY <= 940:
        auto_solve = not auto_solve
        if auto_solve:
            start_time = millis() // 1000
            elapsed_time = 0
        else:
            start_time = millis() // 1000
            elapsed_time = 0

    elif 50 <= mouseX <= 250 and 910 <= mouseY <= 940:
        auto_solve = False
        initialize_maze()
        auto_solve = False
        cursor_row, cursor_col = 1, 1
        loop()

    elif 750 <= mouseX <= 850 and 910 <= mouseY <= 940:
        input_active_size = True
    else:
        input_active_size = False

def keyPressed():
    global cursor_row, cursor_col, input_box_size, XX, YY,w , start_time , elapsed_time , auto_solve
    if input_active_size:
        if key in "0123456789":
            input_box_size += key
        elif key == BACKSPACE and len(input_box_size) > 0:
            input_box_size = input_box_size[:-1]
        elif key == ENTER:
            if input_box_size.isdigit():
                XX = max(10, int(input_box_size))  # Update maze width
                YY = XX  # Assuming square grid, you can adjust if different logic is needed
                start_time = 0
                elapsed_time = 0
                auto_solve = False 
                initialize_maze()
                # Reset cursor position to valid point
                cursor_row, cursor_col = 1, 1  # Set to start position (or another valid position)
    
    else:
        if not auto_solve:
            if key in ['w', 'W'] and cursor_row > 0 and grid[cursor_row - 1][cursor_col] != -2:
                cursor_row -= 1
            elif key in ['s', 'S'] and cursor_row < YY - 1 and grid[cursor_row + 1][cursor_col] != -2:
                cursor_row += 1
            elif key in ['a', 'A'] and cursor_col > 0 and grid[cursor_row][cursor_col - 1] != -2:
                cursor_col -= 1
            elif key in ['d', 'D'] and cursor_col < XX - 1 and grid[cursor_row][cursor_col + 1] != -2:
                cursor_col += 1
