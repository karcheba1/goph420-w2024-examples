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
    _temp: float
    _x: float

    def __init__(self, x: float, temp: float = 0, index: int):
        self.index = index
        self.temp = temp
        self.x = x

    @property
    def x(self):
        return self._x

    @property
    def index(self):
        return self._index

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp: float):
        temp = float(temp)
        self._temp = temp
