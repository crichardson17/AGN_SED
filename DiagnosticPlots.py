#!/usr/bin/env python
"""
Christopher Greene & Chris Richardson
Elon University
Description: A generalized code for generating plots of line ratios based on
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
        if name.startswith('PhiH104771') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A']))
            d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2



d['O III / H-Beta']=np.log10(np.divide(d['O  3  5007A'],d['TOTL  4861A']))

d['O I / H-Alpha']=np.log10(np.divide(d['O  1  6300A'],d['H  1  6563A']))

d['N II / H-Alpha']=np.log10(np.divide(d['N  2  6584A'],d['H  1  6563A']))

d['S II / H-Alpha']=np.log10(np.divide(d['S  2  6720A'],d['H  1  6563A']))

d['O II / O III'] = np.log10(np.divide(d['TOTL  3727A'],d['O  3  5007A']))

d['He II / H-Beta'] = np.log10(np.divide(d['HE 2  4686A'],d['TOTL  4861A']))

d['Ne V / Ne III'] = np.log10(np.divide(d['NE 5  3426A'],d['NE 3  3869A']))

d['S II 6716/ S II 6731'] = np.log10(np.divide(d['S II  6716A'],d['S II  6731A']))

d['O II / N II'] = np.log10(np.divide(d['TOTL  3727A'],d['N  2  6584A']))

d['O III / O II'] = np.log10(np.divide(d['O  3  5007A'],d['TOTL  3727A']))

d.to_csv(Output_File, sep = ",", index=True)


#Plot these data points
SDSS_Data=np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/flux_norm.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Shirazi_Data=np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/shirazi12.csv', skip_header=3, delimiter = ',',unpack=True)

f = plt.figure()

ax1 = plt.subplot(331)
ax2 = plt.subplot(332)
ax3 = plt.subplot(333)
ax4 = plt.subplot(334)
ax5 = plt.subplot(335)
ax6 = plt.subplot(336)
ax7 = plt.subplot(337)
#Need to find a way to make all the plots squares
z = [10^4,10^5, 10^6, 10^7]
x1=np.arange(-2,0.3,0.01)
y1=1.19+np.divide(0.61,x1-0.47)
x2=np.arange(-2,0,0.01)
y2 = 1.3+np.divide(0.61,x2-0.05)

    
ax1.scatter(np.log10(np.divide(SDSS_Data[18],SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), s=0.5)
l1 = ax1.scatter(d['N II / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
l2 = ax1.scatter(d['N II / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
l3 = ax1.scatter(d['N II / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
l4 = ax1.scatter(d['N II / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax1.plot(x1,y1,c = '0.5',linewidth = 2)
ax1.plot(x2,y2, c = '0.5',ls = '-', lw = 2)
#ax1.set_title(r'Log$_{10}$([N II] $\lambda 6583$ / H$\alpha$) vs Log$_{10}$(O III] $\lambda 5700$ / H$\beta$) ')
ax1.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))
ax1.set_xlim(np.log10(10**(-2)), np.log10(10**1.5))
ax1.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax1.set_xlabel(r'Log$_{10}$([N II] $\lambda 6584$ / H$\alpha$)')
ax1.text(-1,1,'AGN')
ax1.text(-0.2,-1,'Composite')
ax1.text(-1.4,-1,'Starburst')

x3 = np.arange(-3,-0.7,0.01)
y3 = 1.33 + np.divide(0.73,x3+0.59)
x4 = np.arange(-1.1,0,0.01)
y4 = 1.18*x4+1.3
ax2.scatter(np.log10(np.divide(SDSS_Data[15],SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), s=0.5, c='b')
ax2.scatter(d['O I / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax2.scatter(d['O I / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax2.scatter(d['O I / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax2.scatter(d['O I / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax2.plot(x3,y3,c = '0.5', ls = '-', linewidth = 2)

ax2.plot(x4,y4,c = '0.5', ls = '-', linewidth = 3.0)

ax2.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))
ax2.set_xlim(np.log10(10**(-3)),np.log10(10**0))
ax2.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax2.set_xlabel(r'Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$)')
ax2.text(-2,1, 'Seyfert')
ax2.text(-2.5,0.5, 'Starburst')
ax2.text(-0.5,-1,'LINER')


x5 = np.arange(-3,0.1,0.01)
y5 = 1.30 + np.divide(0.72,x5-0.32)
x6 = np.arange(-0.3,1.0,0.01)
y6 = 1.89 * x6 + 0.76
ax3.scatter(np.log10(np.divide(np.add(SDSS_Data[19],SDSS_Data[20]),SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), s=0.5, c='b')
ax3.scatter(d['S II / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax3.scatter(d['S II / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax3.scatter(d['S II / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax3.scatter(d['S II / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax3.plot(x5,y5, c='0.5',ls = '-',linewidth=2)
ax3.plot(x6,y6, c='0.5',ls = '-',linewidth=3.0)
ax3.set_xlim(np.log10(10**(-3)),np.log10(10**1))
ax3.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))
ax3.set_ylabel(r'Log$1{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax3.set_xlabel(r'Log$_{10}$([S II] $\lambda 6720$ / H$\alpha$)')
ax3.text(-1.3,1,'Seyfert')
ax3.text(0.2,-0.5,'LINER')

ax4.scatter(np.log10(np.divide(np.add(SDSS_Data[5],SDSS_Data[6]),SDSS_Data[13])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), s=2, c='b')
ax4.scatter(d['O II / O III'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax4.scatter(d['O II / O III'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax4.scatter(d['O II / O III'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax4.scatter(d['O II / O III'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")

ax4.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax4.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / [O III] $\lambda 5007$)')
ax4.set_xlim(np.log10(10**(-2)),np.log10(10**1.5))
ax4.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))


x = np.arange(-3,-0.2,0.01)
y = -1.22 + np.divide(1,8.92*x+1.32)
ax5.scatter(Shirazi_Data[7],Shirazi_Data[6], marker = '+',s = 10)
ax5.scatter(d['N II / H-Alpha'].get_value(0),d['He II / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax5.scatter(d['N II / H-Alpha'].get_value(1),d['He II / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax5.scatter(d['N II / H-Alpha'].get_value(2),d['He II / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax5.scatter(d['N II / H-Alpha'].get_value(3),d['He II / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax5.plot(x,y, c = '0.5', ls = '-', lw = 2.0)
ax5.set_xlim(-3,1)
ax5.set_ylim(-3,1)
ax5.set_xlabel(r'Log$_{10}$([N II] $\lambda 6584$ / H$\alpha$)')
ax5.set_ylabel(r'Log$_{10}$([He II] $\lambda 4686$ / H$\beta$)')
ax5.text(-1,-2.5, 'Starburst')
ax5.text(-2,0,'AGN')


ax6.scatter(np.log10(np.divide(np.add(SDSS_Data[5],SDSS_Data[6]),SDSS_Data[18])),np.log10(np.divide(SDSS_Data[19],SDSS_Data[20])),s = 0.5)
ax6.scatter(d['O II / N II'].get_value(0),d['S II 6716/ S II 6731'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax6.scatter(d['O II / N II'].get_value(1),d['S II 6716/ S II 6731'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax6.scatter(d['O II / N II'].get_value(2),d['S II 6716/ S II 6731'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax6.scatter(d['O II / N II'].get_value(3),d['S II 6716/ S II 6731'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax6.set_ylabel(r'Log$_{10}$([S II] $\lambda 6716$ / [S II] $\lambda 6731$')
ax6.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / [N II] $\lambda 6584$)')

x7 = np.arange(-2.5,1.5)
y7 = -1.701*x7-2.163
x8 = np.arange(-1.1,1)
y8 = 1.0*x8+0.7
ax7.scatter(np.log10(np.divide(SDSS_Data[15],SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],np.add(SDSS_Data[5],SDSS_Data[6]))),s = 0.5)
ax7.scatter(d['O I / H-Alpha'],d['O III / O II'],  marker = "s", c=z, cmap = cm.hot, s = 30)
ax7.scatter(d['O I / H-Alpha'].get_value(0),d['O III / O II'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax7.scatter(d['O I / H-Alpha'].get_value(1),d['O III / O II'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax7.scatter(d['O I / H-Alpha'].get_value(2),d['O III / O II'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax7.scatter(d['O I / H-Alpha'].get_value(3),d['O III / O II'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax7.plot(x7,y7, x8,y8, c = '0.5', lw = 3.0)
ax7.set_xlim(-2.5,0.5)
ax7.set_ylim(-1.5,1.0)
ax7.set_xlabel(r'Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$)')
ax7.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$) / [O II] $\lambda 3727$)')
ax7.text(-1.5,.75,'Seyfert')
ax7.text(0,0,'LINER')
ax7.text(-2.1,-1.25, 'Starburst')
plt.suptitle('AGN Diagnostic Plots: Efrac = 0.01, Phi(h) = 10.4771, n(h) = 3')
ax1.legend()
plt.show() 
