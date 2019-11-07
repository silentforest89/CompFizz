import numpy as np
import scipy.linalg as linalg

class matrix:

    def __init__(self,orbitals):
        self.num_orbitals = orbitals.num_orbitals
        self.matrix = np.zeros((self.num_orbitals,self.num_orbitals))

    def infinite_well(self):
        """
        TEMPORARY HACK SPECIFIC TO PROBLEM 3.2
        """       
        for i in range(self.num_orbitals):
            for j in range(self.num_orbitals):
                if (i+j) == 0 or (i+j)%2 == 0:
                    self.matrix[i,j] = 2/(i+j+5)-4/(i+j+3)+2/(i+j+1)
                else:
                    self.matrix[i,j] = 0

    def transform(self):    
        eigen_vals, eigen_vecs = linalg.eigh(self.matrix) 
        if not np.all((eigen_vals > 0)): # check if positive-definite
            print('\nERROR: the overlap matrix is not positive-definite.\n')
            exit()

        diagonal_matrix = np.diag(1/np.sqrt(eigen_vals))
        transmat = np.matmul(eigen_vecs,diagonal_matrix)
        self.transformation_matrix = np.matmul(eigen_vecs,diagonal_matrix)


