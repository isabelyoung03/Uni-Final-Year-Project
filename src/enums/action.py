from enum import Enum
"""
Enum for types of actions
"""
class Action(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    IDLE = 'IDLE'