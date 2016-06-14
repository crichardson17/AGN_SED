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
                
rootdirectory=r'C:/Users/chris_000/Documents/GitHub/AGN_SED/Cloudy_Data'

filelist(rootdirectory)

#Generate a CSV file containing all the relevant data points

#Output_File=r'C:/Users/chris_000/Documents/GitHub/AGN_SED/All_Emissions.csv' #Create the output file

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
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A']))
            d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2
d['O III / H-Beta']=np.log10(np.divide(d['O  3  5007A'],d['TOTL  4861A']))

d['O I / H-Alpha']=np.log10(np.divide(d['O  1  6300A'],d['H  1  6563A']))

d['N II / H-Alpha']=np.log10(np.divide(d['N  2  6584A'],d['H  1  6563A']))

d['S II / H-Alpha']=np.log10(np.divide(d['S  2  6720A'],d['H  1  6563A']))

d['O II / O III'] = np.log10(np.divide(d['TOTL  3727A'],d['O  3  5007A']))

d['O II / H-Beta'] = np.log10(np.divide(d['TOTL  3727A'], d['TOTL  4861A'])) 

d['O III / O II'] = np.log10(np.divide(d['O  3  5007A'],d['TOTL  3727A']))

d['He II / H-Beta'] = np.log10(np.divide(d['HE 2  4686A'],d['TOTL  4861A']))

#Plot these data points
SDSS_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/flux_norm.csv'
Shirazi_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/Shirazi12_Only_Data.csv'
SDSS_Ratios_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/flux_norm_AGN.csv'
SDSS_Data=np.genfromtxt(SDSS_File, skip_header=1, delimiter = ',',dtype=float,unpack=True)
Shirazi_Data=np.genfromtxt(Shirazi_File, skip_header=3, delimiter = ',',dtype = float)
SDSS_Data_Ratios = np.genfromtxt(SDSS_Ratios_File, skip_header=1, delimiter = ',',dtype=float,invalid_raise = False)
#Set up an array for data that is just AGN
AGN_Array = np.zeros(len(SDSS_Data_Ratios))

#Conditions for what constitutes AGN
condition1 = np.log10(SDSS_Data_Ratios[:,10]) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(SDSS_Data_Ratios[:,3]),.47))) #From Kewley et al. 2001
condition2a = np.log10(SDSS_Data_Ratios[:,10]) > np.add(1.3,np.multiply(1.18,np.log10(SDSS_Data_Ratios[:,2])))  #From Kewley et al. 2006
condition2b = np.log10(SDSS_Data_Ratios[:,10]) > np.add(1.33, np.divide(0.73, np.add(np.log10(SDSS_Data_Ratios[:,2]),.59)))
condition3a = np.log10(SDSS_Data_Ratios[:,10]) > np.add(0.76, np.multiply(1.89,np.log10(SDSS_Data_Ratios[:,5])))
condition3b = np.log10(SDSS_Data_Ratios[:,10]) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(SDSS_Data_Ratios[:,5]),0.32))) 
condition4a = np.log10(SDSS_Data_Ratios[:,6]) > np.subtract(np.multiply(-1.701,np.log10(SDSS_Data_Ratios[:,2])),2.163)
condition4b = np.log10(SDSS_Data_Ratios[:,6]) > np.add(np.log10(SDSS_Data_Ratios[:,2]),0.7)
condition5a = Shirazi_Data[:,0] >= np.add(-1.22, np.divide(1,np.add(np.multiply(8.92,Shirazi_Data[:,1]),1.32)))
condition5b = Shirazi_Data[:,1] >= -0.2

mask = (condition1 & condition2a & condition2b & (condition3a & condition3b))

AGN_Array= SDSS_Data_Ratios[mask,:]

