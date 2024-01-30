def exp(x):
<<<<<<< HEAD
    """Compute values of the exponential function"
    for real -valued arguments.

    Imputs
    --------
    x : float
        The argument to the exponential function

    Returns
    --------
    float

    Raises
    -------
    ValueError
        If x cannot be converted to float
    """

    x = float (x)
    n = 0
    fact_n = 1
    result = 0.0
    tol = 1.0e-16 #Tolerance
    eps_a = 1.0
    while eps_a > tol:
        term = (x ** n) / fact_n
        result += term
        n += 1
        fact_n *= n 
=======
   """Compute values of the exponential function
    for real-valued arguments.

    Inputs
    ------
    x : float
        The argument to the exponential function.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If x cannot be converted to float.
    """
    x = float(x)
    n = 0
    fact_n = 1
    result = 0.0
    tol = 1.0e-16
    eps_a = 1.0
    while eps_a > tol:
       term = (x ** n) / fact_n
        result += term
        n += 1
        fact_n *= n
>>>>>>> ec4bf4f23c7c720e3fae27086789d4eb5a16320b
        eps_a = abs(term / result)
    return result
