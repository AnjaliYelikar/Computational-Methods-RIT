
def Simpson_integration(f,a,b,n):
    """
    Function to calculate the integral of a function f from a to b
    with n intervals using the Simpson's rule
    """
    h = (b-a)/n
    I = 0. #f(a)+f(b)
    for i in range(0,n/2 -1):
        I += f(a+2*i*h) + 4.*f(a+(2*i+1)*h) + f(a+(2*i+2)*h)
    I = (h/3.)*I
    return I

