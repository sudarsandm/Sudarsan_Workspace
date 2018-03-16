def swap_values_by_add_subtract(a, b):
    """
    This function uses addition and subtraction to swap values.
    """
    if a == b:
        print("pass numbers with different values")
        return 0
    elif (type(a) != int or type(b) != int):
        print("Enter integer values")
        return 0
    else:
        a = a + b
        b = a - b
        a = a - b
        
    return(a,b)

def swap_values_by_multiply_divide(a,b):
    """
    This function uses multiplication and division to swap values.
    """
    if a == b:
        print("pass numbers with different values")
        return 0
    elif (type(a) != int or type(b) != int):
        print("Enter integer values")
        return 0
    else:
        a = a * b
        b = a / b
        a = a / b
    return (a,b)
