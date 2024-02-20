# Final Year Project

## Single-Agent and Multi-Agent Search in Maze Games by Isabel Young

This is a Python project using Pygame to model different search algorithms for agents in a maze game of my own design.

## Getting started 
1. Navigate to PROJECT directory via the terminal
2. Run the main script:
    ```bash
    python3 main.py
    ```
3. Select desired maze size and search algorithm
    - if you have chosen Greedy or A* (goal in all cells), you can choose one of three mazes available for your selected maze size
    - if you have chosen Minimax or Expectimax, you can choose how many opponents are in the maze
4. Press start
5. Depending on the type of agent you chose, you may have the option to choose the heuristic function the algorithm uses
6. Press the play button to start and watch the player agent navigate the maze
7. Press the home button if you want to select a new maze/search algorithm

## Analysis feature
If you choose Breadth-First or Depth-First, you can press the "Analyse" button to produce a CSV file of results. This CSV file contains the moves the agent takes to reach the goal, for each possible location of the goal. This file is saved into the "results" directory of the project.

## Installation
To install the required dependencies for this project, run the following command:
```bash
pip install -r requirements.txt
```

## Demo video
https://youtu.be/oMTAwV9lH40

