import numpy as np
import Overlap
import Orbitals
import Hamiltonian

num_orbitals = 16

# create the basis orbitals
orbitals = Orbitals.orbitals(num_orbitals)

# create overlap matrix
overlap_matrix = Overlap.matrix(orbitals)
overlap_matrix.infinite_well()
# find transformation matrix to convert to simple eigenvalue problem
overlap_matrix.transform()

# create hamiltonian matrix
hamiltonian = Hamiltonian.hamiltonian(orbitals)
hamiltonian.infinite_well()

# change basis of hamiltonian to convert to simple eigenvalue problem
hamiltonian.change_basis(overlap_matrix.transformation_matrix)

# solve
hamiltonian.diagonalize()

np.savetxt('eigenvalues.csv',hamiltonian.eigen_vals[:5],fmt='%.4f')

