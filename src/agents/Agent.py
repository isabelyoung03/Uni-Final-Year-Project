from abc import abstractmethod
from src.environment.WorldState import WorldState
from src.enums.action import Action
class Agent():
    def __init__(self, x, y):
        self.x = x #x coord for player in maze map
        self.y = y #y coord for player in maze map

    """
    Returns the location of the agent
    """
    def get_location(self):
        return (self.x,self.y)

    @abstractmethod
    def move_left(self):
        pass

    @abstractmethod
    def move_right(self):
        pass

    @abstractmethod
    def move_down(self):
        pass

    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def decide(self):
        pass

    """
    Execute specified action
    """
    def execute(self, action) -> None:
        if action == Action.DOWN:
            self.move_down()
        elif action == Action.LEFT:
            self.move_left()
        elif action == Action.RIGHT:
            self.move_right()
        elif action == Action.UP:
            self.move_up()

    """
    Update internal representation for the maze map, locations of the ghosts and cupcakes not yet eaten
    """
    def revise(self, world_state: WorldState) -> None:
        self.maze = world_state.get_maze()
        self.ghosts = world_state.get_ghosts()
        self.cupcakes = world_state.get_cupcakes()
        self.player_location = world_state.get_player_location()

    """
    Check is a move to the given location is valid (aka not a wall or a ghost)
    Avoiding a square with a ghost in gives the agent the property of rationality
    """
    def check_valid_move(self, x, y) -> bool:
        if not self.maze.check_valid_location(x,y):
            return False
        if self.ghost_in_location(x,y):
             return False
        return True

    """
    Get the 4 surrounding cells to a specified cells and return as a list
    """
    def get_surrounding_cells(self, x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return [(x + dx, y + dy) for dx, dy in directions]