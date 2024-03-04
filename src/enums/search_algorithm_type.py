from enum import Enum
"""
Enum for the type of search algorithm used by an agent, used as the result from buttons on the menu screen
"""
class SearchAlgoType(Enum):
    BREADTH = 'Breadth-First'
    DEPTH = 'Depth-First'
    UNIFORM = 'Uniform-Cost'
    HUMAN = 'Human'
    GREEDY = 'Greedy'
    A_STAR = 'A*'
    A_STAR_ALL_CELLS = 'A* (goal in all cells)'
    MINIMAX = 'Minimax'
    EXPECTIMAX = 'Expectimax'
    REFLEX = 'Reflex'