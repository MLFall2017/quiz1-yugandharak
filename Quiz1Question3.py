# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:06:34 2017

@author: kulkarniyugandhara
"""

import numpy as np

A = np.array([(0,-1),(2,3)])
eigenValueforA, eigenVectorforA = np.linalg.eig(A)
print "eigenValue for A -- ", eigenValueforA
print "eigenVector for A -- ", eigenVectorforA

'''
When calculated manually, 
the eigenvalues for given matrix are = 1, 2
When calculated programatically, the eigenvalues for given matrix are = 1, 2

The eigenvectors are in the same ratio for manual and programmatic calculations.

'''
