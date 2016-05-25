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
d2=pd.DataFrame({'Temperature': ['10^4','10^5', '10^6', '10^7']},dtype=object) #Create a Dataframe of labels for each file used

for root, dirs, files in os.walk(rootdirectory, topdown=False):
    for name in files:
        if name.startswith('Pressure') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'TOTL  3727A']))
            d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2



d['O III / H-Beta']=np.log10(d['O  3  5007A']/d['H  1  6563A'])

d['O I / H-Alpha']=np.log10(d['O  1  6300A']/d['TOTL  4861A'])

d['N II / H-Alpha']=np.log10(d['N  2  6584A']/d['TOTL  4861A'])

d['S II / H-Alpha']=np.log10(d['S  2  6720A']/d['TOTL  4861A'])

d['O II / O III'] = np.log10(d['TOTL  3727A']/d['O  3  5007A'])

  

d.to_csv(Output_File, sep = ",", index=True)

#Plot these data points
SDSS_Data=np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/flux_norm.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)

f,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)

x1=np.arange(-2,0.3,0.01)
y1=1.19+np.divide(0.61,x1-0.47)
x2=np.arange(-2,0,0.01)
y2 = 1.3+np.divide(0.61,x2-0.05)

ax1.scatter(np.log10(np.divide(SDSS_Data[18],SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), s=0.5, c='b')
ax1.scatter(d['N II / H-Alpha'],d['O III / H-Beta'], c= 'r')
ax1.plot(x1,y1,'b-',x2,y2,'r--',linewidth = 2)
ax1.set_title(r'Log$_{10}$([N II] $\lambda 6583$ / H$\alpha$) vs Log$_{10}$(O III] $\lambda 5700$ / H$\beta$) ')
ax1.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))
ax1.set_xlim(np.log10(10**(-2)), np.log10(10**1.5))
ax1.set_ylabel(r'Log$_{10}$([O III] $\lambda 5700$ / H$\beta$)')
ax1.set_xlabel(r'Log$_{10}$([N II] $\lambda 6583$ / H$\alpha$)')
ax1.text(-1,1,'AGN')
ax1.text(-0.2,-1,'Composite')
ax1.text(-1.4,-1,'Starburst')

x3 = np.arange(-3,-0.7,0.01)
y3 = 1.33 + np.divide(0.73,x3+0.59)
x4 = np.arange(-1.1,-0.5,0.01)
y4 = 1.18*x4+1.3
ax2.scatter(np.log10(np.divide(SDSS_Data[15],SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), s=0.5, c='b')
ax2.scatter(d['O I / H-Alpha'],d['O III / H-Beta'], c='r')
ax2.plot(x3,y3,x4,y4,'r--',linewidth = 2)
ax2.set_title(r'(Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$) vs [O III] $\lambda 5700$ / H$\beta$) ')
ax2.set_title(r'Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$) vs [O III] $\lambda 5700$ / H$\beta$) ')
ax2.set_xlim(np.log10(10**(-3)),np.log10(10**0))
ax2.set_ylabel(r'Log$_{10}$([O III] $\lambda 5700$ / H$\beta$)')
ax2.set_xlabel(r'Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$)')
ax2.text(-2,1, 'Seyfert')
ax2.text(-2.5,0.5, 'Starburst')
ax2.text(-0.5,-1,'LINER')


x5 = np.arange(-3,0.1,0.01)
y5 = 1.30 + np.divide(0.72,x5-0.32)
x6 = np.arange(-0.3,0.1,0.01)
y6 = 1.89 * x6 + 0.76
ax3.scatter(np.log10(np.divide(np.add(SDSS_Data[19],SDSS_Data[20]),SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), s=0.5, c='b')
ax3.scatter(d['S II / H-Alpha'],d['O III / H-Beta'],c = 'r')
ax3.plot(x5,y5,x6,y6, 'r--',linewidth=2)
ax3.set_title(r'Log$_{10}$([S II] $\lambda 6720$ / H$\alpha$) vs Log$_{10}$([O III] $\lambda 5700$ / H$\beta$) ')
ax3.set_xlim(np.log10(10**(-3)),np.log10(10**1))
ax3.set_ylabel(r'Log$_{10}$([O III] $\lambda 5700$ / H$\beta$)')
ax3.set_xlabel(r'Log$_{10}$([S II] $\lambda 6720$ / H$\alpha$)')
ax3.text(-1,1,'Seyfert')
ax3.text(0.2,-0.5,'LINER')

ax4.scatter(np.log10(np.divide(np.add(SDSS_Data[5],SDSS_Data[6]),SDSS_Data[13])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), s=0.5, c='b')
ax4.scatter(d['O II / O III'],d['O III / H-Beta'],c='r')
ax4.set_title(r'Log$_{10}$([O II] $\lambda 3727$ / [O III] $\lambda 5007$) vs Log$_{10}$([O III] $\lambda 5700$ / H$\beta$) ')
ax4.set_ylabel(r'Log$_{10}$([O III] $\lambda 5700$ / H$\beta$)')
ax4.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / [O III] $\lambda 5007$)')
ax4.set_xlim(np.log10(10**(-2)),np.log10(10**1.5))
plt.show() 
