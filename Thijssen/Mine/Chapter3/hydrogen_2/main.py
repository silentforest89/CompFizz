import Basis, Overlap, Hamiltonian, Diag

basis = Basis.gaussian(alpha=[13.00773,1.962079,0.444529,0.1219492])
overlap = Overlap.gaussian(basis)
hamiltonian = Hamiltonian.gaussian(basis,overlap)
energy, eigenvec = Diag.generalized_eigenval(overlap,hamiltonian)

print('\t{:.8f}\tRy'.format(energy[0]))
