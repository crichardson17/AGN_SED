#Import required modules
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


#import our data
NitrogenT4_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT4_sulfer.txt'
NitrogenT4_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT4_sulfer.txt' 
NitrogenT4_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Baseline\Ionization35\Ionization_35_SEDT4_sulfer.txt'
NitrogenT5_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Baseline\Ionization35\Ionization_35_SEDT5_sulfer.txt'
NitrogenT6_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Baseline\Ionization_35\Ionization_35_SEDT6_Sulfur.txt'
NitrogenT7_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Baseline\Ionization_35\Ionization_35_SEDT7_sulfer.txt'
NitrogenT5_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT5_sulfer.txt'
NitrogenT5_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT5_sulfer.txt'
NitrogenT6_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT6_sulfer.txt'
NitrogenT6_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT6_sulfer.txt'
NitrogenT7_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT7_sulfer.txt'
NitrogenT7_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT7_sulfer.txt'
OxygenT4_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT4_oxygen.txt' 
OxygenT4_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT4_oxygen.txt'
OxygenT4_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T4\Baseline\Ionization35\Ionization_35_SEDT4_oxygen.txt'
OxygenT5_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Baseline\Ionization35\Ionization_35_SEDT5_oxygen.txt'
OxygenT6_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Baseline\Ionization_35\Ionization_35_SEDT6_Oxygen.txt'
OxygenT7_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Baseline\Ionization_35\Ionization_35_SEDT7_oxygen.txt'
OxygenT5_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT5_oxygen.txt'
OxygenT5_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T5\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT5_oxygen.txt'
OxygenT6_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT6_oxygen.txt'
OxygenT6_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T6\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT6_oxygen.txt'
OxygenT7_ax117_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Linear_fit\ax117\Ionization_35\Ionization_35_Linear_Fit_ax117_SEDT7_oxygen.txt'
OxygenT7_ax219_File = r'C:\Users\chris_000\Documents\GitHub\AGN_SED\cloudy_data\AGN_T7\Linear_fit\ax219\Ionization_35\Ionization_35_Linear_Fit_ax219_SEDT7_oxygen.txt'

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
oxygenT4_data = np.genfromtxt(OxygenT4_File, skip_header=1,dtype=float,unpack=False)
oxygenT5_data=np.genfromtxt(OxygenT5_File, skip_header=1,dtype=float,unpack=False)
oxygenT6_data = np.genfromtxt(OxygenT6_File, skip_header=1,dtype=float,unpack=False)
oxygenT7_data = np.genfromtxt(OxygenT7_File, skip_header=1,dtype=float,unpack=False)
oxygenT4_ax117_data = np.genfromtxt(OxygenT4_ax117_File, skip_header=1,dtype=float,unpack=False)
oxygenT4_ax219_data = np.genfromtxt(OxygenT4_ax219_File, skip_header=1,dtype=float,unpack=False)
oxygenT5_ax117_data = np.genfromtxt(OxygenT5_ax117_File, skip_header=1,dtype=float,unpack=False)
oxygenT5_ax219_data = np.genfromtxt(OxygenT5_ax219_File, skip_header=1,dtype=float,unpack=False)
oxygenT6_ax117_data = np.genfromtxt(OxygenT6_ax117_File, skip_header=1,dtype=float,unpack=False)
oxygenT6_ax219_data = np.genfromtxt(OxygenT6_ax219_File, skip_header=1,dtype=float,unpack=False)
oxygenT7_ax117_data = np.genfromtxt(OxygenT7_ax117_File, skip_header=1,dtype=float,unpack=False)
oxygenT7_ax219_data = np.genfromtxt(OxygenT7_ax219_File, skip_header=1,dtype=float,unpack=False)


fig, ((ax1,ax2,ax3,ax4),(ax5,ax6,ax7,ax8) ,(ax9,ax10,ax11,ax12)) = plt.subplots(3,4,sharex = True,sharey=True)

plt.subplots_adjust(hspace=0, wspace = 0)


#Plot Baseline structure for each Temperature
ax5.plot(NitrogenT4_data[:,0],NitrogenT4_data[:,1], c = 'g',label = 'S I')
ax5.plot(NitrogenT4_data[:,0],NitrogenT4_data[:,2], c = 'r',label = 'S II' )
ax5.plot(NitrogenT4_data[:,0],NitrogenT4_data[:,3], c = 'b', label = 'S III')
ax5.plot(oxygenT4_data[:,0],oxygenT4_data[:,1], c = 'g', ls = '--', label = 'O I')
ax5.plot(oxygenT4_data[:,0], oxygenT4_data[:,2],c = 'r', ls = '--', label = 'O II')
ax5.plot(oxygenT4_data[:,0], oxygenT4_data[:,3],c = 'b', ls = '--', label = 'O III')
ax5.set_ylabel(r'$\alpha_x$ = 1.42',fontsize = 18)
ax1.set_title(r'$T_{bb}=10^4$',fontsize = 18)

