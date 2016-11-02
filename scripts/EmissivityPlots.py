# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 12:39:07 2016

@author: chris_000
"""

#Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


#import our data
NitrogenT4_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT4_lines.str'
NitrogenT4_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT4_lines.str' 
NitrogenT4_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Baseline\Ionization35\Ionization_35_SEDT4_lines.str'
NitrogenT5_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Baseline\Ionization35\Ionization_35_SEDT5_lines.str'
NitrogenT6_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Baseline\Ionization_35\Ionization_35_SEDT6lines.str'
NitrogenT7_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Baseline\Ionization_35\Ionization_35_SEDT7_lines.str'
NitrogenT5_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT5_lines.str'
NitrogenT5_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT5_lines.str'
NitrogenT6_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT6_lines.str'
NitrogenT6_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT6_lines.str'
NitrogenT7_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT7_lines.str'
NitrogenT7_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT7_lines.str'


NitrogenT4_data = np.genfromtxt(NitrogenT4_File, skip_header=1,dtype=float,unpack=False)
NitrogenT5_data=np.genfromtxt(NitrogenT5_File, skip_header=1,dtype=float,unpack=False)
nitrogenT6_data = np.genfromtxt(NitrogenT6_File, skip_header=1,dtype=float,unpack=False)
nitrogenT7_data = np.genfromtxt(NitrogenT7_File, skip_header=1,dtype=float,unpack=False)
nitrogenT4_ax117_data = np.genfromtxt(NitrogenT4_ax117_File, skip_header=1,dtype=float,unpack=False)
nitrogenT4_ax219_data = np.genfromtxt(NitrogenT4_ax219_File, skip_header=1,dtype=float,unpack=False)
nitrogenT5_ax117_data = np.genfromtxt(NitrogenT5_ax117_File, skip_header=1,dtype=float,unpack=False)
nitrogenT5_ax219_data = np.genfromtxt(NitrogenT5_ax219_File, skip_header=1,dtype=float,unpack=False)
nitrogenT6_ax117_data = np.genfromtxt(NitrogenT6_ax117_File, skip_header=1,dtype=float,unpack=False)
nitrogenT6_ax219_data = np.genfromtxt(NitrogenT6_ax219_File, skip_header=1,dtype=float,unpack=False)
nitrogenT7_ax117_data = np.genfromtxt(NitrogenT7_ax117_File, skip_header=1,dtype=float,unpack=False)
nitrogenT7_ax219_data = np.genfromtxt(NitrogenT7_ax219_File, skip_header=1,dtype=float,unpack=False)

fig, ((ax1,ax2,ax3,ax4),(ax5,ax6,ax7,ax8) ,(ax9,ax10,ax11,ax12)) = plt.subplots(3,4,sharex = True)


#Plot Baseline structure for each Temperature
ax1.plot(NitrogenT4_data[:,0],NitrogenT4_data[:,1], c = 'g', label = 'O III 5007')
ax1.plot(NitrogenT4_data[:,0],NitrogenT4_data[:,4], c = 'r', label = 'N2 6584')
ax1.plot(NitrogenT4_data[:,0],NitrogenT4_data[:,9], c = 'b', label = 'S II 6720')
ax1.plot(NitrogenT4_data[:,0],NitrogenT4_data[:,2], c = 'y',label = 'O II 3727')
ax1.plot(NitrogenT4_data[:,0],NitrogenT4_data[:,3], c = 'black',label = 'O I 6200')
ax1.set_ylabel(r'$\alpha$x = 1.42')

ax2.plot(NitrogenT5_data[:,0],NitrogenT5_data[:,1], c = 'g')
ax2.plot(NitrogenT5_data[:,0],NitrogenT5_data[:,4], c = 'r')
ax2.plot(NitrogenT5_data[:,0],NitrogenT5_data[:,9], c = 'b')
ax2.plot(NitrogenT5_data[:,0],NitrogenT5_data[:,2], c = 'y')
ax2.plot(NitrogenT5_data[:,0],NitrogenT5_data[:,3], c = 'black')

ax3.plot(nitrogenT6_data[:,0],nitrogenT6_data[:,1], c = 'g')
ax3.plot(nitrogenT6_data[:,0],nitrogenT6_data[:,4], c = 'r')
ax3.plot(nitrogenT6_data[:,0],nitrogenT6_data[:,9], c = 'b')
ax3.plot(nitrogenT6_data[:,0],nitrogenT6_data[:,2], c = 'y')
ax3.plot(nitrogenT6_data[:,0],nitrogenT6_data[:,3], c = 'black')

ax4.plot(nitrogenT7_data[:,0],nitrogenT7_data[:,1], c = 'g')
ax4.plot(nitrogenT7_data[:,0],nitrogenT7_data[:,4], c = 'r')
ax4.plot(nitrogenT7_data[:,0],nitrogenT7_data[:,9], c = 'b')
ax4.plot(nitrogenT7_data[:,0],nitrogenT7_data[:,2], c = 'y')
ax4.plot(nitrogenT7_data[:,0],nitrogenT7_data[:,3], c = 'black')


#Plot ax = 117 Structure for each Temperature
ax5.plot(nitrogenT4_ax117_data[:,0],nitrogenT4_ax117_data[:,1], c = 'g')
ax5.plot(nitrogenT4_ax117_data[:,0],nitrogenT4_ax117_data[:,4], c = 'r')
ax5.plot(nitrogenT4_ax117_data[:,0],nitrogenT4_ax117_data[:,9], c = 'b')
ax5.plot(nitrogenT4_ax117_data[:,0],nitrogenT4_ax117_data[:,2], c = 'y')
ax5.plot(nitrogenT4_ax117_data[:,0],nitrogenT4_ax117_data[:,3], c = 'black')
ax5.set_ylabel(r'$\alpha$x = 1.17')

ax6.plot(nitrogenT5_ax117_data[:,0],nitrogenT5_ax117_data[:,1], c = 'g')
ax6.plot(nitrogenT5_ax117_data[:,0],nitrogenT5_ax117_data[:,4], c = 'r')
ax6.plot(nitrogenT5_ax117_data[:,0],nitrogenT5_ax117_data[:,9], c = 'b')
ax6.plot(nitrogenT5_ax117_data[:,0],nitrogenT5_ax117_data[:,2], c = 'y')
ax6.plot(nitrogenT5_ax117_data[:,0],nitrogenT5_ax117_data[:,3], c = 'black')

ax7.plot(nitrogenT6_ax117_data[:,0],nitrogenT6_ax117_data[:,1], c = 'g')
ax7.plot(nitrogenT6_ax117_data[:,0],nitrogenT6_ax117_data[:,4], c = 'r')
ax7.plot(nitrogenT6_ax117_data[:,0],nitrogenT6_ax117_data[:,9], c = 'b')
ax7.plot(nitrogenT6_ax117_data[:,0],nitrogenT6_ax117_data[:,2], c = 'y')
ax7.plot(nitrogenT6_ax117_data[:,0],nitrogenT6_ax117_data[:,3], c = 'black')

ax8.plot(nitrogenT7_ax117_data[:,0],nitrogenT7_ax117_data[:,1], c = 'g')
ax8.plot(nitrogenT7_ax117_data[:,0],nitrogenT7_ax117_data[:,4], c = 'r')
ax8.plot(nitrogenT7_ax117_data[:,0],nitrogenT7_ax117_data[:,9], c = 'b')
ax8.plot(nitrogenT7_ax117_data[:,0],nitrogenT7_ax117_data[:,2], c = 'y')
ax8.plot(nitrogenT7_ax117_data[:,0],nitrogenT7_ax117_data[:,3], c = 'black')

#Plot ax = 219 structure for each temperature 
ax9.plot(nitrogenT4_ax219_data[:,0],nitrogenT4_ax219_data[:,1], c = 'g')
ax9.plot(nitrogenT4_ax219_data[:,0],nitrogenT4_ax219_data[:,4], c = 'r')
ax9.plot(nitrogenT4_ax219_data[:,0],nitrogenT4_ax219_data[:,9], c = 'b')
ax9.plot(nitrogenT4_ax219_data[:,0],nitrogenT4_ax219_data[:,2], c = 'y')
ax9.plot(nitrogenT4_ax219_data[:,0],nitrogenT4_ax219_data[:,3], c = 'black')
ax9.set_ylabel(r'$\alpha$x = 2.19')
ax9.set_xlabel(r'$T_{bb} = 10^4$')

ax10.plot(nitrogenT5_ax219_data[:,0],nitrogenT5_ax219_data[:,1], c = 'g')
ax10.plot(nitrogenT5_ax219_data[:,0],nitrogenT5_ax219_data[:,4], c = 'r')
ax10.plot(nitrogenT5_ax219_data[:,0],nitrogenT5_ax219_data[:,9], c = 'b')
ax10.plot(nitrogenT5_ax219_data[:,0],nitrogenT5_ax219_data[:,2], c = 'y')
ax10.plot(nitrogenT5_ax219_data[:,0],nitrogenT5_ax219_data[:,3], c = 'black')
ax10.set_xlabel(r'$T_{bb} = 10^5$')

ax11.plot(nitrogenT6_ax219_data[:,0],nitrogenT6_ax219_data[:,1], c = 'g')
ax11.plot(nitrogenT6_ax219_data[:,0],nitrogenT6_ax219_data[:,4], c = 'r')
ax11.plot(nitrogenT6_ax219_data[:,0],nitrogenT6_ax219_data[:,9], c = 'b')
ax11.plot(nitrogenT6_ax219_data[:,0],nitrogenT6_ax219_data[:,2], c = 'y')
ax11.plot(nitrogenT6_ax219_data[:,0],nitrogenT6_ax219_data[:,3], c = 'black')
ax11.set_xlabel(r'$T_{bb} = 10^6$')

ax12.plot(nitrogenT7_ax219_data[:,0],nitrogenT7_ax219_data[:,1], c = 'g')
ax12.plot(nitrogenT7_ax219_data[:,0],nitrogenT7_ax219_data[:,4], c = 'r')
ax12.plot(nitrogenT7_ax219_data[:,0],nitrogenT7_ax219_data[:,9], c = 'b')
ax12.plot(nitrogenT7_ax219_data[:,0],nitrogenT7_ax219_data[:,2], c = 'y')
ax12.plot(nitrogenT7_ax219_data[:,0],nitrogenT7_ax219_data[:,3], c = 'black')
ax12.set_xlabel(r'$T_{bb} = 10^7$')

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

fig.text(0.5,0.04, 'Depth (cm)')
fig.text(0.06,0.5, 'Emissivity', ha = 'center', va = 'center', rotation = 'vertical')
plt.suptitle('Emissivities of Standard Diagnostic Elements')
ax1.legend()
plt.show()


