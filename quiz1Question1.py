# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:46:53 2017

@author: kulkarniyugandhara
"""

import numpy as np
import pandas as pn
import matplotlib.pyplot as pit

#read csv file
filereader = pn.read_csv("C:\Users\kulkarniyugandhara\Documents\UNCC - MS\Sem 3\Machine Learning\Python Code\dataset_1.csv")
dataf = pn.DataFrame(filereader)
inputmatrix = dataf.as_matrix()
 
#Part 1
varianceX = np.var(inputmatrix[:,0])
varianceY = np.var(inputmatrix[:,1])
varianceZ = np.var(inputmatrix[:,2])

print "variable x------", varianceX
print "variable y------", varianceY
print "variable z------", varianceZ

#Part 2

covXY = np.cov(inputmatrix[:,0],inputmatrix[:,1])
print 'covariance between x and y----', covXY

covYZ = np.cov(inputmatrix[:,1],inputmatrix[:,2])
print 'covariance between y and z----', covYZ
'''
1.
Variance of x = 0.0805
Variance of y = 2.096
Variance of z = 0.0805

2.
Covariance between x and y = 
[[ 0.08060992  0.40242878]
 [ 0.40242878  2.09900159]]

Covariance between y and z =
 [[ 2.09900159 -0.01439466]
 [-0.01439466  0.08058254]]
 
 3. Answer to 3rd part is in PCA.py
'''