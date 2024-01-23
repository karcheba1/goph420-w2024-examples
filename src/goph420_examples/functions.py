def exp(x):
    """
    Compute values of the exponential function for real-valued input 

    Inputs
    ___________
    x : float
        the argument of the exponential
    Returns
    _______
    float 

    Raises 
    ______
    ValueError
        If x cannot be converted to a float. 
    """
    x = float(x)
    n = 0 
    fact_n=1
    result = 0.0
    tol = 1.0e-16
    eps_a = 1.0
    while eps_a > tol:
        term = (x ** n) / fact_n 
        result += term
        n += 1.0
        fact_n = n*fact_n
        eps_a = abs(term/result)
    return result

