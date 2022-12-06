# -*- coding: utf-8 -*-

# A Fourier-transformed feature engineering design for predicting ternary perovskite properties by coupling a two-dimensional convolutional neural network with a support vector machine (Conv2D-SVM)

# AUTHOR - (1) * Ericsson Chenebuah, (1) Michel Nganbe and (2) Alain Tchagang 
# 1: Department of Mechanical Engineering, University of Ottawa, 75 Laurier Ave. East, Ottawa, ON, K1N 6N5 Canada
# 2: Digital Technologies Research Centre, National Research Council of Canada, 1200 Montréal Road, Ottawa, ON, K1A 0R6 Canada
# * email: echen013@uottawa.ca 
# (28-May-2022)

"""DScribe_eigen.py

Automatically generated by Colaboratory.

"""

## THIS SCRIPT DESCRIBES THE COMPUTATIONAL CODES FOR THE PERIODIC GLOBAL DESCRIPTORS i.e. COULOMB, EWALD-SUM, AND SINE MATRIX IN THEIR EIGENVALUE FORMS USING "DScribe".
## THE GENERALIZED FEATURE IS CONCATENATED WITH THE EIGENVALUE DESCRIPTORS AND USED TO ENHANCE THE PREDICTIVE CAPABILITY OF THE PERIODIC GLOBAL DESCRIPTOR.

# The data file to run this code is separated and compressed as "DScribe Data" on the github repository.

# All calculations related to the atomic coordinates were converted from Angstroms to Atomic Units

#! pip install dscribe

import pandas as pd
import numpy as np
from dscribe.descriptors import CoulombMatrix, EwaldSumMatrix, SineMatrix
from ase import Atoms

# 5 Number of atoms in unit cell
df1 = pd.read_csv('DScribe_5.csv') 

data_cm1 = []
data_esm1 = []
data_sine1 = []

for i in range (0, 13195):
  perov = Atoms(symbols=[df1.iloc[(i,0)], df1.iloc[(i,1)], df1.iloc[(i,2)], df1.iloc[(i,3)], df1.iloc[(i,4)]], 
              positions=[(df1.iloc[i, 5:8]), (df1.iloc[i, 8:11]), (df1.iloc[i, 11:14]), (df1.iloc[i, 14:17]), (df1.iloc[i, 17:20])],
              cell=[df1.iloc[(i,20)], df1.iloc[(i,21)], df1.iloc[(i,22)], df1.iloc[(i,23)], df1.iloc[(i,24)], df1.iloc[(i,25)]], pbc=True)
  
  cm= CoulombMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  cm_out = cm.create(perov)
  data_cm1.append(cm_out)

  esm= EwaldSumMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  esm_out = esm.create(perov)
  data_esm1.append(esm_out)

  sine= SineMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  sine_out = sine.create(perov)
  data_sine1.append(sine_out)

data_cm1 = np.array(data_cm1)
data_esm1 = np.array(data_esm1)
data_sine1 = np.array(data_sine1)

# 10 Number of atoms in unit cell
df2 = pd.read_csv('DScribe_10.csv')

data_cm2 = []
data_esm2 = []
data_sine2 = []

for i in range (0, 10277):
  perov = Atoms(symbols=[df2.iloc[(i,0)], df2.iloc[(i,1)], df2.iloc[(i,2)], df2.iloc[(i,3)], df2.iloc[(i,4)], df2.iloc[(i,5)], df2.iloc[(i,6)], df2.iloc[(i,7)], df2.iloc[(i,8)],
                         df2.iloc[(i,9)]], 
                positions=[(df2.iloc[i, 10:13]), (df2.iloc[i, 13:16]), (df2.iloc[i, 16:19]), (df2.iloc[i, 19:22]), (df2.iloc[i, 22:25]), (df2.iloc[i, 25:28]),
                           (df2.iloc[i, 28:31]), (df2.iloc[i, 31:34]), (df2.iloc[i, 34:37]), (df2.iloc[i, 37:40])], 
                cell=[df2.iloc[(i,40)], df2.iloc[(i,41)], df2.iloc[(i,42)], df2.iloc[(i,43)], df2.iloc[(i,44)], df2.iloc[(i,45)]], pbc=True)
  
  cm= CoulombMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  cm_out = cm.create(perov)
  data_cm2.append(cm_out)

  esm= EwaldSumMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  esm_out = esm.create(perov)
  data_esm2.append(esm_out)

  sine= SineMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  sine_out = sine.create(perov)
  data_sine2.append(sine_out)

data_cm2 = np.array(data_cm2)
data_esm2 = np.array(data_esm2)
data_sine2 = np.array(data_sine2)

# 15 Number of atoms in unit cell
df3 = pd.read_csv('DScribe_15.csv')

data_cm3 = []
data_esm3 = []
data_sine3 = []

