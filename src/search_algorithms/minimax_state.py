"""
Object containing the location of player and ghost
"""
class State():
    def __init__(self, player_location, ghost_location):
        self.player_location = player_location
        self.ghost_location = ghost_location

    def get_player_location(self):
        return self.player_location
    
    def get_ghost_location(self):
        return self.ghost_location