import numpy as np
import scipy.linalg as linalg

class hamiltonian:

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
                    self.matrix[i,j] = -8*((1-i-j-2*i*j)/
                            ((i+j+3)*(i+j+1)*(i+j-1)))
                else:
                    self.matrix[i,j] = 0

    def change_basis(self,transformation_matrix):
        if (len(transformation_matrix[:,0]) != len(transformation_matrix[0,:])
            and len(tranformation_matrix[:,0]) != self.num_orbitals):
            print('\nERROR: trying to change Hamiltonian basis with wrong sized '
                    'matrix\n')
            exit()

        self.matrix = np.matmul(transformation_matrix.T,
                np.matmul(self.matrix,transformation_matrix))

    def diagonalize(self):
        if not np.all(np.round(self.matrix.T,3) == np.round(self.matrix,3)):
            print('\nWARNING: Hamiltonian matrix is not Hermitian\n')

        self.eigen_vals, self.eigen_vecs = linalg.eigh(self.matrix)

