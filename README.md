# A* Pathfinding Algorithm Visualizer

An interactive and animated visualization of the **A* (A-Star) Pathfinding Algorithm** built using **Python** and **Pygame**.

This project allows users to **design their own maze, run the A* search algorithm, and watch the algorithm explore the grid in real-time**. The visualization clearly demonstrates how nodes are expanded, how heuristics guide the search, and how the optimal path is discovered.

The project is designed to help students, developers, and AI enthusiasts understand how **heuristic search algorithms work internally**, rather than just seeing the final path.

---

# Project Demo

The visualization demonstrates how the algorithm:

- Explores possible paths
- Expands nodes based on priority
- Avoids obstacles
- Reconstructs the optimal path

All of this happens **step-by-step in an animated grid interface**.

---

# Screenshots

## 1. Maze Setup

The user first creates a maze by placing the **start node, goal node, and walls**.

This interactive grid allows experimentation with different maze structures before running the algorithm.

![Maze Setup](screenshots/maze_setup.png)

---

## 2. Real-Time Node Expansion

After pressing **SPACE**, the A* algorithm begins exploring the maze.

- **Green nodes** represent nodes that are currently being explored.
- **Red nodes** represent nodes that have already been evaluated.

This animation shows how the search expands through the grid while prioritizing promising paths.

![Node Expansion](screenshots/node_expansion.png)

---

## 3. Final Shortest Path

Once the goal node is reached, the algorithm reconstructs the optimal route.

The **purple path** represents the shortest path found by the A* algorithm.

![Final Path](screenshots/final_path.png)

---

# Features

- Interactive maze creation
- Real-time A* pathfinding visualization
- Step-by-step node expansion
- Animated search process
- Visual distinction between open and closed nodes
- Automatic shortest path reconstruction
- Grid-based interactive interface

---

# Technologies Used

- Python
- Pygame
- Priority Queue (Heap)

---

# Algorithm Overview

This project implements the **A* Search Algorithm**, a widely used pathfinding algorithm in artificial intelligence.

The algorithm evaluates nodes using the function:

```bash
    f(n) = g(n) + h(n)
```


Where:

- **g(n)** = distance from the start node to the current node
- **h(n)** = heuristic estimate from the current node to the goal
- **f(n)** = estimated total cost of the path through that node

The heuristic used in this implementation is **Manhattan Distance**, which works well for grid-based movement.

```bash
    h(n) = |x1 - x2| + |y1 - y2|
```

This heuristic ensures the algorithm remains both **efficient and optimal**.

---

# Project Structure

```bash
    astar_visualizer/
        │
        ├── main.py
        ├── astar.py
        ├── grid.py
        ├── README.md
        │
        └── screenshots/
        ├── 1. intitalizing start and end points.png
        ├── 2. adding walls.png
        ├── 3. finding path
        └── 4. finding final path.png
```


---

# Installation

Clone the repository:
```bash
    git clone https://github.com/tayade-aniket/astar-visualizer.git
```

Navigate to the project directory:
```bash
    cd astar_visualizer
```

Install the required dependency:
```bash
    pip install pygame
```


---

# Running the Application

Run the program using:
```bash
    python main.py
```

---


A window will open displaying the interactive grid.

---

# Controls

|          Action    |      Control      |
|--------------------|-------------------|
| Place Start Node   | First Left Click  |
| Place Goal Node    | Second Left Click |
| Add Wall           | Left Click        |
| Remove Wall        | Right Click       |
| Run Algorithm      | Press **SPACE**   |
| Clear Grid         | Press **C**       |

---

# Learning Outcomes

This project demonstrates several important concepts in computer science and artificial intelligence:

- Graph search algorithms
- Heuristic-based optimization
- Priority queues
- Grid-based pathfinding
- Algorithm visualization
- Interactive simulation design

It is especially useful for students studying **Artificial Intelligence, Data Structures, or Algorithm Design**.

---

# License

This project is intended for **educational and learning purposes**.

---

# Author

Developed as an interactive project to explore **AI pathfinding algorithms and real-time algorithm visualization** using Python by Mr. Aniket Tayade.