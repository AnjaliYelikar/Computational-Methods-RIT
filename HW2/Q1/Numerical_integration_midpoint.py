

def Midpoint_integration(f,a,b,n):
    """
    Function to calculate the integral of a function f from a to b
    with n intervals using the mid-point rule
    """
    h = (b-a)/n                      # h is width of the rectangle
    I = 0.                            #initializing the value of variable which will be the integral
    for i in range(0,n):
        x = (2*a + (2*i+1)*h)/2.       # midpoints are like (2a+h)/2, (2a+3h)/2, (2a+5h)/2, etc
        I += f(x)
    I = h*I
    return I


