#!/usr/bin/env python
"""
Christopher Greene & Chris Richardson
Elon University
Description: A generalized code for generating plots of line ratios based on
simulations from CLOUDY. These line ratios will act as a test of the validity of
our model of the Spectral Energy Distribution of Seyfert Galaxies."""

#Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

#List all the subdirectories within directory that have the data that we want
def filefind(directory): 
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.lin'):
                print file
                
directory=r'Users/compastro/greene/AGN_SED/Cloudy_Data' 

filefind(directory)

#Generate a CSV file containing all the relevant data points

Output_File=r'/Users/compastro/greene/AGN_SED/All_Emissions.csv' #Create the output file

normSource=os.path.normpath(directory)

dfs=[] #Create an empty array for our Data

d=pd.DataFrame() 

d2=pd.DataFrame({'Temperature': ['10^4','10^5', '10^6', '10^7']},dtype=object) #Create a Dataframe of labels for each file used

for root, dirs, files in os.walk(normSource, topdown=False):
    for name in files:
        if  name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter='/t', usecols=['TOTL  4861A','O  3  5007A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' ]))
            d = pd.concat(dfs, ignore_index=False)
            
d['Temperature']=d2



d['O III / H-Beta']=np.log10(d['O  3  5007A']/d['H  1  6563A'])

d['O I / H-Alpha']=np.log10(d['O  1  6300A']/d['TOTL  4861A'])

d['N II / H-Alpha']=np.log10(d['N  2  6584A']/d['TOTL  4861A'])

d['S II / H-Alpha']=np.log10(d['S  2  6720A']/d['TOTL  4861A'])

d.to_csv(Output_File, sep = ",", index=True)

#Plot these data points
f,(ax1,ax2,ax3) = plt.subplots(3)

ax1.scatter(d['N II / H-Alpha'],d['O III / H-Beta'],)

ax1.set_title(r'Log$_{10}$([N II] $\lambda 6583$ / H$\alpha$) vs Log$_{10}$(O III] $\lambda 5700$ / H$\beta$) ')
ax1.set_ylim(np.log10(10**(-0.5)), np.log10(10**(1.5)))
ax1.set_xlim(np.log10(10**(-3)),np.log10(10**1))

ax2.scatter(d['O I / H-Alpha'],d['O III / H-Beta'])
ax2.set_title(r'Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$) vs [O III] $\lambda 5700$ / H$\beta$) ')
ax2.set_ylim(np.log10(10**(-0.5)), np.log10(10**(1.5)))
ax2.set_xlim(np.log10(10**(-2)),np.log10(10**0))

ax3.scatter(d['S II / H-Alpha'],d['O III / H-Beta'])
ax3.set_title(r'Log$_{10}$([S II] $\lambda 6720$ / H$\alpha$) vs Log$_{10}$([O III] $\lambda 5700$ / H$\beta$) ')
ax3.set_ylim(np.log10(10**(-0.5)), np.log10(10**(1.5)))
ax3.set_xlim(np.log10(10**(-4)),np.log10(10**1))
plt.show()
