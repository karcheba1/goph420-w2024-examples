import numpy as np
import numpy.typing as npt


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

    Attributes
    ----------
    index
    x
    temp

    Parameters
    ----------
    index : int
        The global index of the node.
    x : float
        The position of the node.
    temp: float, optional, default=0.0
        The temperature at the node.

    Raises
    ------
    TypeError
        If index is not an int.
    ValueError
        If index is < 0.
        If x cannot be converted to float.
    """
    _index: int
    _x: float
    _temp: float

    def __init__(
        self,
        index: int,
        x: float,
        temp: float = 0.0,
    ):
        if not isinstance(index, int):
            raise TypeError(f"type of index {type(index)} is not int")
        if index < 0:
            raise ValueError(f"value of index {index} is negative")
        self._index = index

        x = float(x)
        self._x = x

        self.temp = temp

    @property
    def index(self) -> int:
        """The global index of the node.

        Returns
        -------
        int
        """
        return self._index

    @property
    def x(self) -> float:
        """The position of the node.

        Returns
        -------
        float
        """
        return self._x

    @property
    def temp(self):
        """The temperature of the node.

        Parameters
        ----------
        float

        Returns
        -------
        float

        Raises
        ------
        ValueError
            If the value provided cannot be converted to float.
        """
        return self._temp

    @temp.setter
    def temp(self, temp: float):
        temp = float(temp)
        self._temp = temp


class Element:
    """Class for grouping Nodes
    and computing element matrices and vectors.

    Attributes
    ----------
    order
    num_nodes
    nodes
    jacobian
    conduction_matrix
    storage_matrix
    flux_vector

    Parameters
    ----------
    nodes : tuple[Node]
        The nodes contained in the element.
    order : int
        The order of interpolation.

    Raises
    ------
    TypeError
        If objects in nodes are not of class Node.
        If order is not an int.
    ValueError
        If order < 0.
        If len(nodes) is not consistent with order.
    """
    _flux_vector: npt.NDArray[np.floating]

    def __init__(self, nodes: tuple[Node], order: int):
        if not isinstance(order, int):
            raise TypeError(f"order is {type(order)}, must be int")
        if order not in [1]:
            raise ValueError(f"order value {order} invalid")
        if len(nodes) != order + 1:
            raise ValueError(
                f"provided {len(nodes)} nodes, "
                + f"should be {order + 1}"
            )
        # TODO: check that all objects in nodes
        # are of type Node
        self._order = order
        self._nodes = tuple(nodes)

    @property
    def order(self) -> int:
        return self._order


    @property
    def num_nodes(self) -> int:
        self._num_nodes = len(self.nodes)
        return(self._num_nodes)

    @property
    def nodes(self) -> tuple[Node]:
        return self._nodes

    @property
    def jacobian(self) -> float:
        self._jacobian = self.nodes[1] - self.nodes[0]
        return self._jacobian

    @property
    def conduction_matrix(self) -> npt.NDArray[np.floating]:
        pass

    @property
    def storage_matrix(self) -> npt.NDArray[np.floating]:
        return ((rho*c*self.jacobian/6)*np.array([[2, 1], [1, 2]]))

    @property
    def flux_vector(self) -> npt.NDArray[np.floating]:
        flux_vector = 0.5 * np.array([[1], [1]])
        return self._flux_vector

    @property
    def heat_transfer_coeff(self):
        pass

    @property
    def t_infinity(self):
        pass

    @property
    def perimeter_area(self):
        pass
