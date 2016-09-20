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
                
rootdirectory= r'/Users/compastro/greene/AGN_SED/Cloudy_Data' 

filelist(rootdirectory)

#Generate a CSV file containing all the relevant data points

#Output_File=r'C:/Users/chris_000/Documents/GitHub/AGN_SED/All_Emissions.csv' #Create the output file



dfs=[] #Create an empty array for our Data

d=pd.DataFrame() 
d=d.reset_index()
d2=pd.DataFrame({'Temperature': [10**4,10**5, 10**6, 10**7]},dtype=float) #Create a Dataframe of labels for each file used

for root, dirs, files in os.walk(rootdirectory, topdown=False):
    for name in files:
        if name.startswith('Ionization_35_Linear_Fit_ax219') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A']))
            d = pd.concat(dfs, ignore_index=True)
        if name.startswith('Ionization_35_Linear_Fit_ax117') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A']))
        if name.startswith('Ionization_35_SED') and name.endswith('.lin'):
             print name
            #only read columns from list cols
             dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A']))
             d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2

d['He II / H-Beta'] = np.log10(np.divide(d['HE 2  4686A'],d['TOTL  4861A']))

d['O III 4363 / H-Alpha'] = np.log10(np.divide(d['TOTL  4363A'],d['TOTL  4861A']))

d['O III 4363 / O III 5007'] = np.log10(np.divide(d['TOTL  4363A'],d['O  3  5007A']))

d['O III / H-Beta']=np.log10(np.divide(d['O  3  5007A'],d['TOTL  4861A']))

d['O II + O III / H-Beta'] = np.log10(np.divide(np.add(d['TOTL  3727A'],d['O  3  5007A']),d['TOTL  4861A']))

d['O II / O III'] = np.log10(np.divide(d['TOTL  3727A'],d['O  3  5007A']))

d['O I / O III'] = np.log10(np.divide(d['O  1  6300A'],d['O  3  5007A']))


d['S II 6716/ S II 6731'] = np.log10(np.divide(d['S II  6716A'],d['S II  6731A']))

d['O II 3726 / O II 3729'] = np.log10(np.divide(d['O II  3726A'],d['O II  3729A']))

#d.to_csv(Output_File, sep = ",", index=True)
#Plot these data points
SDSS_File = '/Users/compastro/greene/AGN_SED/sdss_data/flux_norm.csv'
SDSS_Ratios_File =  '/Users/compastro/greene/AGN_SED/flux_norm_AGN.csv'
SDSS_HeII_File = '/Users/compastro/greene/AGN_SED/sdss_data/HeII_sample.csv'
SDSS_Data=np.genfromtxt(SDSS_File, skip_header=1, delimiter = ',',dtype=float,unpack=True)
SDSS_Data_Ratios = np.genfromtxt(SDSS_Ratios_File, skip_header=1, delimiter = ',',dtype=float,invalid_raise = False)
SDSS_Data_HeII = np.genfromtxt(SDSS_HeII_File,skip_header = 1, delimiter = ',',dtype = float)
#Set up an array for data that is just AGN
AGN_Array = np.zeros(len(SDSS_Data_Ratios))

#Conditions for what constitutes AGN
condition1 = np.log10(SDSS_Data_Ratios[:,8]) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(SDSS_Data_Ratios[:,7]),.47))) #From Kewley et al. 2001
condition2a = np.log10(SDSS_Data_Ratios[:,8]) > np.add(1.3,np.multiply(1.18,np.log10(SDSS_Data_Ratios[:,5])))  #From Kewley et al. 2006
condition2b = np.log10(SDSS_Data_Ratios[:,8]) > np.add(1.33, np.divide(0.73, np.add(np.log10(SDSS_Data_Ratios[:,5]),.59)))
condition3a = np.log10(SDSS_Data_Ratios[:,8]) > np.add(0.76, np.multiply(1.89,np.log10(SDSS_Data_Ratios[:,18])))
condition3b = np.log10(SDSS_Data_Ratios[:,8]) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(SDSS_Data_Ratios[:,18]),0.32))) 
condition4a = np.log10(SDSS_Data_Ratios[:,2]) > np.add(np.multiply(-1.701,np.log10(SDSS_Data_Ratios[:,5])),-2.163)
condition4b = np.log10(SDSS_Data_Ratios[:,2]) > np.add(np.log10(SDSS_Data_Ratios[:,5]),0.7)


Hecondition1 = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(np.divide(SDSS_Data_HeII[:,28],SDSS_Data_HeII[:,27])),.47)))
Hecondition2a = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.3,np.multiply(1.18,np.log10(np.divide(SDSS_Data_HeII[:,24],SDSS_Data_HeII[:,27]))))  #From Kewley et al. 2006
Hecondition2b = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.33, np.divide(0.73, np.add(np.log10(np.divide(SDSS_Data_HeII[:,24],SDSS_Data_HeII[:,27])),.59)))
Hecondition3a = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(0.76, np.multiply(1.89,np.log10(np.divide(np.add(SDSS_Data_HeII[:,29],SDSS_Data_HeII[:,30]),SDSS_Data_HeII[:,27]))))
Hecondition3b = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(np.divide(np.add(SDSS_Data_HeII[:,29],SDSS_Data_HeII[:,30]),SDSS_Data_HeII[:,27])),0.32)))
mask = (condition1 & condition2a & condition2b & (condition3a & condition3b))

