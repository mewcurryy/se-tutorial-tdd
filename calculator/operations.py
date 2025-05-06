def add(a : float, b : float) -> float:
    """Return the sum of two number."""
    return a + b


def subtract(a : float, b : float) -> float:
    """Return the subtraction of two number."""
    return a - b


def multiply(a : float, b : float) -> float:
    """Return the multiple result of two number."""
    return a * b


def divide(a : float, b : float) -> float:
    """Return the division result of two number."""
    if b == 0:
        print("Cannot divide by zero.")
        pass
    else:  
        return a / b
    
    


# def add(a : float, b : float) -> float:
#     """Return the sum of two number."""
#     # return a + b
#     pass