for i in range (0, 49):
  perov = Atoms(symbols=[df3.iloc[(i,0)], df3.iloc[(i,1)], df3.iloc[(i,2)], df3.iloc[(i,3)], df3.iloc[(i,4)], df3.iloc[(i,5)], df3.iloc[(i,6)], df3.iloc[(i,7)], df3.iloc[(i,8)],
                         df3.iloc[(i,9)], df3.iloc[(i,10)], df3.iloc[(i,11)], df3.iloc[(i,12)], df3.iloc[(i,13)], df3.iloc[(i,14)]], 
                positions=[(df3.iloc[i, 15:18]), (df3.iloc[i, 18:21]), (df3.iloc[i, 21:24]), (df3.iloc[i, 24:27]), (df3.iloc[i, 27:30]), (df3.iloc[i, 30:33]), (df3.iloc[i, 33:36]),
                           (df3.iloc[i, 36:39]), (df3.iloc[i, 39:42]), (df3.iloc[i, 42:45]), (df3.iloc[i, 45:48]), (df3.iloc[i, 48:51]), (df3.iloc[i, 51:54]), (df3.iloc[i, 54:57]),
                           (df3.iloc[i, 57:60])], 
                cell=[df3.iloc[(i,60)], df3.iloc[(i,61)], df3.iloc[(i,62)], df3.iloc[(i,63)], df3.iloc[(i,64)], df3.iloc[(i,65)]], pbc=True)
  
  cm= CoulombMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  cm_out = cm.create(perov)
  data_cm3.append(cm_out)

  esm= EwaldSumMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  esm_out = esm.create(perov)
  data_esm3.append(esm_out)

  sine= SineMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  sine_out = sine.create(perov)
  data_sine3.append(sine_out)

data_cm3 = np.array(data_cm3)
data_esm3 = np.array(data_esm3)
data_sine3 = np.array(data_sine3)

# 20 Number of atoms in unit cell
df4 = pd.read_csv('DScribe_20.csv')

data_cm4 = []
data_esm4 = []
data_sine4 = []

for i in range (0, 4066):
  perov = Atoms(symbols=[df4.iloc[(i,0)], df4.iloc[(i,1)], df4.iloc[(i,2)], df4.iloc[(i,3)], df4.iloc[(i,4)], df4.iloc[(i,5)], df4.iloc[(i,6)], df4.iloc[(i,7)], df4.iloc[(i,8)],
                         df4.iloc[(i,9)], df4.iloc[(i,10)], df4.iloc[(i,11)], df4.iloc[(i,12)], df4.iloc[(i,13)], df4.iloc[(i,14)], df4.iloc[(i,15)], df4.iloc[(i,16)], df4.iloc[(i,17)], 
                         df4.iloc[(i,18)], df4.iloc[(i,19)]], 
              positions=[(df4.iloc[i, 20:23]), (df4.iloc[i, 23:26]), (df4.iloc[i, 26:29]), (df4.iloc[i, 29:32]), (df4.iloc[i, 32:35]), (df4.iloc[i, 35:38]), (df4.iloc[i, 38:41]), 
                         (df4.iloc[i, 41:44]), (df4.iloc[i, 44:47]), (df4.iloc[i, 47:50]), (df4.iloc[i, 50:53]), (df4.iloc[i, 53:56]), (df4.iloc[i, 56:59]), (df4.iloc[i, 59:62]),
                         (df4.iloc[i, 62:65]), (df4.iloc[i, 65:68]), (df4.iloc[i, 68:71]), (df4.iloc[i, 71:74]), (df4.iloc[i, 74:77]), (df4.iloc[i, 77:80])],
              cell=[df4.iloc[(i,80)], df4.iloc[(i,81)], df4.iloc[(i,82)], df4.iloc[(i,83)], df4.iloc[(i,84)], df4.iloc[(i,85)]], pbc=True)
  
  cm= CoulombMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  cm_out = cm.create(perov)
  data_cm4.append(cm_out)

  esm= EwaldSumMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  esm_out = esm.create(perov)
  data_esm4.append(esm_out)

  sine= SineMatrix(n_atoms_max=20, flatten=False, permutation='eigenspectrum')
  sine_out = sine.create(perov)
  data_sine4.append(sine_out)

data_cm4 = np.array(data_cm4)
data_esm4 = np.array(data_esm4)
data_sine4 = np.array(data_sine4)

# concatenate all matrices
eigen_cm=np.abs(np.concatenate([data_cm1, data_cm2, data_cm3, data_cm4], axis=0))
eigen_esm=np.abs(np.concatenate([data_esm1, data_esm2, data_esm3, data_esm4], axis=0))
eigen_sine=np.abs(np.concatenate([data_sine1, data_sine2, data_sine3, data_sine4], axis=0))

from sklearn.preprocessing import MinMaxScaler

scaler_cm = MinMaxScaler()
eigen_cm = np.asarray(scaler_cm.fit_transform(eigen_cm))

scaler_esm = MinMaxScaler()
eigen_esm = np.asarray(scaler_esm.fit_transform(eigen_esm))

scaler_sine = MinMaxScaler()
eigen_sine = np.asarray(scaler_sine.fit_transform(eigen_sine))

## GENERALIZED FEATURES
GF = np.asarray(pd.read_csv('gen_feat.csv').astype('float32'))
scaler_gen = MinMaxScaler()
GF = np.asarray(scaler_gen.fit_transform(GF))

# Concatenated periodic input descriptor
x_cm = np.concatenate((GF,eigen_cm), axis=-1) #Coulomb matrix eigen representation with generalized features 
x_esm = np.concatenate((GF,eigen_esm), axis=-1) #Ewald-sum matrix eigen representation with generalized features
x_sine = np.concatenate((GF,eigen_sine), axis=-1) #Sine matrix eigen representation with generalized features
