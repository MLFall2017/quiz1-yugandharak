# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:31:21 2017

@author: kulkarniyugandhara
"""
import numpy as np
import pandas as pn
import matplotlib.pyplot as pit

#read csv file
filereader = pn.read_csv("C:\Users\kulkarniyugandhara\Documents\UNCC - MS\Sem 3\Machine Learning\Python Code\dataset_1.csv")
dataf = pn.DataFrame(filereader)
inputmatrix = dataf.as_matrix()

#calculate mean centered
meanOfMatrix = inputmatrix.mean(axis=0)
meancentered = inputmatrix - meanOfMatrix

#calculate covariance
covarMatrix = np.cov(meancentered.T)

#calculate eigenvalues and eigenvectors
eigenvalues,eignevectors = np.linalg.eig(covarMatrix)

#sorting eigenvalues - descending order
temp = np.argsort(eigenvalues)
temp = temp[::-1]
eignevectors = eignevectors[:,temp]
eigenvalues = eigenvalues[temp]
answer = np.dot(inputmatrix,eignevectors)
print answer;

pit.plot(answer[:,0],answer[:,1],'bo')
pit.show()