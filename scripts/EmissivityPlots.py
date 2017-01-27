# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 12:39:07 2016

@author: chris_000
"""

#Import required modules
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


#import our data
NitrogenT4_ax117_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT4_lines.str'
NitrogenT4_ax219_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT4_lines.str' 
NitrogenT4_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Baseline\Ionization35\Ionization_35_SEDT4_lines.str'
NitrogenT5_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Baseline\Ionization35\Ionization_35_SEDT5_lines.str'
NitrogenT6_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Baseline\Ionization_35\Ionization_35_SEDT6lines.str'
NitrogenT7_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Baseline\Ionization_35\Ionization_35_SEDT7_lines.str'
NitrogenT5_ax117_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT5_lines.str'
NitrogenT5_ax219_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT5_lines.str'
NitrogenT6_ax117_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT6_lines.str'
NitrogenT6_ax219_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT6_lines.str'
NitrogenT7_ax117_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT7_lines.str'
NitrogenT7_ax219_File = r'C:\Users\chris\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT7_lines.str'


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

fig, ((ax1,ax2,ax3,ax4),(ax5,ax6,ax7,ax8) ,(ax9,ax10,ax11,ax12)) = plt.subplots(3,4,sharex = True,sharey = True,figsize = (20,10))

plt.subplots_adjust(wspace = 0, hspace = 0)

#Plot Baseline structure for each Temperature
ax5.plot(NitrogenT4_data[:,0],np.divide(10**NitrogenT4_data[:,1],10**np.amax(NitrogenT4_data[:,1])), c = 'b', ls = '-.', label = 'O III 5007')
ax5.plot(NitrogenT4_data[:,0],np.divide(10**NitrogenT4_data[:,4],10**np.amax(NitrogenT4_data[:,4])), c = 'r', ls = '--', label = 'N II 6584')
ax5.plot(NitrogenT4_data[:,0],np.divide(10**NitrogenT4_data[:,9],10**np.amax(NitrogenT4_data[:,9])), c = 'g',ls = '--', label = 'S II 6720')
ax5.plot(NitrogenT4_data[:,0],np.divide(10**NitrogenT4_data[:,2],10**np.amax(NitrogenT4_data[:,2])), c = 'b',ls = '--',label = 'O II 3727')
ax5.plot(NitrogenT4_data[:,0],np.divide(10**NitrogenT4_data[:,3],10**np.amax(NitrogenT4_data[:,3])), c = 'b',label = 'O I 6300')
ax5.plot(NitrogenT4_data[:,0], np.divide(10**NitrogenT4_data[:,8],10**np.amax(NitrogenT4_data[:,8])),c = 'r', label = 'N I 5200')
ax5.set_ylabel(r'$\alpha_x$ = 1.42',fontsize = 20)
ax1.set_title(r'$T_{bb}=10^4$',fontsize = 20)

ax6.plot(NitrogenT5_data[:,0],10**NitrogenT5_data[:,1]/10**np.amax(NitrogenT5_data[:,1]), c = 'b',ls = '-.')
ax6.plot(NitrogenT5_data[:,0],10**NitrogenT5_data[:,4]/10**np.amax(NitrogenT5_data[:,4]), c = 'r',ls = '--')
ax6.plot(NitrogenT5_data[:,0],10**NitrogenT5_data[:,9]/10**np.amax(NitrogenT5_data[:,9]), c = 'g',ls = '--')
ax6.plot(NitrogenT5_data[:,0],10**NitrogenT5_data[:,2]/10**np.amax(NitrogenT5_data[:,2]), c = 'b',ls = '--')
ax6.plot(NitrogenT5_data[:,0],10**NitrogenT5_data[:,3]/10**np.amax(NitrogenT5_data[:,3]), c = 'b')
ax6.plot(NitrogenT5_data[:,0], 10**NitrogenT5_data[:,8]/10**np.amax(NitrogenT5_data[:,8]),c = 'r', label = 'N I 5200')
ax2.set_title(r'$T_{bb}=10^5$',fontsize = 20)

ax7.plot(nitrogenT6_data[:,0],10**nitrogenT6_data[:,2]/10**np.amax(nitrogenT6_data[:,2]), c = 'b',ls = '-.')
ax7.plot(nitrogenT6_data[:,0],10**nitrogenT6_data[:,5]/10**np.amax(nitrogenT6_data[:,5]), c = 'r',ls = '--')
ax7.plot(nitrogenT6_data[:,0],10**nitrogenT6_data[:,10]/10**np.amax(nitrogenT6_data[:,10]), c = 'g',ls = '--')
ax7.plot(nitrogenT6_data[:,0],10**nitrogenT6_data[:,3]/10**np.amax(nitrogenT6_data[:,3]), c = 'b',ls = '--',)
ax7.plot(nitrogenT6_data[:,0],np.divide(10**nitrogenT6_data[:,4],10**np.amax(nitrogenT6_data[:,4])), c = 'b')
ax7.plot(nitrogenT6_data[:,0],10**nitrogenT6_data[:,9]/10**np.amax(nitrogenT6_data[:,9]),c = 'r', label = 'N I 5200')
ax3.set_title(r'$T_{bb}=10^6$',fontsize = 20)

ax8.plot(nitrogenT7_data[:,0],10**nitrogenT7_data[:,1]/10**np.amax(nitrogenT7_data[:,1]), c = 'b',ls = '-.')
ax8.plot(nitrogenT7_data[:,0],10**nitrogenT7_data[:,4]/10**np.amax(nitrogenT7_data[:,4]), c = 'r',ls = '--')
ax8.plot(nitrogenT7_data[:,0],10**nitrogenT7_data[:,9]/10**np.amax(nitrogenT7_data[:,9]), c = 'g',ls = '--')
ax8.plot(nitrogenT7_data[:,0],10**nitrogenT7_data[:,2]/10**np.amax(nitrogenT7_data[:,2]), c = 'b',ls = '--')
ax8.plot(nitrogenT7_data[:,0],10**nitrogenT7_data[:,3]/10**np.amax(nitrogenT7_data[:,3]), c = 'b')
ax8.plot(nitrogenT7_data[:,0], 10**nitrogenT7_data[:,8]/10**np.amax(nitrogenT7_data[:,4]),c = 'r',label = 'N I 5200')
ax4.set_title(r'$T_{bb}=10^7$',fontsize = 20)
##Plot ax = 117 Structure for each Temperature
ax1.plot(nitrogenT4_ax117_data[:,0],10**nitrogenT4_ax117_data[:,1]/10**np.amax(nitrogenT4_ax117_data[:,1]), c = 'b',ls = '-.',label = 'O III 5007')
ax1.plot(nitrogenT4_ax117_data[:,0],10**nitrogenT4_ax117_data[:,4]/10**np.amax(nitrogenT4_ax117_data[:,4]), c = 'r',ls = '--', label ='N2 6584')
ax1.plot(nitrogenT4_ax117_data[:,0],10**nitrogenT4_ax117_data[:,9]/10**np.amax(nitrogenT4_ax117_data[:,9]), c = 'g',ls = '--', label = 'S II 6720' )
ax1.plot(nitrogenT4_ax117_data[:,0],10**nitrogenT4_ax117_data[:,2]/10**np.amax(nitrogenT4_ax117_data[:,2]), c = 'b',ls = '--',label = 'O II 3727')
ax1.plot(nitrogenT4_ax117_data[:,0],10**nitrogenT4_ax117_data[:,3]/10**np.amax(nitrogenT4_ax117_data[:,3]), c = 'b' ,label = 'O I 6300')
ax1.plot(nitrogenT4_ax117_data[:,0],10**nitrogenT4_ax117_data[:,8]/10**np.amax(nitrogenT4_ax117_data[:,8]), c = 'r',label = 'N I 5200')
ax1.set_ylabel(r'$\alpha_x$ = 1.17',fontsize = 20)

ax2.plot(nitrogenT5_ax117_data[:,0],10**nitrogenT5_ax117_data[:,1]/10**np.amax(nitrogenT5_ax117_data[:,1]), c = 'b',ls = '-.')
ax2.plot(nitrogenT5_ax117_data[:,0],10**nitrogenT5_ax117_data[:,4]/10**np.amax(nitrogenT5_ax117_data[:,4]), c = 'r',ls = '--')
ax2.plot(nitrogenT5_ax117_data[:,0],10**nitrogenT5_ax117_data[:,9]/10**np.amax(nitrogenT5_ax117_data[:,9]), c = 'g',ls = '--')
ax2.plot(nitrogenT5_ax117_data[:,0],10**nitrogenT5_ax117_data[:,2]/10**np.amax(nitrogenT5_ax117_data[:,2]), c = 'b',ls = '--')
ax2.plot(nitrogenT5_ax117_data[:,0],10**nitrogenT5_ax117_data[:,3]/10**np.amax(nitrogenT5_ax117_data[:,3]), c = 'b')
ax2.plot(nitrogenT5_ax117_data[:,0],10**nitrogenT5_ax117_data[:,8]/10**np.amax(nitrogenT5_ax117_data[:,8]), c = 'r')

ax3.plot(nitrogenT6_ax117_data[:,0],10**nitrogenT6_ax117_data[:,1]/10**np.amax(nitrogenT6_ax117_data[:,1]), c = 'b',ls = '-.')
ax3.plot(nitrogenT6_ax117_data[:,0],10**nitrogenT6_ax117_data[:,4]/10**np.amax(nitrogenT6_ax117_data[:,4]), c = 'r',ls = '--')
ax3.plot(nitrogenT6_ax117_data[:,0],10**nitrogenT6_ax117_data[:,9]/10**np.amax(nitrogenT6_ax117_data[:,9]), c = 'g',ls = '--')
ax3.plot(nitrogenT6_ax117_data[:,0],10**nitrogenT6_ax117_data[:,2]/10**np.amax(nitrogenT6_ax117_data[:,2]), c = 'b',ls = '--')
ax3.plot(nitrogenT6_ax117_data[:,0],10**nitrogenT6_ax117_data[:,3]/10**np.amax(nitrogenT6_ax117_data[:,3]), c = 'b')
ax3.plot(nitrogenT6_ax117_data[:,0],10**nitrogenT6_ax117_data[:,8]/10**np.amax(nitrogenT6_ax117_data[:,8]), c = 'r')

ax4.plot(nitrogenT7_ax117_data[:,0],10**nitrogenT7_ax117_data[:,1]/10**np.amax(nitrogenT7_ax117_data[:,1]), c = 'b',ls = '-.')
ax4.plot(nitrogenT7_ax117_data[:,0],10**nitrogenT7_ax117_data[:,4]/10**np.amax(nitrogenT7_ax117_data[:,4]), c = 'r',ls = '--')
ax4.plot(nitrogenT7_ax117_data[:,0],10**nitrogenT7_ax117_data[:,9]/10**np.amax(nitrogenT7_ax117_data[:,9]), c = 'g',ls = '--')
ax4.plot(nitrogenT7_ax117_data[:,0],10**nitrogenT7_ax117_data[:,2]/10**np.amax(nitrogenT7_ax117_data[:,2]), c = 'b',ls = '--')
ax4.plot(nitrogenT7_ax117_data[:,0],10**nitrogenT7_ax117_data[:,3]/10**np.amax(nitrogenT7_ax117_data[:,3]), c = 'b')
ax4.plot(nitrogenT7_ax117_data[:,0],10**nitrogenT7_ax117_data[:,8]/10**np.amax(nitrogenT7_ax117_data[:,8]), c = 'r')
#Plot ax = 219 structure for each temperature 
ax9.plot(nitrogenT4_ax219_data[:,0],10**nitrogenT4_ax219_data[:,1]/10**np.amax(nitrogenT4_ax219_data[:,1]), c = 'b',ls = '-.')
ax9.plot(nitrogenT4_ax219_data[:,0],10**nitrogenT4_ax219_data[:,4]/10**np.amax(nitrogenT4_ax219_data[:,4]), c = 'r',ls = '--')
ax9.plot(nitrogenT4_ax219_data[:,0],10**nitrogenT4_ax219_data[:,9]/10**np.amax(nitrogenT4_ax219_data[:,9]), c = 'g',ls = '--')
ax9.plot(nitrogenT4_ax219_data[:,0],10**nitrogenT4_ax219_data[:,2]/10**np.amax(nitrogenT4_ax219_data[:,2]), c = 'b',ls = '--')
ax9.plot(nitrogenT4_ax219_data[:,0],10**nitrogenT4_ax219_data[:,3]/10**np.amax(nitrogenT4_ax219_data[:,3]), c = 'b')
ax9.plot(nitrogenT4_ax219_data[:,0],10**nitrogenT4_ax219_data[:,8]/10**np.amax(nitrogenT4_ax219_data[:,8]), c = 'r')

ax9.set_ylabel(r'$\alpha_x$ = 2.19',fontsize = 20)
#ax9.set_xlabel(r'$T_{bb} = 10^4$')

ax10.plot(nitrogenT5_ax219_data[:,0],10**nitrogenT5_ax219_data[:,1]/10**np.amax(nitrogenT5_ax219_data[:,1]), c = 'b',ls = '-.')
ax10.plot(nitrogenT5_ax219_data[:,0],10**nitrogenT5_ax219_data[:,4]/10**np.amax(nitrogenT5_ax219_data[:,4]), c = 'r',ls = '--')
ax10.plot(nitrogenT5_ax219_data[:,0],10**nitrogenT5_ax219_data[:,9]/10**np.amax(nitrogenT5_ax219_data[:,9]), c = 'g',ls = '--')
ax10.plot(nitrogenT5_ax219_data[:,0],10**nitrogenT5_ax219_data[:,2]/10**np.amax(nitrogenT5_ax219_data[:,2]), c = 'b',ls = '--')
ax10.plot(nitrogenT5_ax219_data[:,0],10**nitrogenT5_ax219_data[:,3]/10**np.amax(nitrogenT5_ax219_data[:,3]), c = 'b')
ax10.plot(nitrogenT5_ax219_data[:,0],10**nitrogenT5_ax219_data[:,8]/10**np.amax(nitrogenT5_ax219_data[:,8]), c = 'r')

#ax10.set_xlabel(r'$T_{bb} = 10^5$')

ax11.plot(nitrogenT6_ax219_data[:,0],10**nitrogenT6_ax219_data[:,1]/10**np.amax(nitrogenT6_ax219_data[:,1]), c = 'b',ls = '-.')
ax11.plot(nitrogenT6_ax219_data[:,0],10**nitrogenT6_ax219_data[:,4]/10**np.amax(nitrogenT6_ax219_data[:,4]), c = 'r',ls = '--')
ax11.plot(nitrogenT6_ax219_data[:,0],10**nitrogenT6_ax219_data[:,9]/10**np.amax(nitrogenT6_ax219_data[:,9]), c = 'g',ls = '--')
ax11.plot(nitrogenT6_ax219_data[:,0],10**nitrogenT6_ax219_data[:,2]/10**np.amax(nitrogenT6_ax219_data[:,2]), c = 'b',ls = '--')
ax11.plot(nitrogenT6_ax219_data[:,0],10**nitrogenT6_ax219_data[:,3]/10**np.amax(nitrogenT6_ax219_data[:,3]), c = 'b')
ax11.plot(nitrogenT6_ax219_data[:,0],10**nitrogenT6_ax219_data[:,8]/10**np.amax(nitrogenT6_ax219_data[:,8]), c = 'r')

#ax11.set_xlabel(r'$T_{bb} = 10^6$')

ax12.plot(nitrogenT7_ax219_data[:,0],10**nitrogenT7_ax219_data[:,1]/10**np.amax(nitrogenT7_ax219_data[:,1]), c = 'b',ls = '-.')
ax12.plot(nitrogenT7_ax219_data[:,0],10**nitrogenT7_ax219_data[:,4]/10**np.amax(nitrogenT7_ax219_data[:,4]), c = 'r',ls = '--')
ax12.plot(nitrogenT7_ax219_data[:,0],10**nitrogenT7_ax219_data[:,9]/10**np.amax(nitrogenT7_ax219_data[:,9]), c = 'g',ls = '--')
ax12.plot(nitrogenT7_ax219_data[:,0],10**nitrogenT7_ax219_data[:,2]/10**np.amax(nitrogenT7_ax219_data[:,2]), c = 'b',ls = '--')
ax12.plot(nitrogenT7_ax219_data[:,0],10**nitrogenT7_ax219_data[:,3]/10**np.amax(nitrogenT7_ax219_data[:,3]), c = 'b')
ax12.plot(nitrogenT7_ax219_data[:,0],10**nitrogenT7_ax219_data[:,8]/10**np.amax(nitrogenT7_ax219_data[:,8]), c = 'r')

#ax12.set_xlabel(r'$T_{bb} = 10^7$')

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.gca().xaxis.set_major_locator(MaxNLocator(prune='upper'))
plt.gca().yaxis.set_major_locator(MaxNLocator(prune='upper'))
fig.text(0.5,0.04, 'Depth (cm)',fontsize = 22)
fig.text(0.06,0.5, 'Emissivity', ha = 'center', va = 'center', rotation = 'vertical',fontsize = 22)

plt.suptitle('Emissivities of Standard Diagnostic Elements', fontsize = 22)
ax1.legend()
plt.show()
plt.savefig(r'C:\Users\chris\Documents\GitHub\AGN_SED\Presentations\Emissivities.png', format='png', dpi=1000)

