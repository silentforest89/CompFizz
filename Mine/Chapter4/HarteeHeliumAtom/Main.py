import numpy as np
import matplotlib.pyplot as plt
import Overlap
import Orbitals
import Hamiltonian

############################# INPUT PARAMETERS ###################################
num_orbitals = 4
num_grid_points = 5000
alphas = [0.298073,1.242567,5.782948,38.474970]
r_limit = 24
nuclear_z = 2

scf_tol = 1e-8
max_scf = 50
scf_guess = 'equal'

############### CALCULATE OVERLAP MATRIX AND HAMILTONIAN ##########################
orbitals = Orbitals.orbitals(num_orbitals,num_grid_points,r_limit)
orbitals.gaussian_functions(alphas,guess=scf_guess)

overlap_matrix = Overlap.matrix(orbitals)
overlap_matrix.transform()

hamiltonian = Hamiltonian.hamiltonian(orbitals)
hamiltonian.atomic(orbitals,nuclear_z)

########### DIAGONALIZE HAMILTONIAN AND ITERATE TO SELF CONSISTENCY ###############
last_energy_value = 0
hamiltonian.diagonalize(overlap_matrix.transformation_matrix)
hamiltonian.compute_ground_state_energy(orbitals)

print('\n####### SCF: ITERATING TO SELF CONSISTENCY ########\n')
for num_iter in range(1,max_scf+1):    
    new_coefficients = hamiltonian.eigen_vecs[:,np.argmin(hamiltonian.eigen_vals)]

    scf_convergence = abs(hamiltonian.ground_state_energy-last_energy_value)
    last_energy_value = hamiltonian.ground_state_energy

    print('\tStep {} convergence = {:.10f} Ry'.format(num_iter,scf_convergence))

    if num_iter == max_scf:
        print('\n*** WARNING: SCF failed to converge ***')
        print('\nSCF did ***NOT*** converge in {} iterations\n'
              'Final SCF accuracy = {:.10f} Ry\n'.format(num_iter,scf_convergence))
        print('\n\n\tComputed Ground State Energy = {:.8f} Ry\n\n\n'
                .format(hamiltonian.ground_state_energy))
        break

    elif num_iter != 1 and abs(scf_convergence) < scf_tol:
        print('\nSCF convergence achieved in {} iterations\n'
              'Final SCF accuracy = {:.10f} Ry\n'.format(num_iter,scf_convergence))
        print('\n\n\tComputed Ground State Energy = {:.8f} Ry\n\n\n'
                .format(hamiltonian.ground_state_energy))
        break

    orbitals.update_expansion_coefficients(new_coefficients,overlap_matrix.matrix)
    hamiltonian.atomic(orbitals,nuclear_z)
    hamiltonian.diagonalize(overlap_matrix.transformation_matrix)
    hamiltonian.compute_ground_state_energy(orbitals)

#################### PLOT THE GROUND STATE WAVE FUNCTION ##########################
hamiltonian.eigen_vecs[:,0] = hamiltonian.eigen_vecs[:,0]
wave_function = np.zeros(num_grid_points)
for i in range(orbitals.num_orbitals):
    wave_function = (wave_function+
            orbitals.orbitals[i,:]*hamiltonian.eigen_vecs[i,0])
plt.plot(orbitals.grid,wave_function,'k',lw=2,zorder=10,label='4 Gaussians')
plt.legend()
plt.xlabel('r (Bohr)')
plt.ylabel('Amplitude')
plt.xlim(0,2)
plt.ylim(0,1.3)
plt.title('Helium atom ground state. E = {:.8f} Ry'
        .format(hamiltonian.ground_state_energy))
plt.show()

