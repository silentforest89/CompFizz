import numpy as np

class input_params:
    pass

def parse(inputfile):
    data = input_params()
    with open(inputfile,'r') as fid:
        for line in fid:
            line = line.strip().split()
            if len(line) == 0:
                continue
            elif line[0] == '#':
                continue
            elif line[0] == 'NUM_ORBITALS':
                try:
                    data.num_orbitals = int(line[1])
                except:
                    print('\nERROR: NUM_ORBITALS must be an integer.\n')
                    exit()
                if data.num_orbitals < 1:
                    print('\nERROR: NUM_ORBITALS must be greater than 0.\n')
                    exit()
            elif line[0] == 'ALPHAS':
                data.alphas = line[1:]
                for i in range(len(data.alphas)):
                    data.alphas[i] = data.alphas[i].strip(',')
                try:
                    data.alphas = list(map(float,data.alphas))
                except:
                    print('\nERROR: ALPHAS must be a list of floats.\n')
                    exit()
            elif line[0] == 'NUCLEAR_Z':
                try:
                     data.nuclear_z = float(line[1])
                except:
                    print('\nERROR: NUCLEAR_Z must be a number.\n')
                    exit()
                if data.nuclear_z < 1:
                    print('\nERROR: NUCLEAR_Z must be greater than 0.\n')
                    exit()
            elif line[0] == 'NUM_GRID_POINTS':
                try:
                     data.num_grid_points = int(line[1])
                except:
                    print('\nERROR: NUM_GRID_POINTS must be an integer.\n')
                    exit()
                if data.num_grid_points < 1:
                    print('\nERROR: NUM_GRID_POINTS must be greater than 0.\n')
                    exit()
            elif line[0] == 'R_LIMIT':
                try:
                     data.r_limit = float(line[1])
                except:
                    print('\nERROR: R_LIMIT must be a number.\n')
                    exit()
                if data.r_limit < 1:
                    print('\nERROR: R_LIMIT must be greater than 0.\n')
                    exit()
            elif line[0] == 'SCF_TOL':
                try:
                     data.scf_tol = float(line[1])
                except:
                    print('\nERROR: SCF_TOL must be a number.\n')
                    exit()
                if data.scf_tol < 0:
                    print('\nERROR: SCF_TOL must be greater than 0.\n')
                    exit()
            elif line[0] == 'MAX_SCF':
                try:
                     data.max_scf = int(line[1])
                except:
                    print('\nERROR: MAX_SCF must be an integer.\n')
                    exit()
                if data.max_scf < 1:
                    print('\nERROR: MAX_SCF must be greater than 0.\n')
                    exit()
            elif line[0] == 'SCF_GUESS':
                data.scf_guess = str(line[-1].strip('\''))
                if (data.scf_guess == 'equal' or data.scf_guess == 'EQUAL' or 
                        data.scf_guess == 'Equal'):
                    data.scf_guess = 'equal'
                elif (data.scf_guess == 'random' or data.scf_guess == 'RANDOM' or 
                        data.scf_guess == 'Random'):
                    data.scf_guess = 'random'
                else:
                    print('\nERROR: SCF_GUESS option not recognized.\n')
                    exit()
            elif line[0] == 'SHOW_WAVEFUNCTION':
                data.show_plot = str(line[-1].strip('\''))
                if (data.show_plot == 'True' or data.show_plot == 'TRUE' or
                        data.show_plot == 'true'):
                    data.show_plot = True
                else:
                    data.show_plot = False 
            else:
                print('\nERROR: option {} not recognized.\n'.format(line[-1]))
                exit()
        return data