AGN_Array= SDSS_Data_Ratios[mask,:]
mask2 = (Hecondition1 & Hecondition2a & Hecondition2b & (Hecondition3a & Hecondition3b))

AGN_Array2 = SDSS_Data_HeII[mask2,:]
plt.figure()
ax1 = plt.subplot(111,autoscale_on = False)
#ax2 = plt.subplot(222, aspect = 'equal', autoscale_on = False)
#ax3 = plt.subplot(223, aspect = 'equal')

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


basexvalO3 = (d['O III 4363 / O III 5007'].get_value(0),d['O III 4363 / O III 5007'].get_value(3),d['O III 4363 / O III 5007'].get_value(6),d['O III 4363 / O III 5007'].get_value(9))
baseyvalS2 = (d['S II 6716/ S II 6731'].get_value(0),d['S II 6716/ S II 6731'].get_value(3),d['S II 6716/ S II 6731'].get_value(6),d['S II 6716/ S II 6731'].get_value(9))
linxval03 = (d['O III 4363 / O III 5007'].get_value(1),d['O III 4363 / O III 5007'].get_value(4),d['O III 4363 / O III 5007'].get_value(7),d['O III 4363 / O III 5007'].get_value(10))
linyvalS2 = (d['S II 6716/ S II 6731'].get_value(1),d['S II 6716/ S II 6731'].get_value(4),d['S II 6716/ S II 6731'].get_value(7),d['S II 6716/ S II 6731'].get_value(10))
lin12xval03 = (d['O III 4363 / O III 5007'].get_value(2),d['O III 4363 / O III 5007'].get_value(5),d['O III 4363 / O III 5007'].get_value(8),d['O III 4363 / O III 5007'].get_value(11))
lin12yvalS2 = (d['S II 6716/ S II 6731'].get_value(2),d['S II 6716/ S II 6731'].get_value(5),d['S II 6716/ S II 6731'].get_value(8),d['S II 6716/ S II 6731'].get_value(11))
ax1.scatter(np.log10(SDSS_Data_Ratios[:,16]),np.log10(SDSS_Data_Ratios[:,14]),edgecolor = '', c = '#000080',s = 5)
ax1.scatter(np.log10(AGN_Array[:,16]),np.log10(AGN_Array[:,14]),edgecolor = '', s = 5, c = '#800000')
ax1.scatter(d['O III 4363 / O III 5007'].get_value(0),d['S II 6716/ S II 6731'].get_value(0), marker = "s",c='#FF5D5D', s = 60, label = "10^4")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(3),d['S II 6716/ S II 6731'].get_value(3), marker = "s",c='#FF0000', s = 60, label = "10^5")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(6),d['S II 6716/ S II 6731'].get_value(6), marker = "s",c='#C60000', s = 60, label = "10^6")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(9),d['S II 6716/ S II 6731'].get_value(9), marker = "s",c='#9B0000', s = 60, label = "10^7")

ax1.scatter(d['O III 4363 / O III 5007'].get_value(1),d['S II 6716/ S II 6731'].get_value(1), marker = "s",c='#7056C5', s = 60, label = "10^4 ax=1.17")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(4),d['S II 6716/ S II 6731'].get_value(4), marker = "s",c='#3914AF', s = 60, label = "10^5 ax=1.17")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(7),d['S II 6716/ S II 6731'].get_value(7), marker = "s",c='#2B0E87', s = 60, label = "10^6 ax=1.17")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(10),d['S II 6716/ S II 6731'].get_value(10), marker = "s",c='#200969', s = 60, label = "10^7 ax=1.17")

ax1.scatter(d['O III 4363 / O III 5007'].get_value(2),d['S II 6716/ S II 6731'].get_value(2), marker = "s",c='#50DA50', s = 60, label = "10^4 ax=2.19")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(5),d['S II 6716/ S II 6731'].get_value(5), marker = "s",c='#00CC00', s = 60, label = "10^5 ax=2.19")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(8),d['S II 6716/ S II 6731'].get_value(8), marker = "s",c='#009D00', s = 60, label = "10^6 ax=2.19")
ax1.scatter(d['O III 4363 / O III 5007'].get_value(11),d['S II 6716/ S II 6731'].get_value(11), marker = "s",c='#007A00', s = 60, label = "10^7 ax=2.19")
ax1.plot(basexvalO3, baseyvalS2, c = '0')
ax1.plot(linxval03,linyvalS2, ls = '--', c = '0')
ax1.plot(lin12xval03,lin12yvalS2, ls = ':', lw = 3, c = '0')
ax1.set_xlabel(r'Log$_{10}$( [O III] $\lambda 4363$/ [O III] $\lambda 5007$)', fontsize = 20)
ax1.set_ylabel(r'Log$_{10}$([S II] $\lambda 6716$ / [S II] $\lambda 6731$)', fontsize = 20)
ax1.set_xlim(-4.0,0.0)
ax1.set_ylim(-1.5,1.5)

