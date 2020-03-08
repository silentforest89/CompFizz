import numpy as np

class gaussian:
    def __init__(self,basis):
        self.dim = basis.num_alpha
        self.overlap_mat = np.zeros((self.dim,self.dim)).astype(complex)
        for i in range(self.dim):
            for j in range(i,self.dim):
                self.overlap_mat[i,j] = np.sqrt(np.pi/(basis.alpha[i]+basis.alpha[j]))**3
        self.overlap_mat = self.overlap_mat+np.triu(self.overlap_mat,k=1).conj().T
