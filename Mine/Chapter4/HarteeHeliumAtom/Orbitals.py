import numpy as np

class orbitals:

    def __init__(self,num_orbitals,num_grid_points,r_limit):
        self.num_orbitals = num_orbitals
        self.num_grid_points = num_grid_points
        self.r_limit = r_limit
    
    def gaussian_functions(self,alphas,guess='random'):
        self.basis_type = 'gaussian'
        self.alphas = alphas
        self.orbitals = np.zeros((self.num_orbitals,self.num_grid_points))
        self.grid = np.linspace(0,self.r_limit,self.num_grid_points)
        for i in range(self.num_orbitals):
            self.orbitals[i,:] = np.exp(-self.alphas[i]*self.grid**2)
        if guess == 'random':
            self.expansion_coefficients = np.random.rand(self.num_orbitals)
        elif guess == 'equal':
            self.expansion_coefficients = np.ones(self.num_orbitals)
        else:
            print('\nERROR: option {} to guess initial expansion coefficients '
                  'is not recognized.\n'.format(guess))
            exit()

    def normalize(self,overlap_matrix):
        self.expansion_coefficients = (self.expansion_coefficients/
                (self.expansion_coefficients.conj().dot(np.matmul(overlap_matrix,
                    self.expansion_coefficients)))**(1/2))

    def update_expansion_coefficients(self,new_coefficients,overlap_matrix):
        self.expansion_coefficients = new_coefficients
        self.normalize(overlap_matrix)


