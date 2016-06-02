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
        if name.startswith('Metallicity34') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A']))
            d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2








Dasyra2011_Data=np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/dasyra2011/dasyra2011_Type1.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Dasyra2011_2_Data = np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/dasyra2011/dasyra2011_Type2.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Weaver2010_Data = np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/weaver2010/weaver2010.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)

fig = plt.figure()

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)

ax1.scatter(np.log10(Weaver2010_Data[6]), np.log10( Weaver2010_Data[4]), marker = '^',label = 'Weaver 2010', edgecolor = '')
ax1.scatter(np.log10(Dasyra2011_Data[9]), np.log10 (Dasyra2011_Data[2]), marker = 'x', c = 'r', label = 'Dasyra 2011 Type 1')
ax1.scatter(np.log10(Dasyra2011_2_Data[8]), np.log10 (Dasyra2011_2_Data[2]), marker = '*', c = 'r', label = 'Dasyra 2011 Type 2', edgecolor = '')
ax1.set_xlabel(r'Log$_{10}$([Ne V] $\lambda$ 14.32 $\mu$m')
ax1.set_ylabel(r'Log$_{10}$([Ne II] $\lambda$ 12.81 $\mu$m')
ax1.legend(loc = 'lower right')




plt.show()


