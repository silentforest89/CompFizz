#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title:---------- GrowDendrite - Parser

Created on Mon Jul  1 13:13:23 2019

Author:---------Ty Sterling
Contact:--------ty.sterling@colorado.edu
Instituion:-----University of Colorado Boulder
Department:-----Material Science & Physics

Description: Reads input parameters from file 

"""

class parse:
    def __init__(self,inputfile):
        nlines = sum(1 for lines in open(inputfile,'r'))
        with open(inputfile,'r') as fid:
            for i in range(nlines):
                tmp = fid.readline().strip().split()

                if len(tmp) == 0:
                    continue

                elif tmp[0] == '#':
                    continue

                elif tmp[0] == 'GRID_SIZE':
                    try:
                        self.gridsize = int(tmp[-1])
                    except:
                        print('\nERROR: GRID_SIZE must be a positive integer!\n')
                        exit()

                elif tmp[0] == 'N_PARTICLES':
                    try:
                        self.num_particles = int(tmp[-1])
                    except:
                        print('\nERROR: N_PARTICLES must be a positive integer!\n')
                        exit()

                elif tmp[0] == 'N_SEED':
                    try:
                        self.num_seeds = int(tmp[-1])
                    except:
                        print('\nERROR: N_SEED must be a positive integer!\n') 
                        exit()
                    self.seeds = []
                    for i in range(self.num_seeds):
                        tmp = fid.readline().strip().split(',')
                        try:
                            self.seeds.append([int(tmp[0]),int(tmp[-1])])
                        except:
                            print('\nERROR: there should be {} lines of comma seperated ' 
                                  'seed pairs!\n'.format(self.num_seeds))
                            exit()

                elif tmp[0] == 'STARTING_EDGE':
                    tmp[-1] = tmp[-1].strip('\'')
                    if tmp[-1] == 'random' or tmp[-1] == 'Random' or tmp[-1] == 'RANDOM':
                        self.starting_edge = 'random'
                    elif tmp[-1] == 'top' or tmp[-1] == 'Top' or tmp[-1] == 'TOP':
                        self.starting_edge = 'top'
                    elif tmp[-1] == 'bottom' or tmp[-1] == 'Bottom' or tmp[-1] == 'BOTTOM':
                        self.starting_edge = 'bottom'
                    elif tmp[-1] == 'left' or tmp[-1] == 'Left' or tmp[-1] == 'LEFT':
                        self.starting_edge = 'left'
                    elif tmp[-1] == 'right' or tmp[-1] == 'Right' or tmp[-1] == 'RIGHT':
                        self.starting_edge = 'right'
                    else:
                        try:
                            self.starting_edge = int(tmp[-1])
                        except:
                            print('\nERROR: STARTING_EDGE must be a \'random\', \'top\', ' 
                                  '\'bottom\', \'left\', \'right\', or a positive '
                                  'integer!\n')
                            exit()

                elif tmp[0] == 'STARTING_POINT':
                    tmp[-1] = tmp[-1].strip('\'')
                    if tmp[-1] == 'random' or tmp[-1] == 'Random' or tmp[-1] == 'RANDOM':
                        self.starting_point = 'random'
                    else:
                        try:
                            self.starting_point = int(tmp[-1])
                        except:
                            print('\nERROR: STARTING_POINT must be a \'random\', or a '
                                    'positive integer!\n')
                            exit()

                elif tmp[0] == 'STEP':
                    tmp[-1] = tmp[-1].strip('\'')
                    if (tmp[-1] == 'rectilinear' or tmp[-1] == 'Rectilinear' 
                            or tmp[-1] == 'RECTILINEAR'):
                        self.step = 'rectilinear'
                    elif (tmp[-1] == 'euclidean' or tmp[-1] == 'Euclidean' 
                            or tmp[-1] == 'EUCLIDEAN'):
                        self.step = 'euclidean'
                    else:                        
                        print('\nERROR: STEP must be a \'rectilinear\', or '
                                    '\'euclidean\'!\n')
                        exit()

                elif tmp[0] == 'MAKE_MOVIE':
                    tmp[-1] = tmp[-1].strip('\'')
                    if tmp[-1] == 'true' or tmp[-1] == 'True' or tmp[-1] == 'TRUE':
                        self.make_movie = True
                    else:
                        self.make_movie = False

                elif tmp[0] == 'SHOW_FIG':
                    tmp[-1] = tmp[-1].strip('\'')
                    if tmp[-1] == 'true' or tmp[-1] == 'True' or tmp[-1] == 'TRUE':
                        self.show_fig = True
                    else:
                        self.show_fig = False

                elif tmp[0] == 'GRID_FILE':
                    tmp[-1] = tmp[-1].strip('\'')
                    self.grid_file = str(tmp[-1])

                elif tmp[0] == 'RATE_FILE':
                    tmp[-1] = tmp[-1].strip('\'')
                    self.rate_file = str(tmp[-1])

                else: 
                    print('\nERROR: Option {} not recognized!\n'.format(tmp[0]))


                    


                    





