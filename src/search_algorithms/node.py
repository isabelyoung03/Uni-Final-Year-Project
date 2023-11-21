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
    
    """
    Returns location of node
    """
    def get_location(self):
        return (self.x, self.y)
    
    """
    Returns g
    """
    def get_g(self) -> int:
        return self.g
    
    """
    Returns h
    """
    def get_h(self) -> int:
        return self.h
    
    """
    Returns the parent node
    """
    def get_parent(self):
        return self.parent
    
    """
    Sets the parent node
    """
    def set_parent(self, parent):
        self.parent = parent
