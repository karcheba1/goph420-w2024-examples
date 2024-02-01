import numpy as np

def shape (s, order=1):
    """Compute Lagrange interpolating polynomial 
    shape functions of various order.

    Inputs
    ------
    s : float
        The local coordinate on the interval [0, 1]
    order : int, optional, default=1
        The order of interpolation.
        Valid values are [1].

    Returns
    -------
    numpy.ndarray, shape=(1, order+1)
        The array of shape function values

    Raises
    ------
    ValueError
        If s cannot be converted to float.
        If order is not in [1].
    """
    s = float(s)
    if order not in [1]:
        raise ValueError(f"order {order} is not valid")

    return np.array([[(1.0-s), s]])