
class Matrix:
    def __init__(self, matrixA, matrixB):
        self.A = matrixA
        self.B = matrixB
        
    def __addition__(self,other):
        C = np.zeros((len(A),len(A[0]))
                     
        for i in range(len(A)):    #rows
            for j in range(len(A[0])): #columns
                C[i][j] = A[i][j] + B[i][j]
                  
	def __multiplication(self,other):
		C = np.zeros((len(A),len(A[0]))) 

		for i in range(len(A)):                 # iterate through rows of X
		     for j in range(len(B[0])):           # iterate through columns of Y
		         for k in range(len(B)):          # iterate through rows of Y
        		    C[i][j] += A[i][k] * B[k][j]


	def __transpose(self):
		A_T =  np.zeros((len(A[0]),len(A))) 
		
		for i in range(len(A)):
			 for j in range(len(A[0])):
     			A_T[j][i] = A[i][j]

	
	def __trace(self):
		trace = 0.
		for i in range(len(A)):
			trace += A[i][i]

#A = [[1,2,3],[1,1,1]]
#B = [[1,2,1],[1,1,2]]
                     
#f = Matrix(A,B)
#print(f.addition())
