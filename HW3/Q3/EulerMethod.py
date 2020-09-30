import numpy as np
import matplotlib.pyplot as plt


def odeEuler(f,y0,t):
        #ODE solver by Euler's method where f is y'=f(t,y), y0 is the initial value
        #at t0, t is the list of times we need to solve for
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1] - t[n])
    return y

t = np.linspace(-2,1,21)
y0 = np.exp(-2.)
f = lambda y,t: y
y = odeEuler(f,y0,t)
y_true = np.exp(t)
plt.plot(t,y,'r.-',t,y_true,'b-')
plt.legend(['Euler','True'])
plt.axis([-2,1,0,5])
plt.show()
