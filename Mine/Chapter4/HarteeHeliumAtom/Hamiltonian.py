import numpy as np
import scipy.linalg as linalg

class hamiltonian:

    def __init__(self,orbitals):
        self.num_orbitals = orbitals.num_orbitals

    def atomic(self,orbitals,nuclear_z):
        self.nuclear_z = nuclear_z
        self.matrix = np.zeros((self.num_orbitals,self.num_orbitals))
        self.ke_matrix = np.zeros((self.num_orbitals,self.num_orbitals))
        self.pe_matrix = np.zeros((self.num_orbitals,self.num_orbitals))
        for i in range(self.num_orbitals):
            for j in range(i,self.num_orbitals):
                self.ke_matrix[i,j] = (3*(np.pi**(3/2)*
                         orbitals.alphas[i]*
                         orbitals.alphas[j])/
                         (orbitals.alphas[i]+
                         orbitals.alphas[j])**(5/2))
                self.pe_matrix[i,j] = (-2*self.nuclear_z*np.pi/
                        (orbitals.alphas[i]+
                         orbitals.alphas[j]))
        self.ke_matrix = self.ke_matrix+np.triu(self.ke_matrix,k=1).T
        self.pe_matrix = self.pe_matrix+np.triu(self.pe_matrix,k=1).T
        self.matrix = self.ke_matrix+self.pe_matrix
        self.hpq_matrix = self.ke_matrix+self.pe_matrix
        self.compute_q_prqs(orbitals)
        self.matrix = self.matrix+self.q_matrix

    def compute_q_prqs(self,orbitals):
        self.q_matrix = np.zeros((self.num_orbitals,self.num_orbitals))
        self.q_prqs = np.zeros((self.num_orbitals,self.num_orbitals,
                                    self.num_orbitals,self.num_orbitals))
        i = 0
        for p in orbitals.alphas:
            j = 0
            for r in orbitals.alphas:
                k = 0
                for q in orbitals.alphas:
                    l = 0
                    for s in orbitals.alphas:
                        self.q_prqs[i,j,k,l] = (2*np.pi**(5/2)/
                                ((p+q)*(r+s)*np.sqrt(p+q+r+s)))
                        l = l+1
                    k = k+1
                j = j+1
            i = i+1
        for i in range(self.num_orbitals):
            for j in range(self.num_orbitals):
                self.q_matrix[i,j] = (orbitals.expansion_coefficients.conj().dot(
                        np.matmul(self.q_prqs[i,:,j,:],
                            orbitals.expansion_coefficients)))
    
    def diagonalize(self,transformation_matrix):
        self.change_basis(transformation_matrix)
        if not np.all(np.round(self.matrix.conj().T,6) ==
                np.round(self.matrix,6)):
            print('\nERROR: Hamiltonian matrix is not Hermitian\n')
            exit()
        self.eigen_vals, self.eigen_vecs = linalg.eigh(self.matrix)
        self.change_back(transformation_matrix)

    def change_basis(self,transformation_matrix):
        if (len(transformation_matrix[:,0]) != len(transformation_matrix[0,:])
            and len(tranformation_matrix[:,0]) != self.num_orbitals):
            print('\nERROR: trying to change Hamiltonian basis with wrong sized '
                    'matrix\n')
            exit()
        self.matrix = np.matmul(transformation_matrix.T,
                np.matmul(self.matrix,transformation_matrix))

    def change_back(self,transformation_matrix):
        self.eigen_vecs = np.matmul(transformation_matrix,self.eigen_vecs)
    
    def compute_ground_state_energy(self,orbitals):
        self.ground_state_energy = (2*orbitals.expansion_coefficients.conj().dot(
                np.matmul(self.hpq_matrix,orbitals.expansion_coefficients))+
                orbitals.expansion_coefficients.conj().dot(
                    np.matmul(self.q_matrix,orbitals.expansion_coefficients)))

    def canned_method(self,overlap_matrix):
        """
        I found out how to do this AFTER I finished the code. If I pass the 
        overlap matrix to the .eigh() method, it will solve it for me without
        having to do the transformations I put above!! Eitherway, I learned alot
        and just used this one to prove that my method predicts the same results
        as this one (to within 6 decimals).
        """
        self.eigen_vals, self.eigen_vecs = linalg.eigh(self.matrix,overlap_matrix)



