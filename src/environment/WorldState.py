"""
Object containing the current state of the world
"""
class WorldState():
    def __init__(self, maze, ghosts, cupcakes, player_location):
        self.maze = maze
        self.ghosts = ghosts
        self.cupcakes = cupcakes
        self.player_location = player_location

    def get_maze(self):
        return self.maze
    
    def get_ghosts(self):
        return self.ghosts
    
    def get_cupcakes(self):
        return self.cupcakes
    
    def get_player_location(self):
        return self.player_location