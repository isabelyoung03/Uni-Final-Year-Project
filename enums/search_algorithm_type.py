from enum import Enum
"""
Enum for the type of search algorithm used by an agent, used as the result from buttons on the menu screen
"""
class SearchAlgoType(Enum):
    BREADTH = 'Breadth-first'
    DEPTH = 'Depth-first'
    UNIFORM = 'Uniform-cost'
    GREEDY_A_STAR = 'Greedy vs A*'
    MINIMAX = 'Minimax'
    EXPECTIMAX = 'Expectimax'