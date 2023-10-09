from enum import Enum
import config
"""
Enum used to define the size of a maze, used as the result from buttons on the menu screen
"""
class MazeSize(Enum):
    SMALL = config.SMALL_MAZE_MAP
    MEDIUM = config.MEDIUM_MAZE_MAP
    LARGE = config.LARGE_MAZE_MAP