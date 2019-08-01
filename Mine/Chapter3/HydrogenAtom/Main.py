import numpy as np
import matplotlib.pyplot as plt
import Overlap
import Orbitals
import Hamiltonian

num_orbitals = 4
num_grid_points = 1000

### create the basis orbitals
orbitals = Orbitals.orbitals(num_orbitals)
orbitals.hydrogen_atom(num_grid_points)

### create overlap matrix
overlap_matrix = Overlap.matrix(orbitals)
overlap_matrix.hydrogen_atom(orbitals)

### find transformation matrix to convert to simple eigenvalue problem
overlap_matrix.transform()

### create hamiltonian matrix
hamiltonian = Hamiltonian.hamiltonian(orbitals)
hamiltonian.hydrogen_atom(orbitals)

### see the docstring for hamiltonian.canned_method before using!
#hamiltonian.canned_method(overlap_matrix.matrix)
#np.savetxt('eigvals1.csv',hamiltonian.eigen_vals,fmt='%.6f')
#np.savetxt('eigvecs1.csv',hamiltonian.eigen_vecs,fmt='%.6f')

### change basis of hamiltonian to convert to simple eigenvalue problem
hamiltonian.change_basis(overlap_matrix.transformation_matrix)

### solve
hamiltonian.diagonalize()
hamiltonian.transform_vectors(overlap_matrix.transformation_matrix)

np.savetxt('eigenvalues.csv',hamiltonian.eigen_vals,fmt='%.6f')
np.savetxt('eigenvectors.csv',hamiltonian.eigen_vecs,fmt='%.6f')


####################################################################

# arbitrary phase had them all negative (real)
hamiltonian.eigen_vecs[:,0] = -1*hamiltonian.eigen_vecs[:,0]

# in Bohr units
exact = 1/np.sqrt(np.pi)*np.exp(-orbitals.grid)

### plot wavefunction
wave_function = np.zeros(num_grid_points)
for i in range(orbitals.num_orbitals):
    wave_function = (wave_function+
            orbitals.orbitals[i,:]*hamiltonian.eigen_vecs[i,0])

plt.plot(orbitals.grid,wave_function,'k',lw=2,zorder=10,label='4 Gaussians')
plt.plot(orbitals.grid,exact,'r--',lw=2,label='Analytical')
plt.legend()
plt.xlabel('r (Bohr)')
plt.ylabel('Amplitude')
plt.xlim(0,2)
plt.ylim(0.075,0.6)
plt.show()

