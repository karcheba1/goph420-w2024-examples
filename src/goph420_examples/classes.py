import numpy as np
import numpy.typing as npt

from .interpolation import (
    shape,
)


class Point:
    _x: float

    def __init__(self, x: float):
        self.x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: float):
        value = float(value)
        self._x = value

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
    def temp(self, value: float):
        value = float(value)
        self._temp = value


class IntegrationPoint:
    """Store material property information
    and interpolated values of solutions variables
    for integrating element matrices and vectors.

    Attributes
    ----------
    local_coord
    weight
    x
    temp
    density
    thrm_cond
    spec_heat_cap
    heat_trans_coef
    temp_inf
    perimeter
    area

    Parameters
    ----------
    local_coord : float
        The local coordinate for Gauss integration within
        the parent element.
    weight : float
        The weight for Gauss integration within the parent element.
    x : float
        The position of the integration point.
    temp: float, optional, default=0.0
        The temperature at the integration point.
    density: float, optional, default=0.0
        The density at the integration point.
    thrm_cond: float, optional, default=0.0
        The thermal conductivity at the integration point.
    spec_heat_cap: float, optional, default=0.0
        The specific heat capacity at the integration point.
    heat_trans_coef: float, optional, default=0.0
        The heat transfer coefficient
        (to outside ambient fluid)
        at the integration point.
    temp_inf : float, optional, default=0.0
        Ambient temperature around the element.
    perimeter : float, optional, default=0.0
        Perimeter of the element.
    area : float, optional, default=0.0
        Area of the element.

    Raises
    ------
    ValueError
        If local_coord cannot be converted to float.
        If weight cannot be converted to float.
        If weight < 0.
        If x cannot be converted to float.
        If temp cannot be converted to float.
        If density cannot be converted to float.
        If density < 0.
        If thrm_cond cannot be converted to float.
        If thrm_cond < 0.
        If spec_heat_cap cannot be converted to float.
        If spec_heat_cap < 0.
        If heat_trans_coef cannot be converted to float.
        If heat_trans_coef < 0.
        If temp_inf cannot be converted to float.
        If perimeter cannot be converted to float.
        If perimeter < 0.
        If area cannot be converted to float.
        If area < 0.
    """
    _local_coord: float
    _weight: float
    _x: float
    _temp: float = 0.0
    _density: float = 0.0
    _thrm_cond: float = 0.0
    _spec_heat_cap: float = 0.0
    _heat_trans_coef: float = 0.0
    _temp_inf: float = 0.0
    _perimeter: float = 0.0
    _area: float = 0.0

    def __init__(
        self,
        local_coord: float,
        weight: float,
        x: float,
        temp: float = 0.0,
        density: float = 0.0,
        thrm_cond: float = 0.0,
        spec_heat_cap: float = 0.0,
        heat_trans_coef: float = 0.0,
        temp_inf: float = 0.0,
        perimeter: float = 0.0,
        area: float = 0.0,
    ):
        # data validation on immutable properties
        x = float(x)
        local_coord = float(local_coord)
        weight = float(weight)
        if weight < 0.0:
            raise ValueError("weight cannot be negative")

        # assign immutable properties to private attributes
        self._x = x
        self._local_coord = local_coord
        self._weight = weight

        # use setters to assign public properties
        self.temp = temp
        self.density = density
        self.thrm_cond = thrm_cond
        self.spec_heat_cap = spec_heat_cap
        self.heat_trans_coef = heat_trans_coef
        self.temp_inf = temp_inf
        self.perimeter = perimeter
        self.area = area

    @property
    def local_coord(self) -> float:
        """The local coordinate of the integration point
        within the parent element.

        Returns
        -------
        float
        """
        return self._local_coord

    @property
    def weight(self) -> float:
        """The integration weight of the integration point
        within the parent element.

        Returns
        -------
        float
        """
        return self._weight

    @property
    def x(self) -> float:
        """The position of the integration point.

        Returns
        -------
        float
        """
        return self._x

    @property
    def temp(self) -> float:
        """The temperature of the integration point.

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
    def temp(self, value: float) -> None:
        value = float(value)
        self._temp = value

    @property
    def perimeter(self) -> float:
        """The perimeter of the element.

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
            If the value provided is negative.
        """
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value: float) -> None:
        value = float(value)
        if value < 0.0:
            raise ValueError(f"value {value} for perimeter cannot be negative")
        self._perimeter = value

    @property
    def area(self):
        """The area of the element.

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
            If the value provided is negative.
        """
        return self._area

    @area.setter
    def area(self, value: float) -> None:
        value = float(value)
        if value < 0.0:
            raise ValueError(f"value {value} for area cannot be negative")
        self._area = value

    @property
    def temp_inf(self) -> float:
        """The ambient temperature of the integration point.

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
        return self._temp_inf

    @temp_inf.setter
    def temp_inf(self, value: float) -> None:
        value = float(value)
        self._temp_inf = value

    @property
    def density(self) -> float:
        """The density of the integration point.

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
            If the value provided is negative.
        """
        return self._density

    @density.setter
    def density(self, value: float) -> None:
        value = float(value)
        if value < 0.0:
            raise ValueError("density cannot be negative")
        self._density = value

    @property
    def thrm_cond(self) -> float:
        """The thermal conductivity of the integration point.

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
            If the value provided is negative.
        """
        return self._thrm_cond

    @thrm_cond.setter
    def thrm_cond(self, value: float) -> None:
        value = float(value)
        if value < 0.0:
            raise ValueError("thermal conductivity cannot be negative")
        self._thrm_cond = value

    @property
    def spec_heat_cap(self):
        """The specific heat capacity of the integration point.

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
            If the value provided is negative.
        """
        return self._spec_heat_cap

    @spec_heat_cap.setter
    def spec_heat_cap(self, value: float) -> None:
        value = float(value)
        if value < 0.0:
            raise ValueError("specific heat capacity cannot be negative")
        self._spec_heat_cap = value

    @property
    def heat_trans_coef(self):
        """The heat transfer coefficient of the integration point.

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
        return self._heat_trans_coef

    @heat_trans_coef.setter
    def heat_trans_coef(self, value: float) -> None:
        value = float(value)
        if value < 0:
            raise ValueError("heat transfer coefficient cannot be negative")
        self._heat_trans_coef = value


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
    _order: int
    _nodes: tuple[Node, ...]
    _int_pts: tuple[IntegrationPoint, ...]

    _int_pt_coords_0 = (
        0.5,
    )
    _int_pt_weights_0 = (
        1.0,
    )

    def __init__(self, nodes: tuple[Node], order: int):
        # validate input arguments
        if not isinstance(order, int):
            raise TypeError(f"order is {type(order)}, must be int")
        if order not in [1]:
            raise ValueError(f"order value {order} invalid")
        if len(nodes) != order + 1:
            raise ValueError(
                f"provided {len(nodes)} nodes, "
                + f"should be {order + 1}"
            )
        for nd in nodes:
            if not isinstance(nd, Node):
                raise TypeError("objects in nodes must be of type Node")

        self._order = order
        self._nodes = tuple(nodes)

        # TODO: determine number of int pts
        # based on order
        int_pt_coords = Element._int_pt_coords_0
        int_pt_weights = Element._int_pt_weights_0

        # create integration points
        xe = np.array([nd.x for nd in self.nodes])
        int_pts = []
        for s, w in zip(int_pt_coords, int_pt_weights):
            N = shape(s, self.order)
            xip = (N @ xe)[0]
            int_pts.append(IntegrationPoint(local_coord=s, weight=w, x=xip))
        self._int_pts = tuple(int_pts)

    @property
    def order(self) -> int:
        return self._order

    @property
    def num_nodes(self) -> int:
        return len(self.nodes)

    @property
    def nodes(self) -> tuple[Node, ...]:
        return self._nodes

    @property
    def num_int_pts(self) -> int:
        return len(self.int_pts)

    @property
    def int_pts(self) -> tuple[IntegrationPoint, ...]:
        return self._int_pts

    @property
    def jacobian(self) -> float:
        return self.nodes[-1].x - self.nodes[0].x

    @property
    def conduction_matrix(self) -> npt.NDArray[np.floating]:
        h = self.int_pts[0].heat_trans_coef
        lam = self.int_pts[0].thrm_cond
        P = self.int_pts[0].perimeter
        A = self.int_pts[0].area
        jac = self.jacobian
        cond_mat = (h * (P / A) * jac / 6.0) * np.array(
            [[2.0, 1.0], [1.0, 2.0]]
        )
        cond_mat += (lam / jac) * np.array([[1.0, -1.0], [-1.0, 1.0]])
        return cond_mat

    @property
    def storage_matrix(self) -> npt.NDArray[np.floating]:
        rho = self.int_pts[0].density
        c = self.int_pts[0].spec_heat_cap
        jac = self.jacobian
        return (rho * c * jac / 6.0) * np.array([[2.0, 1.0], [1.0, 2.0]])

    @property
    def flux_vector(self) -> npt.NDArray[np.floating]:
        h = self.int_pts[0].heat_trans_coef
        P = self.int_pts[0].perimeter
        A = self.int_pts[0].area
        T_inf = self.int_pts[0].temp_inf
        jac = self.jacobian
        return h * (P/A) * jac * T_inf * np.array([0.5, 0.5])