ax6.plot(NitrogenT5_data[:,0],NitrogenT5_data[:,1], c = 'g')
ax6.plot(NitrogenT5_data[:,0],NitrogenT5_data[:,2], c = 'r')
ax6.plot(NitrogenT5_data[:,0],NitrogenT5_data[:,3], c = 'b')
ax6.plot(oxygenT5_data[:,0],oxygenT5_data[:,1], c = 'g', ls = '--', label = 'O I')
ax6.plot(oxygenT5_data[:,0], oxygenT5_data[:,2],c = 'r', ls = '--', label = 'O II')
ax6.plot(oxygenT5_data[:,0], oxygenT5_data[:,3],c = 'b', ls = '--', label = 'O III')

ax2.set_title(r'$T_{bb}=10^5$',fontsize = 18)

ax7.plot(nitrogenT6_data[:,0],nitrogenT6_data[:,1], c = 'g')
ax7.plot(nitrogenT6_data[:,0],nitrogenT6_data[:,2], c = 'r')
ax7.plot(nitrogenT6_data[:,0],nitrogenT6_data[:,3], c = 'b')
ax7.plot(oxygenT6_data[:,0],oxygenT6_data[:,1], c = 'g', ls = '--', label = 'O I')
ax7.plot(oxygenT6_data[:,0], oxygenT6_data[:,2],c = 'r', ls = '--', label = 'O II')
ax7.plot(oxygenT6_data[:,0], oxygenT6_data[:,3],c = 'b', ls = '--', label = 'O III')

ax3.set_title(r'$T_{bb}=10^6$',fontsize = 18)

ax8.plot(nitrogenT7_data[:,0],nitrogenT7_data[:,1], c = 'g')
ax8.plot(nitrogenT7_data[:,0],nitrogenT7_data[:,2], c = 'r')
ax8.plot(nitrogenT7_data[:,0],nitrogenT7_data[:,3], c = 'b')
ax8.plot(oxygenT7_data[:,0],oxygenT7_data[:,1], c = 'g', ls = '--', label = 'O I')
ax8.plot(oxygenT7_data[:,0], oxygenT7_data[:,2],c = 'r', ls = '--', label = 'O II')
ax8.plot(oxygenT7_data[:,0], oxygenT7_data[:,3],c = 'b', ls = '--', label = 'O III')

ax4.set_title(r'$T_{bb}=10^7$',fontsize = 18)

#Plot ax = 117 Structure for each Temperature
ax1.plot(nitrogenT4_ax117_data[:,0],nitrogenT4_ax117_data[:,1], c = 'g',label = 'S I')
ax1.plot(nitrogenT4_ax117_data[:,0],nitrogenT4_ax117_data[:,2], c = 'r',label = 'S II')
ax1.plot(nitrogenT4_ax117_data[:,0],nitrogenT4_ax117_data[:,3], c = 'b',label = 'S III')
ax1.plot(oxygenT4_ax117_data[:,0],oxygenT4_ax117_data[:,1], c = 'g', ls = '--', label = 'O I')
ax1.plot(oxygenT4_ax117_data[:,0], oxygenT4_ax117_data[:,2],c = 'r', ls = '--', label = 'O II')
ax1.plot(oxygenT4_ax117_data[:,0], oxygenT4_ax117_data[:,3],c = 'b', ls = '--', label = 'O III')
ax1.set_ylabel(r'$\alpha_x$ = 1.17',fontsize = 18)

ax2.plot(nitrogenT5_ax117_data[:,0],nitrogenT5_ax117_data[:,1], c = 'g')
ax2.plot(nitrogenT5_ax117_data[:,0],nitrogenT5_ax117_data[:,2], c = 'r')
ax2.plot(nitrogenT5_ax117_data[:,0],nitrogenT5_ax117_data[:,3], c = 'b')
ax2.plot(oxygenT5_ax117_data[:,0],oxygenT5_ax117_data[:,1], c = 'g', ls = '--', label = 'O I')
ax2.plot(oxygenT5_ax117_data[:,0], oxygenT5_ax117_data[:,2],c = 'r', ls = '--', label = 'O II')
ax2.plot(oxygenT5_ax117_data[:,0], oxygenT5_ax117_data[:,3],c = 'b', ls = '--', label = 'O III')


ax3.plot(nitrogenT6_ax117_data[:,0],nitrogenT6_ax117_data[:,1], c = 'g')
ax3.plot(nitrogenT6_ax117_data[:,0],nitrogenT6_ax117_data[:,2], c = 'r')
ax3.plot(nitrogenT6_ax117_data[:,0],nitrogenT6_ax117_data[:,3], c = 'b')
ax3.plot(oxygenT6_ax117_data[:,0],oxygenT6_ax117_data[:,1], c = 'g', ls = '--', label = 'O I')
ax3.plot(oxygenT6_ax117_data[:,0], oxygenT6_ax117_data[:,2],c = 'r', ls = '--', label = 'O II')
ax3.plot(oxygenT6_ax117_data[:,0], oxygenT6_ax117_data[:,3],c = 'b', ls = '--', label = 'O III')


