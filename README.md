# Maze-Generator-and-Solver
This project generates random mazes and solves them using Dijkstra's algorithm to find the shortest path. It features an interactive interface allowing both auto-solve and manual navigation of the maze.

## Features

- **Random Maze Generation**: Generates a random maze using a backtracking algorithm.
- **Maze Solver**: Solves the maze using Dijkstra's algorithm.
- **Interactive Navigation**: Allows the user to manually navigate the maze using WASD keys.
- **Auto-Solve Option**: Option to automatically solve the maze, with the solution path being visually displayed.
- **Adjustable Maze Size**: The size of the maze can be modified dynamically using an input box.
- **Elapsed Time Display**: Displays the elapsed time for the auto-solve feature.


## Installation
1. Download and install [Processing](https://processing.org/) [use Python Mode]
2. Clone this repository or download the ZIP file:
   ```bash
   git clone https://github.com/kmusadiqpasha/cellular-automata-visualizer

3. Open the .pde files for each simulation in Processing.
4. Run the sketches and watch the cellular automata come to life!
   


Usage
Generate Maze: Click the "Generate Maze" button to create a new random maze.
Manual Solve: Use the WASD keys to navigate through the maze. Avoid walls (black cells).
Auto Solve: Click the "Auto-Solve" button to solve the maze automatically using Dijkstra's algorithm.
Adjust Maze Size: Enter a new maze size in the input box (default: 50x50) and press Enter to update the maze.

Code Overview
Maze Class: Responsible for generating the maze and solving it using Dijkstra's algorithm.
Global Variables: Includes maze size, cursor position, and elapsed time tracking.
UI Controls: Buttons for generating the maze, toggling auto-solve, and updating the maze size

How It Works
Maze Generation: The maze is generated using a backtracking algorithm, starting from a given point (top-left corner). The maze is a grid of cells, where walls are represented by -2 and open paths by -1.
Dijkstra's Algorithm: This algorithm is used to find the shortest path from the start to the end of the maze. The maze solver uses a priority queue (heap) to explore the grid efficiently.
Manual Navigation: The user can manually move through the maze using the W, A, S, and D keys to simulate a step-by-step solution.
Auto-Solving: When enabled, the maze is automatically solved by the algorithm, and the solution path is shown in the maze grid.


Maze Generation and Solving
Maze Generation: The maze is generated using a backtracking algorithm. Starting from the top-left corner, it recursively explores neighboring cells, carving paths (-1) and marking walls (-2). The algorithm backtracks when no unvisited neighbors remain, ensuring a perfect maze with one solution.

Maze Solving: Dijkstra's algorithm is used to find the shortest path from the start to the end. It explores neighboring cells, updating the shortest path cost, and reconstructs the solution path once the end is reached. The path is then marked on the maze (2).


<img src='https://github.com/MusadiqPasha/Cellular-Automata-Visualizer/blob/main/ca%20demo/Larger_than_life.gif'>


Visualization
During the maze generation, the walls (-2) are drawn as black squares, while the open paths (-1) are displayed as white squares.
The start point is typically highlighted as a red square (1).
The path solution is displayed as purple squares (2) during the auto-solve process.


### License
- This project is licensed under the MIT License - see the LICENSE file for details.

##
## Just follow me and Star ⭐ my repository 
## Thank You!!



