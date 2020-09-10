
def Trapezoidal_integration(f,a,b,n):
    """
    Function to calculate the integral of a function f from a to b
    with n intervals using the Trapezoidal rule
    """
    h = (b-a)/n
    I = 0.5*(f(a) + f(b))                # initializing I as 0.5*(f(a)+f(b)) as I at every 
                                         # other point except the edges is just h*f(x_i)
    for i in range(1, n):
        x = a + i*h                      # the function is evaluated at every point in between 
                                         # a and b spaced by width w
        I += f(x)
    I = h*I
    return I

