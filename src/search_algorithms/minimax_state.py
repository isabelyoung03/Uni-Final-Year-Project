"""
Object containing the location of player and ghost
"""
class State():
    def __init__(self, player_location, ghost_location):
        self.player_location = player_location
        self.ghost_location = ghost_location

    def get_player_location(self):
        return tuple(self.player_location)

    def get_ghost_location(self):
        return tuple(self.ghost_location)
    
    def __eq__(self, other):
        return isinstance(other, State) and self.get_player_location() == other.get_player_location() and self.get_ghost_location() == other.get_ghost_location()
    
    def __hash__(self):
        return hash((self.get_player_location(), self.get_ghost_location()))
    
    def __str__(self):
        return f"Player at {self.player_location}, Ghost at {self.ghost_location}" 