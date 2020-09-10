

def Num_derivative(f,c,h):
    """
    Function to calculate the derivative of a function f by using 
    the centered difference method at c with h being 
    the delta value about c
    """
    return (f(c + h) - f(c - h))/(2*h)    

