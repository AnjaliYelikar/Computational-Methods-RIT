
#Matrix addition

import numpy as np

A = [[1,2,3],[1,1,1]]
B = [[1,2,1],[1,1,2]]

C = np.zeros((len(A),len(A[0])))    # initializing the addition matrix with a null matrix

for i in A : 
    print(i)      # printing the matrix in a readable format
print

for i in B : 
    print(i) 

for i in range(len(A)):              # iterate through rows of A
    for j in range(len(A[0])):       # iterate through columns of A
        C[i][j] = A[i][j] + B[i][j]

print
for i in C:
    print(i)