#basexvalO3Ha = (d['O III 4363 / H-Alpha'].get_value(0),d['O III 4363 / H-Alpha'].get_value(3),d['O III 4363 / H-Alpha'].get_value(6),d['O III 4363 / H-Alpha'].get_value(9))
#baseyvalO3 = (d['O III / H-Beta'].get_value(0),d['O III / H-Beta'].get_value(3),d['O III / H-Beta'].get_value(6),d['O III / H-Beta'].get_value(9))
#linxvalO3Ha = (d['O III 4363 / H-Alpha'].get_value(1),d['O III 4363 / H-Alpha'].get_value(4),d['O III 4363 / H-Alpha'].get_value(7),d['O III 4363 / H-Alpha'].get_value(10))
#linyvalO3 = (d['O III / H-Beta'].get_value(1),d['O III / H-Beta'].get_value(4),d['O III / H-Beta'].get_value(7),d['O III / H-Beta'].get_value(10))
#lin12xvalO3Ha = (d['O III 4363 / H-Alpha'].get_value(2),d['O III 4363 / H-Alpha'].get_value(5),d['O III 4363 / H-Alpha'].get_value(8),d['O III 4363 / H-Alpha'].get_value(11))
#lin12yvalO3 = (d['O III / H-Beta'].get_value(2),d['O III / H-Beta'].get_value(5),d['O III / H-Beta'].get_value(8),d['O III / H-Beta'].get_value(11))
#ax2.scatter(np.log10(SDSS_Data_Ratios[:,15]),np.log10(SDSS_Data_Ratios[:,8]),edgecolor = '', c = '#000080',s = 5)
#ax2.scatter(np.log10(AGN_Array[:,15]),np.log10(AGN_Array[:,8]),edgecolor = '', s = 5, c = '#800000')
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
#
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
#
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
#ax2.scatter(d['O III 4363 / H-Alpha'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
#ax2.plot(basexvalO3Ha,baseyvalO3,c = '0')
#ax2.plot(linxvalO3Ha,linyvalO3, c = '0')
#ax2.plot(lin12xvalO3Ha,lin12yvalO3, c = '0')
#ax2.set_xlabel(r'Log$_{10}$( [O III] $\lambda 4363$/ H$\alpha$)', fontsize = 20)
#ax2.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)', fontsize = 20)
#ax2.set_xlim(-6.0,0.0)
#ax2.set_ylim(-1.5,1.5)

#basexvalO2 = (d['O II 3726 / O II 3729'].get_value(0),d['O II 3726 / O II 3729'].get_value(3),d['O II 3726 / O II 3729'].get_value(6),d['O II 3726 / O II 3729'].get_value(9))
#linxvalO2 = (d['O II 3726 / O II 3729'].get_value(1),d['O II 3726 / O II 3729'].get_value(4),d['O II 3726 / O II 3729'].get_value(7),d['O II 3726 / O II 3729'].get_value(10))
#lin12xvalO2 = (d['O II 3726 / O II 3729'].get_value(2),d['O II 3726 / O II 3729'].get_value(5),d['O II 3726 / O II 3729'].get_value(8),d['O II 3726 / O II 3729'].get_value(11))
#ax3.scatter(np.log10(SDSS_Data_Ratios[:,19]),np.log10(SDSS_Data_Ratios[:,14]),edgecolor = '', c = '#000080',s = 5)
#ax3.scatter(np.log10(AGN_Array[:,19]),np.log10(AGN_Array[:,14]),edgecolor = '', s = 5, c = '#800000')
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(0),d['S II 6716/ S II 6731'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(3),d['S II 6716/ S II 6731'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(6),d['S II 6716/ S II 6731'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(9),d['S II 6716/ S II 6731'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
#
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(1),d['S II 6716/ S II 6731'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(4),d['S II 6716/ S II 6731'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(7),d['S II 6716/ S II 6731'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(10),d['S II 6716/ S II 6731'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
#
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(2),d['S II 6716/ S II 6731'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(5),d['S II 6716/ S II 6731'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(8),d['S II 6716/ S II 6731'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
#ax3.scatter(d['O II 3726 / O II 3729'].get_value(11),d['S II 6716/ S II 6731'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
#ax3.plot(basexvalO2,baseyvalS2, c = '0')
#ax3.plot(linxvalO2,linyvalS2, c = '0')
#ax3.plot(lin12xvalO2,lin12yvalS2, c = '0')
#ax3.set_ylabel(r'Log$_{10}$([S II] $\lambda 6716$ / [S II] $\lambda 6731$)', fontsize = 20)
#ax3.set_xlabel(r'Log$_{10}$( [O II] $\lambda 3726$/ [O II] $\lambda 3729$)', fontsize = 20)


#Display the figure full screen
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
#plt.suptitle('AGN Temperature / Density Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
ax1.legend(loc = 'upper left')
plt.show() 
