"""
Christopher Greene & Chris Richardson
Elon University
Description: A generalized code for generating plots of Infrared emission line ratios based on
simulations from CLOUDY. These line ratios will act as a test of the validity of
our model of the Spectral Energy Distribution of Seyfert Galaxies."""

#Import required modules
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import os
#List all the subdirectories within directory that have the data that we want
def filelist(directory): 
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.lin'):
                print (file)
                
rootdirectory='C:/Users/chris_000/Documents/GitHub/AGN_SED/Cloudy_Data' 

filelist(rootdirectory)

#Generate a CSV file containing all the relevant data points

Output_File=r'C:/Users/chris_000/Documents/GitHub/AGN_SED/All_Emissions.csv' #Create the output file

normSource=os.path.normpath(rootdirectory)

dfs=[] #Create an empty array for our Data

d=pd.DataFrame() 
d=d.reset_index()
d2=pd.DataFrame({'Temperature': [10**4,10**5, 10**6, 10**7]},dtype=float) #Create a Dataframe of labels for each file used

for root, dirs, files in os.walk(rootdirectory, topdown=False):
    for name in files:
        if name.startswith('Hden25') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['NE 5 14.32m', 'NE 2 12.81m','NE 3 15.55m','O  4 25.88m']))
            d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2








Dasyra2011_Data=np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/dasyra2011/dasyra2011_Type1.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Dasyra2011_2_Data = np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/dasyra2011/dasyra2011_Type2.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Weaver2010_Data = np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/weaver2010/weaver2010.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)

fig = plt.figure()

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax1.scatter(np.log10(Weaver2010_Data[7]), np.log10( Weaver2010_Data[5]), marker = '^',label = 'Weaver 2010', edgecolor = '')
ax1.scatter(np.log10(Dasyra2011_Data[10]), np.log10 (Dasyra2011_Data[2]), marker = 'x', c = 'r', label = 'Dasyra 2011 Type 1')
ax1.scatter(np.log10(Dasyra2011_2_Data[10]), np.log10 (Dasyra2011_2_Data[2]), marker = '*', c = 'r', label = 'Dasyra 2011 Type 2', edgecolor = '')
ax1.scatter(d['NE 5 14.32m'].get_value(0),d['NE 2 12.81m'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax1.scatter(d['NE 5 14.32m'].get_value(1),d['NE 2 12.81m'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax1.scatter(d['NE 5 14.32m'].get_value(2),d['NE 2 12.81m'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax1.scatter(d['NE 5 14.32m'].get_value(3),d['NE 2 12.81m'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax1.set_xlabel(r'Log$_{10}$([Ne V] $\lambda$ 14.32 $\mu$m')
ax1.set_ylabel(r'Log$_{10}$([Ne II] $\lambda$ 12.81 $\mu$m')


ax2.scatter(np.log10(Weaver2010_Data[7]),np.log10(Weaver2010_Data[9]), marker = '^', edgecolor = '')
ax2.scatter(np.log10(Dasyra2011_Data[10]), np.log10 (Dasyra2011_Data[6]), marker = 'x', c = 'r', label = 'Dasyra 2011 Type 1')
ax2.scatter(np.log10(Dasyra2011_2_Data[10]), np.log10 (Dasyra2011_2_Data[6]), marker = '*', c = 'r', label = 'Dasyra 2011 Type 2', edgecolor = '')
ax2.scatter(d['NE 5 14.32m'].get_value(0),d['NE 3 15.55m'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax2.scatter(d['NE 5 14.32m'].get_value(1),d['NE 3 15.55m'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax2.scatter(d['NE 5 14.32m'].get_value(2),d['NE 3 15.55m'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax2.scatter(d['NE 5 14.32m'].get_value(3),d['NE 3 15.55m'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax2.set_xlabel(r'Log$_{10}$([Ne V] $\lambda$ 14.32 $\mu$m')
ax2.set_ylabel(r'Log$_{10}$([Ne III] $\lambda$ 15.56 $\mu$m')

ax3.scatter(np.log10(np.divide(Weaver2010_Data[14],Weaver2010_Data[7])),np.log10(np.divide(Weaver2010_Data[9],Weaver2010_Data[5])), edgecolor = '', marker ='^' )
ax3.scatter(np.log10(np.divide(Weaver2010_Data[14],Weaver2010_Data[7])),np.log10(np.divide(Weaver2010_Data[9],Weaver2010_Data[5])), edgecolor = '', marker ='^' )
ax3.set_xlim(-1,2)
ax3.set_ylim(-2,2)
ax3.set_xlabel(r'Log$_{10}$([O IV] $\lambda$ 25.88 $\mu$m / [Ne V] $\lambda$ 14.32 $\mu$m)')
ax3.set_ylabel(r'Log$_{10}$([Ne III] $\lambda$ 15.56 $\mu$m / [Ne II] $\lambda$ 12.81 $\mu$m)')

plt.legend(loc = 'lower right')
plt.suptitle('AGN Infrared Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
plt.show()


