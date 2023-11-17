class Node:
    """
    Node class used in A* search
    """
    def __init__(self, x:int, y:int, g:int, h:int, parent):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.parent = parent
    
    """
    Calculates f by summing g and h
    """
    def get_f(self) -> int:
        return self.g + self.h
    
    def get_location(self):
        return (self.x, self.y)
    
    def get_g(self) -> int:
        return self.g
    
    def get_h(self) -> int:
        return self.h
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent
