
class Matrix(object):

    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])
    
    def __add__(self,other):

        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        matrix_addition = []
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                addition = self.g[i][j] + other.g[i][j]
                new_row.append(addition)

            matrix_addition.append(new_row)

        return Matrix(matrix_addition)
