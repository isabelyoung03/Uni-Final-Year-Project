# Final Year Project

## Single-Agent and Multi-Agent Search in Maze Games by Isabel Young

This is a Python project using Pygame to model agents using different search algorithms in a maze game of my own design. I have implemented a simple reflex agent, as well as goal-based agents that use the following search algorithms:
- Breadth-first search
- Depth-first search
- Uniform-cost search
- A* search
- Greedy search
- Minimax
- Expectimax

## Getting started 
1. Navigate to PROJECT directory via the terminal
2. Run the main script:
    ```bash
    python3 main.py
    ```
3. Select desired maze size and agent type
    - if you have chosen Greedy or A* (goal in all cells), you can choose one of three mazes available for your selected maze size
    - if you have chosen Minimax or Expectimax, you can choose how many opponents are in the maze
    - select 'human' to be able to play the game yourself!
4. Press start
5. Depending on the type of agent you chose, you may have the option to choose the heuristic function the algorithm uses
6. Press the play button to start and watch the player agent navigate the maze
7. Press the home button if you want to select a new maze/search algorithm


## Analysis feature
If you choose Breadth-First or Depth-First, you can press the "Analyse" button to produce a CSV file of results. This CSV file contains the number of moves the agent takes to reach the goal, for each possible location of the goal. This file is saved into the "results" directory of the project.

## Installation
To install the required dependencies for this project, run the following command:
```bash
pip install -r requirements.txt
```

## Demo video
https://youtu.be/wohps3uBbR4?si=-xxacss_Vlsyxicg

