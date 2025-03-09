import numpy as np

    
class Algebra:    
    fil = 3
    col = 3
    
    def __init__(self, fil=3, col=3, mat1 = [], mat2 = []):
        self.fil = fil
        self.col = col        
        self.mat1= mat1
        self.showMat(self.mat1)
        self.mat2= mat2
        self.showMat(self.mat2)
        
    def generate(self):
        mat = np.random.randint(0, 10, size=(self.fil, self.col))
        self.showMat(mat)
        return mat
    
    def showMat(mat= [],mje=""):
        print(mje+"\n","Matriz:\n",mat)        
        
    def Prod(self):
        prod = np.dot(self.mat1, self.mat2)
        self.showMat(prod,"Product")
        return prod
        
    def mulHadamard(self):
        prod = np.multiply(self.mat1, self.mat2)
        self.showMat(prod,"Product Hadamard")
        return prod
    
    def identity(self):
        mat = np.identity(self.col)
        self.showMat(mat,"Identity")
        return mat
            
Algebra.mat1 =  np.random.randint(0, 10, size=(3, 3))
Algebra.showMat(Algebra.mat1,"A")
Algebra.mat2 =  np.random.randint(0, 10, size=(3, 3))
Algebra.showMat(Algebra.mat2,"B")
Algebra.Prod(Algebra)
Algebra.mulHadamard(Algebra)
Algebra.identity(Algebra)

    