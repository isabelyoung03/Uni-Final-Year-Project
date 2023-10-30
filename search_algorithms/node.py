class Node:
    """
    Node class used in A* search
    """
    def __init__(self, x, y, g, h, parent):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.parent = parent
    
    def get_location(self):
        return (self.x, self.y)
    
    def get_g(self):
        return self.g
    
    def get_h(self):
        return self.h
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent
