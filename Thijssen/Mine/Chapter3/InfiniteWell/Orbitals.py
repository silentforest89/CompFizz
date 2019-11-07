import numpy as np

class orbitals:

    def __init__(self,num_orbitals):
        self.num_orbitals = num_orbitals

    def infinite_well(self,num_grid_points):
        """
        TEMPORARY HACK SPECIFIC TO PROBLEM 3.2
        """
        self.num_grid_points = num_grid_points
        self.orbitals = np.zeros((self.num_orbitals,self.num_grid_points))
        self.grid = np.linspace(-1,1,self.num_grid_points)

        for i in range(self.num_orbitals):
            self.orbitals[i,:] = self.grid**i*(self.grid-1)*(self.grid+1)


