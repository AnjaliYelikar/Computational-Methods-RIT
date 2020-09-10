
# Transpose of a matrix

import numpy as np

A = [[1,2,3],[3,4,5]] 

for i in A: 
    print(i) 

print    
A_T =  np.zeros((len(A[0]),len(A)))     # initializing the transpose a null matrix
for i in A_T:                               
    print(i) 
    
for i in range(len(A)):
    for j in range(len(A[0])):
        A_T[j][i] = A[i][j]
        
print
for i in A_T:
    print(i)
