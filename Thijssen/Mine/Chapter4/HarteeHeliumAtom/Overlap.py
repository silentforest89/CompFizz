import numpy as np
import scipy.linalg as linalg

class matrix:
    
    def __init__(self,orbitals):
        self.num_orbitals = orbitals.num_orbitals
        self.matrix = np.zeros((self.num_orbitals,self.num_orbitals))
        if orbitals.basis_type == 'gaussian':
            self.gaussian_overlap(orbitals)
        orbitals.normalize(self.matrix)

    def gaussian_overlap(self,orbitals):
        for i in range(self.num_orbitals):
            for j in range(i,self.num_orbitals):
                self.matrix[i,j] = (np.pi/
                        (orbitals.alphas[i]+
                         orbitals.alphas[j]))**(3/2)
        self.matrix = self.matrix+np.triu(self.matrix,k=1).conj().T

    def transform(self):    
        eigen_vals, eigen_vecs = linalg.eigh(self.matrix) 
        if not np.all((eigen_vals > 0)): # check if positive-definite
            print('\nERROR: the overlap matrix is not positive-definite.\n')
            exit()
        diagonal_matrix = np.diag(1/np.sqrt(eigen_vals))
        transmat = np.matmul(eigen_vecs,diagonal_matrix)
        self.transformation_matrix = np.matmul(eigen_vecs,diagonal_matrix)



