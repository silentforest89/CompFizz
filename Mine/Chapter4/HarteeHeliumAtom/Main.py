import numpy as np
import matplotlib.pyplot as plt
import Parser
import Overlap
import Orbitals
import Hamiltonian

params = Parser.parse('INPUTFILE') # read input file

# calculate overlap and hamiltonian matrix elements
orbitals = Orbitals.orbitals(params.num_orbitals,params.num_grid_points,params.r_limit)
orbitals.gaussian_functions(params.alphas,guess=params.scf_guess)

overlap_matrix = Overlap.matrix(orbitals)
overlap_matrix.transform()

hamiltonian = Hamiltonian.hamiltonian(orbitals)
hamiltonian.atomic(orbitals,params.nuclear_z)

# diagonalize hamiltonian for starting point of SCF iteration
last_energy_value = 0 
hamiltonian.diagonalize(overlap_matrix.transformation_matrix)
hamiltonian.compute_ground_state_energy(orbitals)

# iterate until SCF covergence threshold or max number of iterations is met
print('\n####### SCF: ITERATING TO SELF CONSISTENCY ########\n')
for num_iter in range(1,params.max_scf+1):    
    # use calculate eigenvector as next guess in Hartree potential
    new_coefficients = hamiltonian.eigen_vecs[:,np.argmin(hamiltonian.eigen_vals)]
    scf_convergence = abs(hamiltonian.ground_state_energy-last_energy_value)
    last_energy_value = hamiltonian.ground_state_energy

    print('\tStep {} convergence = {:.10f} Ry'.format(num_iter,scf_convergence))
    if num_iter == params.max_scf:
        print('\n*** WARNING: SCF failed to converge ***')
        print('\nSCF did ***NOT*** converge in {} iterations\n'
              'Final SCF accuracy = {:.10f} Ry\n'.format(num_iter,scf_convergence))
        print('\n\n\tComputed Ground State Energy = {:.8f} Ry\n\n\n'
                .format(hamiltonian.ground_state_energy))
        break
    elif num_iter != 1 and abs(scf_convergence) < params.scf_tol:
        print('\nSCF convergence achieved in {} iterations\n'
              'Final SCF accuracy = {:.10f} Ry\n'.format(num_iter,scf_convergence))
        print('\n\n\tComputed Ground State Energy = {:.8f} Ry\n\n\n'
                .format(hamiltonian.ground_state_energy))
        break
    
    # calculate hamiltonian matrix elements and diagonalize again
    orbitals.update_expansion_coefficients(new_coefficients,overlap_matrix.matrix)
    hamiltonian.atomic(orbitals,params.nuclear_z)
    hamiltonian.diagonalize(overlap_matrix.transformation_matrix)
    # calculate energy expectation value to check convergence
    hamiltonian.compute_ground_state_energy(orbitals)

# plot the wave function
if params.show_plot:
    hamiltonian.eigen_vecs[:,0] = hamiltonian.eigen_vecs[:,0]
    wave_function = np.zeros(params.num_grid_points)
    for i in range(orbitals.num_orbitals):
        wave_function = (wave_function+
                orbitals.orbitals[i,:]*hamiltonian.eigen_vecs[i,0])
    plt.plot(orbitals.grid,wave_function,'k',lw=2,zorder=10,label='{} Gaussians'
            .format(orbitals.num_orbitals))
    plt.legend()
    plt.xlabel('r (Bohr)')
    plt.ylabel('Amplitude')
    plt.xlim(0,2)
    plt.ylim(0,1.3)
    plt.title('Helium atom ground state. E = {:.8f} Ry'
            .format(hamiltonian.ground_state_energy))
    plt.show()

