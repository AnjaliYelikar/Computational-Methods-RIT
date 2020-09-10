
# Matrix multiplication

import numpy as np

A = [[1,2,3],[1,1,1],[4,3,1]]
B = [[1,2,1],[1,1,2],[3,5,7]]

C = np.zeros((len(A),len(A[0])))    # initializing the multiplication matrix with a null matrix

for i in A : 
    print(i) 
print

for i in B : 
    print(i)
    

for i in range(len(A)):                 # iterate through rows of X
    for j in range(len(B[0])):           # iterate through columns of Y
        for k in range(len(B)):          # iterate through rows of Y
            C[i][j] += A[i][k] * B[k][j]

print
for i in C:
    print(i)
