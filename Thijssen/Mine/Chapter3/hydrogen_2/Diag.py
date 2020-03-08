import numpy.linalg as linalg, numpy as np

def generalized_eigenval(overlap,hamiltonian):
    overlap_vals, overlap_vecs = linalg.eigh(overlap.overlap_mat)
    diag_overlap = np.diag(1/np.sqrt(overlap_vals))
    trans_mat = np.dot(overlap_vecs,diag_overlap)

    energies, coeffs_prime = linalg.eigh(np.dot(np.dot(
        trans_mat.conj().T,hamiltonian.hamiltonian_mat),trans_mat))

    return energies, np.dot(trans_mat,coeffs_prime)


