from enum import Enum
import config
"""
Enum used to define the size of a maze, used as the result from buttons on the menu screen
"""
class MazeSize(Enum):
    SMALL = config.SMALL_MAZE_MAP
    MEDIUM = config.MEDIUM_MAZE_MAP
    LARGE = config.LARGE_MAZE_MAP

    """
    Return the width of the screen for this size maze
    """
    def get_width(self):
        if self == MazeSize.SMALL:
            return config.SMALL_MAZE_SCREEN_WIDTH
        elif self == MazeSize.MEDIUM:
            return config.MEDIUM_MAZE_SCREEN_WIDTH
        elif self == MazeSize.LARGE:
            return config.LARGE_MAZE_SCREEN_WIDTH
        
    """
    Return the height of the screen for this size maze
    """
    def get_height(self):
        if self == MazeSize.SMALL:
            return config.SMALL_MAZE_SCREEN_HEIGHT
        elif self == MazeSize.MEDIUM:
            return config.MEDIUM_MAZE_SCREEN_HEIGHT
        elif self == MazeSize.LARGE:
            return config.LARGE_MAZE_SCREEN_HEIGHT
        
    """
    Return string representation of enum
    """
    def to_string(self):
        if self == MazeSize.SMALL:
            return "Small"
        elif self == MazeSize.MEDIUM:
            return "Medium"
        elif self == MazeSize.LARGE:
            return "Large"
