#Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


#import our data
OxygenT4_ax117_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T4/Linear_fit/ax117/Ionization_35/Ionization_35_Linear_Fit_ax117_SEDT4_oxygen.txt'
OxygenT4_ax219_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T4/Linear_fit/ax219/Ionization_35/Ionization_35_Linear_Fit_ax219_SEDT4_oxygen.txt' 
OxygenT4_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T4/Baseline/Ionization35/Ionization_35_SEDT4_oxygen.txt'
OxygenT5_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T5/Baseline/Ionization35/Ionization_35_SEDT5_oxygen.txt'
oxygenT6_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T6/Baseline/Ionization_35/Ionization_35_SEDT6_Oxygen.txt'
oxygenT7_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T7/Baseline/Ionization_35/Ionization_35_SEDT7_Oxygen.txt'
oxygenT5_ax117_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T5/Linear_fit/ax117/Ionization_35/Ionization_35_Linear_Fit_ax117_SEDT5_oxygen.txt'
oxygenT5_ax219_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T5/Linear_fit/ax219/Ionization_35/Ionization_35_Linear_Fit_ax219_SEDT5_oxygen.txt'
oxygenT6_ax117_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T6/Linear_fit/ax117/Ionization_35/Ionization_35_Linear_Fit_ax117_SEDT6_oxygen.txt'
oxygenT6_ax219_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T6/Linear_fit/ax219/Ionization_35/Ionization_35_Linear_Fit_ax219_SEDT6_oxygen.txt'
oxygenT7_ax117_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T7/Linear_fit/ax117/Ionization_35/Ionization_35_Linear_Fit_ax117_SEDT7_oxygen.txt'
oxygenT7_ax219_File = '/Users/compastro/greene/AGN_SED/cloudy_data/AGN_T7/Linear_fit/ax219/Ionization_35/Ionization_35_Linear_Fit_ax219_SEDT7_oxygen.txt'

oxygenT4_data = np.genfromtxt(OxygenT4_File, skip_header=1,dtype=float,unpack=False)
oxygenT5_data=np.genfromtxt(OxygenT5_File, skip_header=1,dtype=float,unpack=False)
oxygenT6_data = np.genfromtxt(oxygenT6_File, skip_header=1,dtype=float,unpack=False)
oxygenT7_data = np.genfromtxt(oxygenT7_File, skip_header=1,dtype=float,unpack=False)
oxygenT4_ax117_data = np.genfromtxt(OxygenT4_ax117_File, skip_header=1,dtype=float,unpack=False)
oxygenT4_ax219_data = np.genfromtxt(OxygenT4_ax219_File, skip_header=1,dtype=float,unpack=False)
oxygenT5_ax117_data = np.genfromtxt(oxygenT5_ax117_File, skip_header=1,dtype=float,unpack=False)
oxygenT5_ax219_data = np.genfromtxt(oxygenT5_ax219_File, skip_header=1,dtype=float,unpack=False)
oxygenT6_ax117_data = np.genfromtxt(oxygenT6_ax117_File, skip_header=1,dtype=float,unpack=False)
oxygenT6_ax219_data = np.genfromtxt(oxygenT6_ax219_File, skip_header=1,dtype=float,unpack=False)
oxygenT7_ax117_data = np.genfromtxt(oxygenT7_ax117_File, skip_header=1,dtype=float,unpack=False)
oxygenT7_ax219_data = np.genfromtxt(oxygenT7_ax219_File, skip_header=1,dtype=float,unpack=False)

fig, ((ax1,ax2,ax3,ax4),(ax5,ax6,ax7,ax8) ,(ax9,ax10,ax11,ax12)) = plt.subplots(3,4,sharex = True)

#Plot Baseline structure for each Temperature
ax1.scatter(oxygenT4_data[:,0],oxygenT4_data[:,1], c = 'g',edgecolor = '')
ax1.scatter(oxygenT4_data[:,0],oxygenT4_data[:,2], c = 'r',edgecolor = '')
ax1.scatter(oxygenT4_data[:,0],oxygenT4_data[:,3], c = 'b',edgecolor = '')
ax1.set_ylabel('Baseline SED')
ax2.scatter(oxygenT5_data[:,0],oxygenT5_data[:,1], c = 'g',edgecolor = '')
ax2.scatter(oxygenT5_data[:,0],oxygenT5_data[:,2], c = 'r',edgecolor = '')
ax2.scatter(oxygenT5_data[:,0],oxygenT5_data[:,3], c = 'b',edgecolor = '')

