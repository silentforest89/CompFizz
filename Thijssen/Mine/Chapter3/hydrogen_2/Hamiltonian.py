import numpy as np

class gaussian:
    def __init__(self,basis,overlap):
        self.dim = overlap.dim
#        self.kinetic_mat = self.kinetic(basis)
#        self.potential_mat = self.potential(basis)
#        self.hamiltonian_mat = self.kinetic_mat+self.potential_mat
        self.hamiltonian_mat = self.kinetic(basis)+self.potential(basis)

    def kinetic(self,basis):
        tmp = np.zeros((self.dim,self.dim)).astype(complex)
        for i in range(self.dim):
            for j in range(i,self.dim):
                tmp[i,j] = (3*np.sqrt(np.pi)**3*
                        basis.alpha[i]*basis.alpha[j]/
                        np.sqrt((basis.alpha[i]+basis.alpha[j]))**5)
        return tmp+np.triu(tmp,k=1).conj().T

    def potential(self,basis):
        tmp = np.zeros((self.dim,self.dim)).astype(complex)
        for i in range(self.dim):
            for j in range(i,self.dim):
                tmp[i,j] = -2*np.pi/(basis.alpha[i]+basis.alpha[j])
        return tmp+np.triu(tmp,k=1).conj().T

 

        
    
