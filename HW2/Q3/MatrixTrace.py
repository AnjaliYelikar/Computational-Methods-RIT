
# Trace of a matrix

import numpy as np

A = np.array([[1,2,1],[1,1,2],[3,5,7]])

trace = 0.

for i in range(len(A)):
    trace += A[i][i]
    
print(trace)