ax4.plot(nitrogenT7_ax117_data[:,0],nitrogenT7_ax117_data[:,1], c = 'g')
ax4.plot(nitrogenT7_ax117_data[:,0],nitrogenT7_ax117_data[:,2], c = 'r')
ax4.plot(nitrogenT7_ax117_data[:,0],nitrogenT7_ax117_data[:,3], c = 'b')
ax4.plot(oxygenT7_ax117_data[:,0],oxygenT7_ax117_data[:,1], c = 'g', ls = '--', label = 'O I')
ax4.plot(oxygenT7_ax117_data[:,0], oxygenT7_ax117_data[:,2],c = 'r', ls = '--', label = 'O II')
ax4.plot(oxygenT7_ax117_data[:,0], oxygenT7_ax117_data[:,3],c = 'b', ls = '--', label = 'O III')


#Plot ax = 219 structure for each temperature 
ax9.plot(nitrogenT4_ax219_data[:,0],nitrogenT4_ax219_data[:,1], c = 'g')
ax9.plot(nitrogenT4_ax219_data[:,0],nitrogenT4_ax219_data[:,2], c = 'r')
ax9.plot(nitrogenT4_ax219_data[:,0],nitrogenT4_ax219_data[:,3], c = 'b')
ax9.plot(oxygenT4_ax219_data[:,0],oxygenT4_ax219_data[:,1], c = 'g', ls = '--', label = 'O I')
ax9.plot(oxygenT4_ax219_data[:,0], oxygenT4_ax219_data[:,2],c = 'r', ls = '--', label = 'O II')
ax9.plot(oxygenT4_ax219_data[:,0], oxygenT4_ax219_data[:,3],c = 'b', ls = '--', label = 'O III')
ax9.set_ylabel(r'$\alpha_x$ = 2.19',fontsize = 18)
#ax9.set_xlabel(r'$T_{bb} = 10^4$')

ax10.plot(nitrogenT5_ax219_data[:,0],nitrogenT5_ax219_data[:,1], c = 'g')
ax10.plot(nitrogenT5_ax219_data[:,0],nitrogenT5_ax219_data[:,2], c = 'r')
ax10.plot(nitrogenT5_ax219_data[:,0],nitrogenT5_ax219_data[:,3], c = 'b')
ax10.plot(oxygenT5_ax219_data[:,0],oxygenT5_ax219_data[:,1], c = 'g', ls = '--', label = 'O I')
ax10.plot(oxygenT5_ax219_data[:,0], oxygenT5_ax219_data[:,2],c = 'r', ls = '--', label = 'O II')
ax10.plot(oxygenT5_ax219_data[:,0], oxygenT5_ax219_data[:,3],c = 'b', ls = '--', label = 'O III')


#ax10.set_xlabel(r'$T_{bb} = 10^5$')

ax11.plot(nitrogenT6_ax219_data[:,0],nitrogenT6_ax219_data[:,1], c = 'g')
ax11.plot(nitrogenT6_ax219_data[:,0],nitrogenT6_ax219_data[:,2], c = 'r')
ax11.plot(nitrogenT6_ax219_data[:,0],nitrogenT6_ax219_data[:,3], c = 'b')
ax11.plot(oxygenT6_ax219_data[:,0],oxygenT6_ax219_data[:,1], c = 'g', ls = '--', label = 'O I')
ax11.plot(oxygenT6_ax219_data[:,0], oxygenT6_ax219_data[:,2],c = 'r', ls = '--', label = 'O II')
ax11.plot(oxygenT6_ax219_data[:,0], oxygenT6_ax219_data[:,3],c = 'b', ls = '--', label = 'O III')


#ax11.set_xlabel(r'$T_{bb} = 10^6$')

ax12.plot(nitrogenT7_ax219_data[:,0],nitrogenT7_ax219_data[:,1], c = 'g')
ax12.plot(nitrogenT7_ax219_data[:,0],nitrogenT7_ax219_data[:,2], c = 'r')
ax12.plot(nitrogenT7_ax219_data[:,0],nitrogenT7_ax219_data[:,3], c = 'b')
ax12.plot(oxygenT7_ax219_data[:,0],oxygenT7_ax219_data[:,1], c = 'g', ls = '--', label = 'O I')
ax12.plot(oxygenT7_ax219_data[:,0], oxygenT7_ax219_data[:,2],c = 'r', ls = '--', label = 'O II')
ax12.plot(oxygenT7_ax219_data[:,0], oxygenT7_ax219_data[:,3],c = 'b', ls = '--', label = 'O III')
#ax12.set_xlabel(r'$T_{bb} = 10^7$')


figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

fig.text(0.5,0.04, 'Depth (cm)',fontsize = 18 )
fig.text(0.06,0.5, 'Ionization Fraction', ha = 'center', va = 'center', rotation = 'vertical',fontsize = 18)
plt.suptitle('Ionization Structure for Sulfur and Oxygen',fontsize = 20)
ax1.legend()
plt.gca().xaxis.set_major_locator(MaxNLocator(prune='upper'))
plt.gca().yaxis.set_major_locator(MaxNLocator(prune='upper'))
plt.show()
plt.savefig(r'C:\Users\chris_000\Documents\GitHub\AGN_SED\Presentations\Ionization_structure.png', format='png', dpi=1000)


