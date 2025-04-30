#2. Write a program that implements a Matrix class and performs addition,
#multiplication and transpose operations on 3x3 matrices.
class Matrix:
    def __init__(self):
        self.m=[[0,0,0],[0,0,0],[0,0,0]]
    def printMatrix(self):
        print(self.m[0][0],self.m[0][1],self.m[0][2],'\n',self.m[1][0],self.m[1][1],self.m[1][2],'\n',self.m[2][0],self.m[2][1],self.m[2][2])
    def getMatrix(self):
        for i in range(3):
            for j in range(3):
                self.m[i][j] = int(input(f'Enter the [{i}][{j}]th element] :'))
    def __add__(self,M2):
        print('Matrix Addition')
        M = Matrix()
        for i in range(3):
            for j in range(3):
                M.m[i][j]=self.m[i][j] + M2.m[i][j]
        return M
    def __mul__(self,M2):
        print('Matrix Multiplication')
        M = Matrix()
        for i in range(3):
            for j in range(3):
                M.m[i][j]=self.m[0][j]*M2.m[i][0] + self.m[1][j]*M2.m[i][1] + self.m[2][j]*M2.m[i][2]
        return M
    def transpose(self):
        print('Matrix Transpose')
        M = Matrix()
        for i in range(3):
            for j in range(3):
                M.m[i][j] = self.m[j][i]
        return M
        
M1 = Matrix()
M2 = Matrix()
M1.getMatrix()
M1.printMatrix()
M2.getMatrix()
M2.printMatrix()
(M1 + M2).printMatrix()
(M1*M2).printMatrix()
M1.transpose().printMatrix()