ax3.scatter(oxygenT6_data[:,0],oxygenT6_data[:,1], c = 'g',edgecolor = '')
ax3.scatter(oxygenT6_data[:,0],oxygenT6_data[:,2], c = 'r',edgecolor = '')
ax3.scatter(oxygenT6_data[:,0],oxygenT6_data[:,3], c = 'b',edgecolor = '')

ax4.scatter(oxygenT7_data[:,0],oxygenT7_data[:,1], c = 'g',edgecolor = '')
ax4.scatter(oxygenT7_data[:,0],oxygenT7_data[:,2], c = 'r',edgecolor = '')
ax4.scatter(oxygenT7_data[:,0],oxygenT7_data[:,3], c = 'b',edgecolor = '')

#Plot ax = 117 Structure for each Temperature
ax5.scatter(oxygenT4_ax117_data[:,0],oxygenT4_ax117_data[:,1], c = 'g',edgecolor = '')
ax5.scatter(oxygenT4_ax117_data[:,0],oxygenT4_ax117_data[:,2], c = 'r',edgecolor = '')
ax5.scatter(oxygenT4_ax117_data[:,0],oxygenT4_ax117_data[:,3], c = 'b',edgecolor = '')
ax5.set_ylabel(r'$\alpha$x = 1.17')
ax6.scatter(oxygenT5_ax117_data[:,0],oxygenT5_ax117_data[:,1], c = 'g',edgecolor = '')
ax6.scatter(oxygenT5_ax117_data[:,0],oxygenT5_ax117_data[:,2], c = 'r',edgecolor = '')
ax6.scatter(oxygenT5_ax117_data[:,0],oxygenT5_ax117_data[:,3], c = 'b',edgecolor = '')

ax7.scatter(oxygenT6_ax117_data[:,0],oxygenT6_ax117_data[:,1], c = 'g',edgecolor = '')
ax7.scatter(oxygenT6_ax117_data[:,0],oxygenT6_ax117_data[:,2], c = 'r',edgecolor = '')
ax7.scatter(oxygenT6_ax117_data[:,0],oxygenT6_ax117_data[:,3], c = 'b',edgecolor = '')

ax8.scatter(oxygenT7_ax117_data[:,0],oxygenT7_ax117_data[:,1], c = 'g',edgecolor = '')
ax8.scatter(oxygenT7_ax117_data[:,0],oxygenT7_ax117_data[:,2], c = 'r',edgecolor = '')
ax8.scatter(oxygenT7_ax117_data[:,0],oxygenT7_ax117_data[:,3], c = 'b',edgecolor = '')

#Plot ax = 219 structure for each temperature 
ax9.scatter(oxygenT4_ax219_data[:,0],oxygenT4_ax219_data[:,1], c = 'g',edgecolor = '')
ax9.scatter(oxygenT4_ax219_data[:,0],oxygenT4_ax219_data[:,2], c = 'r',edgecolor = '')
ax9.scatter(oxygenT4_ax219_data[:,0],oxygenT4_ax219_data[:,3], c = 'b',edgecolor = '')
ax9.set_ylabel(r'$\alpha$x = 1.17')
ax10.scatter(oxygenT5_ax219_data[:,0],oxygenT5_ax219_data[:,1], c = 'g',edgecolor = '')
ax10.scatter(oxygenT5_ax219_data[:,0],oxygenT5_ax219_data[:,2], c = 'r',edgecolor = '')
ax10.scatter(oxygenT5_ax219_data[:,0],oxygenT5_ax219_data[:,3], c = 'b',edgecolor = '')

ax11.scatter(oxygenT6_ax219_data[:,0],oxygenT6_ax219_data[:,1], c = 'g',edgecolor = '')
ax11.scatter(oxygenT6_ax219_data[:,0],oxygenT6_ax219_data[:,2], c = 'r',edgecolor = '')
ax11.scatter(oxygenT6_ax219_data[:,0],oxygenT6_ax219_data[:,3], c = 'b',edgecolor = '')

ax12.scatter(oxygenT7_ax219_data[:,0],oxygenT7_ax219_data[:,1], c = 'g',edgecolor = '')
ax12.scatter(oxygenT7_ax219_data[:,0],oxygenT7_ax219_data[:,2], c = 'r',edgecolor = '')
ax12.scatter(oxygenT7_ax219_data[:,0],oxygenT7_ax219_data[:,3], c = 'b',edgecolor = '')


figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

fig.text(0.5,0.04, 'Depth (cm)')
fig.text(0.06,0.5, 'Ionization Fraction', ha = 'center', va = 'center', rotation = 'vertical')
plt.suptitle(r'Ionization Structure for Oxygen from T = $10^4$ to T = $10^7$')
plt.show()

