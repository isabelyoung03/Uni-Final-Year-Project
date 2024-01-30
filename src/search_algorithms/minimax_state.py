"""
Object containing the location of player and ghost
"""
class State():
    def __init__(self, player_location, ghost_locations: list):
        self.player_location = player_location
        self.ghost_locations = ghost_locations

    def get_player_location(self):
        return tuple(self.player_location)

    def get_ghost_locations(self):
        return self.ghost_locations
    
    def __eq__(self, other):
        return isinstance(other, State) and self.get_player_location() == other.get_player_location() and self.get_ghost_locations() == other.get_ghost_locations()
    
    def __hash__(self):
        return hash((self.get_player_location(), self.get_ghost_locations()))
    
    def __str__(self):
        return f"Player at {self.player_location}, Ghosts at {self.ghost_locations}" 