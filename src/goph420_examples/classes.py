import numpy as np


class Point:
    _x: float

    def __init__(self, x: float):
        self.x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: float):
        x = float(x)
        self._x = x

    def length(self):
        return np.sqrt(self.x ** 2)


class Node:
    """Store solution variable information.

    Attributes:
    index : int
        The global index of the node.
    x : float
        The position of the node.
    temp: float
        The temperature at the node.

    """
    _x: float

    def __init__(self, x: float):
        self.x = x 

    @property
    def x(self):
        x = float(x)
        return self._x

    def length(self):
        return np.abs(self.x)