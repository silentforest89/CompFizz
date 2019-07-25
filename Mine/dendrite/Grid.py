#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title:----------(type name of code here)

Created on Mon Jul  1 13:13:23 2019

Author:---------Ty Sterling
Contact:--------ty.sterling@colorado.edu
Instituion:-----University of Colorado Boulder
Department:-----Material Science & Physics

Description: (type code or project description here!)

"""

import numpy as np

class grid:
    def __init__(self,n):
        if n%2 == 0:
            n = n+1
        self.grid = np.zeros((n,n))
        self.grid[n//2,n//2] = 1



