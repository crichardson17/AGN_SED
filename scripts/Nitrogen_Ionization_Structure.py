#Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


#import our data
NitrogenT5_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T4/Linear_fit/ax219/Ionization_35/Ionization_35_Linear_Fit_ax219_SEDT4_nitrogen.txt'
NitrogenT5_Data=np.genfromtxt(NitrogenT5_File, skip_header=1,dtype=float,unpack=False)
print(NitrogenT5_Data[:,0])
plt.scatter(NitrogenT5_Data[:,0],NitrogenT5_Data[:,1], c = 'g',edgecolor = '', label = 'n = 1')
plt.scatter(NitrogenT5_Data[:,0],NitrogenT5_Data[:,2], c = 'r',edgecolor = '', label = 'n = 2')
plt.scatter(NitrogenT5_Data[:,0],NitrogenT5_Data[:,3], c = 'y',edgecolor = '', label = 'n = 3')
plt.scatter(NitrogenT5_Data[:,0],NitrogenT5_Data[:,4], c = 'b', edgecolor = '', label = 'n = 4')
plt.scatter(NitrogenT5_Data[:,0],NitrogenT5_Data[:,5], c = 'cyan', edgecolor = '',label = 'n = 5')
plt.scatter(NitrogenT5_Data[:,0],NitrogenT5_Data[:,6], c = 'm', edgecolor = '', label = 'n = 6')
plt.legend(loc = 'right')
plt.ylim(-.05,1.05)
plt.xlabel('Depth (cm)')
plt.ylabel('Ionization Fraction')
plt.title(r'Nitrogen Ionization Structure as a Function of Depth ($T = 10 ^ 4 K$, ax = 2.19)')
plt.show()