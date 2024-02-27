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

    def __init__(self, index: int):
        self.index = index

    @property
    def index(self):
        return self._index
    
    def get_index(self):
        return self._index

        pass





class temp:
    _T: float

    def __init__(self, T=0:float): 
        self.T = T  

    @property 
    def T(self):
        return self._T

    @T.setter 
    def T(self, T: float):
        T = float(T)
        self._T = T 