ax1 = plt.subplot(231, aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax2 = plt.subplot(232, aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax3 = plt.subplot(233, aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax4 = plt.subplot(234, aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax5 = plt.subplot(235,aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax6 = plt.subplot(236,aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
z = [10^4,10^5, 10^6, 10^7]
x1=np.arange(-2,0.3,0.01)
y1=1.19+np.divide(0.61,x1-0.47)
x2=np.arange(-2,0,0.01)
y2 = 1.3+np.divide(0.61,x2-0.05)


#Make arrays for that have just the data from AGN
N2AGN = SDSS_Data_Ratios[condition1, :]
OIAGN = SDSS_Data_Ratios[np.logical_and(condition2a, condition2b),:]
S2AGN = SDSS_Data_Ratios[(condition3a & condition3b),:]
O3O2AGN = SDSS_Data_Ratios[(condition4a & condition4b),:]
ShiraziAGN = Shirazi_Data[(condition5a | condition5b),:]

np.savetxt("C:/Users/chris_000/Documents/GitHub/AGN_SED/ShiraziAGN.csv",ShiraziAGN, delimiter = ',')
print Shirazi_Data
print ShiraziAGN
ax1.scatter(np.log10(np.divide(SDSS_Data[18],SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])),  marker = 'o',edgecolor = '', c = '#000080',s = 5)
ax1.scatter(np.log10(AGN_Array[:,3]),np.log10(AGN_Array[:,10]),edgecolor = '', s = 5, c = '#800000')
l1 = ax1.scatter(d['N II / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
l2 = ax1.scatter(d['N II / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
l3 = ax1.scatter(d['N II / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
l4 = ax1.scatter(d['N II / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax1.plot(x1,y1,c = '0',linewidth = 2)
ax1.plot(x2,y2, c = '0',ls = '--', lw = 2)

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
ax2.scatter(np.log10(np.divide(SDSS_Data[15],SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), edgecolor = '', c = '#000080',s=5)
ax2.scatter(np.log10(AGN_Array[:,2]),np.log10(AGN_Array[:,10]),edgecolor = '', s = 5, c = '#800000')
ax2.scatter(d['O I / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax2.scatter(d['O I / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax2.scatter(d['O I / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax2.scatter(d['O I / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax2.plot(x3,y3,c = '0', ls = '-', linewidth = 2)

ax2.plot(x4,y4,c = '0', ls = '--', linewidth = 3.0)

ax2.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))
ax2.set_xlim(np.log10(10**(-3)),np.log10(10**0.5))
ax2.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax2.set_xlabel(r'Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$)')
ax2.text(-2,1, 'Seyfert')
ax2.text(-2.5,0.5, 'Starburst')
ax2.text(-0.5,-1,'LINER')


x5 = np.arange(-3,0.1,0.01)
y5 = 1.30 + np.divide(0.72,x5-0.32)
x6 = np.arange(-0.3,1.0,0.01)
y6 = 1.89 * x6 + 0.76
ax3.scatter(np.log10(np.divide(np.add(SDSS_Data[19],SDSS_Data[20]),SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],SDSS_Data[11])), edgecolor = '', c = '#000080',s=5.0)
ax3.scatter(np.log10(AGN_Array[:,5]),np.log10(AGN_Array[:,10]),edgecolor = '', c = '#800000', s = 5)
ax3.scatter(d['S II / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax3.scatter(d['S II / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax3.scatter(d['S II / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax3.scatter(d['S II / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax3.plot(x5,y5, c='0',ls = '-',linewidth=2)
ax3.plot(x6,y6, c='0',ls = '--',linewidth=3.0)
ax3.set_xlim(np.log10(10**(-2)),np.log10(10**1.5))
ax3.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))
ax3.set_ylabel(r'Log$1{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax3.set_xlabel(r'Log$_{10}$([S II] $\lambda 6720$ / H$\alpha$)')
ax3.text(-1.3,1,'Seyfert')
ax3.text(0.2,-0.5,'LINER')

x9 = np.arange(-2,0.9,0.01)
y9 = np.divide(.11,x9-0.92)+0.85
x10 = np.arange(0.7,3,0.01)
y10 = np.multiply(0.95,x10)-0.4

ax4.scatter(np.log10(SDSS_Data_Ratios[:,1]),np.log10(SDSS_Data_Ratios[:,10]),edgecolor = '', c = '#000080',s=5)
ax4.scatter(np.log10(AGN_Array[:,1]),np.log10(AGN_Array[:,10]),edgecolor = '', c = '#800000',s=5)
ax4.scatter(d['O II / H-Beta'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax4.scatter(d['O II / H-Beta'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax4.scatter(d['O II / H-Beta'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax4.scatter(d['O II / H-Beta'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax4.plot(x9,y9,x10,y10,c = '0', lw = 2)
ax4.axhline(y = 0.3,xmin = -2, xmax = 0.65, c = '0', lw =3)
ax4.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax4.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / H$\beta$')
ax4.set_xlim(np.log10(10**(-1.5)),np.log10(10**2))
ax4.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))
ax4.text(-1,0.5,'SF/Sy2')
ax4.text(-1,1,'Seyfert 2')
ax4.text(-1,-0.5,'Star-forming')
ax4.text(1,-1,'LINER')

x = np.arange(-3,-0.2,0.01)
y = -1.22 + np.divide(1,8.92*x+1.32)
ax5.scatter(Shirazi_Data[:,1],Shirazi_Data[:,0], marker = '^', c ='#000080' ,edgecolor = '', s = 15)
ax5.scatter(ShiraziAGN[:,1],ShiraziAGN[:,0], marker = '^', c = '#800000',edgecolor = '', s = 15)
ax5.scatter(d['N II / H-Alpha'].get_value(0),d['He II / H-Beta'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax5.scatter(d['N II / H-Alpha'].get_value(1),d['He II / H-Beta'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax5.scatter(d['N II / H-Alpha'].get_value(2),d['He II / H-Beta'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax5.scatter(d['N II / H-Alpha'].get_value(3),d['He II / H-Beta'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax5.plot(x,y, c = '0', ls = '-', lw = 2.0)
ax5.set_xlim(-3,2)
ax5.set_ylim(-3,2)
ax5.set_xticks((-3,-2,-1,0,1,2))
ax5.set_yticks((-3,-2,-1,0,1,2))
ax5.set_xlabel(r'Log$_{10}$([N II] $\lambda 6584$ / H$\alpha$)')
ax5.set_ylabel(r'Log$_{10}$([He II] $\lambda 4686$ / H$\beta$)')
ax5.text(-1,-2.5, 'Starburst')
ax5.text(-2,0,'AGN')

x7 = np.arange(-2.5,1.5)
y7 = -1.701*x7-2.163
x8 = np.arange(-1.1,1)
y8 = 1.0*x8+0.7
ax6.scatter(np.log10(np.divide(SDSS_Data[15],SDSS_Data[17])),np.log10(np.divide(SDSS_Data[13],np.add(SDSS_Data[5],SDSS_Data[6]))),edgecolor = '', s = 5,c = '#000080', )
ax6.scatter(np.log10(O3O2AGN[:,2]), np.log10(O3O2AGN[:,6]), edgecolor = '', s = 5, c = '#800000')
ax6.scatter(d['O I / H-Alpha'].get_value(0),d['O III / O II'].get_value(0), marker = "s",c='green', s = 30, label = "10^4")
ax6.scatter(d['O I / H-Alpha'].get_value(1),d['O III / O II'].get_value(1), marker = "s",c='cyan', s = 30, label = "10^5")
ax6.scatter(d['O I / H-Alpha'].get_value(2),d['O III / O II'].get_value(2), marker = "s",c='r', s = 30, label = "10^6")
ax6.scatter(d['O I / H-Alpha'].get_value(3),d['O III / O II'].get_value(3), marker = "s",c='magenta', s = 30, label = "10^7")
ax6.plot(x7,y7, x8,y8, c = '0', lw = 3.0)
ax6.set_xlim(-2.5,0.5)
ax6.set_ylim(-1.5,1.5)
ax6.set_xlabel(r'Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$)')
ax6.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$) / [O II] $\lambda 3727$)')
ax6.text(-1.5,1,'Seyfert')
ax6.text(-0.1,0,'LINER')
ax6.text(-2.2,-1.3, 'Starburst')
plt.suptitle('AGN Excitation Mechanism Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
ax1.legend(loc = 'best')

#Display the figure full screen
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show() 
