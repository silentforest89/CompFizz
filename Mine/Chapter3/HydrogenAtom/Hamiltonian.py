import numpy as np
import scipy.linalg as linalg

class hamiltonian:

    def __init__(self,orbitals):
        self.num_orbitals = orbitals.num_orbitals
        self.matrix = np.zeros((self.num_orbitals,self.num_orbitals))
        self.ke_matrix = np.zeros((self.num_orbitals,self.num_orbitals))
        self.pe_matrix = np.zeros((self.num_orbitals,self.num_orbitals))

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

    def hydrogen_atom(self,orbitals):
        for i in range(self.num_orbitals):
            for j in range(i,self.num_orbitals):
                self.ke_matrix[i,j] = (3*(np.pi**(3/2)*
                         orbitals.alpha_coefficients[i]*
                         orbitals.alpha_coefficients[j])/
                         (orbitals.alpha_coefficients[i]+
                         orbitals.alpha_coefficients[j])**(5/2))
                self.pe_matrix[i,j] = (-2*np.pi/
                        (orbitals.alpha_coefficients[i]+
                         orbitals.alpha_coefficients[j]))

        self.ke_matrix = self.ke_matrix+np.triu(self.ke_matrix,k=1).T
        self.pe_matrix = self.pe_matrix+np.triu(self.pe_matrix,k=1).T
        self.matrix = self.ke_matrix+self.pe_matrix

    def change_basis(self,transformation_matrix):
        if (len(transformation_matrix[:,0]) != len(transformation_matrix[0,:])
            and len(tranformation_matrix[:,0]) != self.num_orbitals):
            print('\nERROR: trying to change Hamiltonian basis with wrong sized '
                    'matrix\n')
            exit()

        self.matrix = np.matmul(transformation_matrix.T,
                np.matmul(self.matrix,transformation_matrix))

    def diagonalize(self):
        if not np.all(np.round(self.matrix.T,6) == np.round(self.matrix,6)):
            print('\nWARNING: Hamiltonian matrix is not Hermitian\n')

        self.eigen_vals, self.eigen_vecs = linalg.eigh(self.matrix)

    def transform_vectors(self,transformation_matrix):
        self.eigen_vecs = np.matmul(transformation_matrix,self.eigen_vecs)
        
    def canned_method(self,overlap_matrix):
        """
        I found out how to do this AFTER I finished the code. If I pass the 
        overlap matrix to the .eigh() method, it will solve it for me without
        having to do the transformations I put above!! Eitherway, I learned alot
        and just used this one to prove that my method predicts the same results
        as this one (to within 6 decimals).
        """
        self.eigen_vals, self.eigen_vecs = linalg.eigh(self.matrix,overlap_matrix)



