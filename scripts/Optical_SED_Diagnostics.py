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
Output_File=r'C:/Users/chris_000/Documents/GitHub/AGN_SED/All_Emissions.csv' #Create the output file
for root, dirs, files in os.walk(rootdirectory, topdown=False):
    for name in files:
        if name.startswith('Ionization_35_Linear_Fit_ax117') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A', 'N  1  5200A']))
            d = pd.concat(dfs, ignore_index=True)
        elif name.startswith('Ionization_35_Linear_Fit_ax219') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A', 'N  1  5200A']))
            d = pd.concat(dfs, ignore_index=True)
        elif name.startswith('Ionization_35_SED') and name.endswith('.lin'):
             print name
            #only read columns from list cols
             dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A', 'N  1  5200A']))
             d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2

d['O III / H-Beta']=np.log10(np.divide(d['O  3  5007A'],d['TOTL  4861A']))

d['O I / H-Alpha']=np.log10(np.divide(d['O  1  6300A'],d['H  1  6563A']))

d['He II / H-Beta'] = np.log10(np.divide(d['HE 2  4686A'],d['TOTL  4861A']))

d['O II / N II'] = np.log10(np.divide(d['TOTL  3727A'],d['N  2  6584A']))

d['N II / H-Alpha']=np.log10(np.divide(d['N  2  6584A'],d['H  1  6563A']))

d['O II / O III'] = np.log10(np.divide(d['TOTL  3727A'],d['O  3  5007A']))

d['O II / O I'] = np.log10(np.divide(d['TOTL  3727A'],d['O  1  6300A']))

d['O I / O III'] = np.log10(np.divide(d['O  1  6300A'],d['O  3  5007A']))

d['S II 6716/ S II 6731'] = np.log10(np.divide(d['S II  6716A'],d['S II  6731A']))

d['O II / H-Beta'] = np.log10(np.divide(d['TOTL  3727A'], d['TOTL  4861A'])) 

d['O III 4363 / H-Alpha'] = np.log10(np.divide(d['TOTL  4363A'],d['TOTL  4861A']))

d['He I / He II'] = np.log10(np.divide(d['HE 1  5876A'],d['HE 2  4686A']))

d['He II / He I'] = np.log10(np.divide(d['HE 2  4686A'],d['HE 1  5876A']))

d['N I 5200 / N II 6584'] = np.log10(np.divide(d['N  1  5200A'], d['N  2  6584A']))

d.to_csv(Output_File, sep = ",", index=True)
#Plot these data points
SDSS_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/flux_norm.csv'
Shirazi_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/shirazi12.csv'
SDSS_Ratios_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/flux_norm_AGN.csv'
SDSS_HeII_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/HeII_sample.csv'
SDSS_Data=np.genfromtxt(SDSS_File, skip_header=1, delimiter = ',',dtype=float,unpack=True)
Shirazi_Data=np.genfromtxt(Shirazi_File, skip_header=3, delimiter = ',',unpack=True)
SDSS_Data_Ratios = np.genfromtxt(SDSS_Ratios_File, skip_header=1, delimiter = ',',dtype=float,invalid_raise = False)
SDSS_Data_HeII = np.genfromtxt(SDSS_HeII_File,skip_header = 1, delimiter = ',',dtype = float)
#Set up an array for data that is just AGN
AGN_Array = np.zeros(len(SDSS_Data_Ratios))
AGN_Array2 = np.zeros(len(SDSS_Data_HeII))

#Conditions for what constitutes AGN
condition1 = np.log10(SDSS_Data_Ratios[:,8]) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(SDSS_Data_Ratios[:,7]),.47))) #From Kewley et al. 2001
condition2a = np.log10(SDSS_Data_Ratios[:,8]) > np.add(1.3,np.multiply(1.18,np.log10(SDSS_Data_Ratios[:,5])))  #From Kewley et al. 2006
condition2b = np.log10(SDSS_Data_Ratios[:,8]) > np.add(1.33, np.divide(0.73, np.add(np.log10(SDSS_Data_Ratios[:,5]),.59)))
condition3a = np.log10(SDSS_Data_Ratios[:,8]) > np.add(0.76, np.multiply(1.89,np.log10(SDSS_Data_Ratios[:,18])))
condition3b = np.log10(SDSS_Data_Ratios[:,8]) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(SDSS_Data_Ratios[:,18]),0.32))) 
condition4a = np.log10(SDSS_Data_Ratios[:,2]) > np.subtract(np.multiply(-1.701,np.log10(SDSS_Data_Ratios[:,5])),2.163)
condition4b = np.log10(SDSS_Data_Ratios[:,2]) > np.add(np.log10(SDSS_Data_Ratios[:,5]),0.7)


Hecondition1 = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(np.divide(SDSS_Data_HeII[:,28],SDSS_Data_HeII[:,27])),.47)))
Hecondition2a = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.3,np.multiply(1.18,np.log10(np.divide(SDSS_Data_HeII[:,24],SDSS_Data_HeII[:,27]))))  #From Kewley et al. 2006
Hecondition2b = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.33, np.divide(0.73, np.add(np.log10(np.divide(SDSS_Data_HeII[:,24],SDSS_Data_HeII[:,27])),.59)))
Hecondition3a = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(0.76, np.multiply(1.89,np.log10(np.divide(np.add(SDSS_Data_HeII[:,29],SDSS_Data_HeII[:,30]),SDSS_Data_HeII[:,27]))))
Hecondition3b = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(np.divide(np.add(SDSS_Data_HeII[:,29],SDSS_Data_HeII[:,30]),SDSS_Data_HeII[:,27])),0.32))) 

mask = (condition1 & condition2a & condition2b & (condition3a & condition3b))
mask2 = (Hecondition1 & Hecondition2a & Hecondition2b & (Hecondition3a & Hecondition3b))

AGN_Array= SDSS_Data_Ratios[mask,:]
AGN_Array2 = SDSS_Data_HeII[mask2,:]
ax1 = plt.subplot(231, aspect = 'equal', adjustable = 'box-forced')
ax2 = plt.subplot(232, aspect = 'equal', adjustable = 'box-forced')
ax3 = plt.subplot(233, aspect = 'equal', adjustable = 'box-forced')
ax4 = plt.subplot(234,  adjustable = 'box')
ax5 = plt.subplot(235)
basexvalO3O2 = (d['O II / O III'].get_value(0),d['O II / O III'].get_value(3),d['O II / O III'].get_value(6),d['O II / O III'].get_value(9))
baseyvalO3 = (d['O III / H-Beta'].get_value(0),d['O III / H-Beta'].get_value(3),d['O III / H-Beta'].get_value(6),d['O III / H-Beta'].get_value(9))
linxvalO3O2 = (d['O II / O III'].get_value(1),d['O II / O III'].get_value(4),d['O II / O III'].get_value(7),d['O II / O III'].get_value(10))
linyvalO3 = (d['O III / H-Beta'].get_value(1),d['O III / H-Beta'].get_value(4),d['O III / H-Beta'].get_value(7),d['O III / H-Beta'].get_value(10))
lin12xvalO3O2 = (d['O II / O III'].get_value(2),d['O II / O III'].get_value(5),d['O II / O III'].get_value(8),d['O II / O III'].get_value(11))
lin12yvalO3 = (d['O III / H-Beta'].get_value(2),d['O III / H-Beta'].get_value(5),d['O III / H-Beta'].get_value(8),d['O III / H-Beta'].get_value(11))
ax1.scatter(np.log10(SDSS_Data_Ratios[:,1]),np.log10(SDSS_Data_Ratios[:,8]), edgecolor = '', c = '#000080',s=5)
ax1.scatter(np.log10(AGN_Array[:,1]),np.log10(AGN_Array[:,8]), edgecolor = '', c = '#800000', s = 5)
ax1.scatter(d['O II / O III'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax1.scatter(d['O II / O III'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax1.scatter(d['O II / O III'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax1.scatter(d['O II / O III'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax1.scatter(d['O II / O III'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4 ax=1.17")
ax1.scatter(d['O II / O III'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5 ax=1.17")
ax1.scatter(d['O II / O III'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6 ax=1.17")
ax1.scatter(d['O II / O III'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7 ax=1.17")

ax1.scatter(d['O II / O III'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4 ax=2.19")
ax1.scatter(d['O II / O III'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5 ax=2.19")
ax1.scatter(d['O II / O III'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6 ax=2.19")
ax1.scatter(d['O II / O III'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7 ax=2.19")
ax1.plot(basexvalO3O2,baseyvalO3,c = '0')
ax1.plot(linxvalO3O2,linyvalO3, c = '0')
ax1.plot(lin12xvalO3O2, lin12yvalO3, c = '0')

ax1.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax1.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / [O III] $\lambda 5007$)')
ax1.set_xlim(np.log10(10**(-1.5)),np.log10(10**2))
ax1.set_ylim(np.log10(10**(-1.5)), np.log10(10**(1.5)))
baseO1O3 = (d['O I / O III'].get_value(0),d['O I / O III'].get_value(3),d['O I / O III'].get_value(6),d['O I / O III'].get_value(9))
linO1O3 = (d['O I / O III'].get_value(1),d['O I / O III'].get_value(4),d['O I / O III'].get_value(7),d['O I / O III'].get_value(10))
lin12O1O3 = (d['O I / O III'].get_value(2),d['O I / O III'].get_value(5),d['O I / O III'].get_value(8),d['O I / O III'].get_value(11))
ax2.scatter(np.log10(SDSS_Data_Ratios[:,1]),np.log10(SDSS_Data_Ratios[:,6]),edgecolor = '', c = '#000080',s = 5)
ax2.scatter(np.log10(AGN_Array[:,1]),np.log10(AGN_Array[:,6]),edgecolor = '', s = 5, c = '#800000')
ax2.scatter(d['O II / O III'].get_value(0),d['O I / O III'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax2.scatter(d['O II / O III'].get_value(3),d['O I / O III'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax2.scatter(d['O II / O III'].get_value(6),d['O I / O III'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax2.scatter(d['O II / O III'].get_value(9),d['O I / O III'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax2.scatter(d['O II / O III'].get_value(1),d['O I / O III'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4 ax=1.6")
ax2.scatter(d['O II / O III'].get_value(4),d['O I / O III'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5 ax=1.6")
ax2.scatter(d['O II / O III'].get_value(7),d['O I / O III'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6 ax=1.6")
ax2.scatter(d['O II / O III'].get_value(10),d['O I / O III'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7 ax=1.6")

ax2.scatter(d['O II / O III'].get_value(2),d['O I / O III'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4 ax=1.2")
ax2.scatter(d['O II / O III'].get_value(5),d['O I / O III'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5 ax=1.2")
ax2.scatter(d['O II / O III'].get_value(8),d['O I / O III'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6 ax=1.2")
ax2.scatter(d['O II / O III'].get_value(11),d['O I / O III'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7 ax=1.2")
ax2.plot(basexvalO3O2,baseO1O3, c= '0')
ax2.plot(linxvalO3O2,linO1O3, c= '0')
ax2.plot(lin12xvalO3O2,lin12O1O3, c ='0')
ax2.set_ylabel(r'Log$_{10}$([O I] $\lambda 6300$ / [O III] $\lambda 5007$)')
ax2.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / [O III] $\lambda 5007$)')
ax2.set_xlim(-2,2)
ax2.set_ylim(-3,1.5)

baseO2O1 = (d['O II / O I'].get_value(0),d['O II / O I'].get_value(3),d['O II / O I'].get_value(6),d['O II / O I'].get_value(9))
linO2O1 = (d['O II / O I'].get_value(1),d['O II / O I'].get_value(4),d['O II / O I'].get_value(7),d['O II / O I'].get_value(10))
lin12O2O1 = (d['O II / O I'].get_value(2),d['O II / O I'].get_value(5),d['O II / O I'].get_value(8),d['O II / O I'].get_value(11))
ax3.scatter(np.log10(SDSS_Data_Ratios[:,4]),np.log10(SDSS_Data_Ratios[:,8]),edgecolor = '', c = '#000080',s=5)
ax3.scatter(np.log10(AGN_Array[:,4]), np.log10(AGN_Array[:,8]),edgecolor = '', c = '#800000',s=5)
ax3.scatter(d['O II / O I'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax3.scatter(d['O II / O I'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax3.scatter(d['O II / O I'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax3.scatter(d['O II / O I'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax3.scatter(d['O II / O I'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax3.scatter(d['O II / O I'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax3.scatter(d['O II / O I'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax3.scatter(d['O II / O I'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")

ax3.scatter(d['O II / O I'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax3.scatter(d['O II / O I'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax3.scatter(d['O II / O I'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax3.scatter(d['O II / O I'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax3.plot(baseO2O1,baseyvalO3, c= '0')
ax3.plot(linO2O1,linyvalO3, c= '0')
ax3.plot(lin12O2O1,lin12yvalO3, c='0')
ax3.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / [O I] $\lambda 6300$)')
ax3.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)')
ax3.set_xlim(np.log10(10**(-1)),np.log10(10**3))
ax3.set_ylim(np.log10(10**(-1.5)), np.log10(10**(2)))

baseHe2He1 = (d['He II / He I'].get_value(0),d['He II / He I'].get_value(3),d['He II / He I'].get_value(6),d['He II / He I'].get_value(9))
linHe2He1 = (d['He II / He I'].get_value(1),d['He II / He I'].get_value(4),d['He II / He I'].get_value(7),d['He II / He I'].get_value(10))
lin21He2He1 = (d['He II / He I'].get_value(2),d['He II / He I'].get_value(5),d['He II / He I'].get_value(8),d['He II / He I'].get_value(11))
ax4.scatter(np.log10(np.divide(SDSS_Data_HeII[:,15],SDSS_Data_HeII[:,23])),np.log10(np.divide(np.add(SDSS_Data_HeII[:,7],SDSS_Data_HeII[:,8]),SDSS_Data_HeII[:,20])),edgecolor = '', c = '#000080',s=5)
ax4.scatter(np.log10(np.divide(AGN_Array2[:,15],AGN_Array2[:,23])), np.log10(np.divide(np.add(AGN_Array2[:,7],AGN_Array2[:,8]),AGN_Array2[:,20])),edgecolor = '', c = '#800000',s=5)
ax4.scatter(d['He II / He I'].get_value(0),d['O II / O III'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax4.scatter(d['He II / He I'].get_value(3),d['O II / O III'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax4.scatter(d['He II / He I'].get_value(6),d['O II / O III'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax4.scatter(d['He II / He I'].get_value(9),d['O II / O III'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
ax4.scatter(d['He II / He I'].get_value(1),d['O II / O III'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax4.scatter(d['He II / He I'].get_value(4),d['O II / O III'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax4.scatter(d['He II / He I'].get_value(7),d['O II / O III'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax4.scatter(d['He II / He I'].get_value(10),d['O II / O III'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
ax4.set_xlabel(r'Log$_{10}$([He II] $\lambda 4686$ / [He I] $\lambda 5876$)')
ax4.set_ylabel(r'Log$_{10}$([O II] $\lambda 3727$ / [O III] $\lambda 5007$)')
ax4.scatter(d['He II / He I'].get_value(2),d['O II / O III'].get_value(2), marker = "s", c='#50DA50', s = 30, label = "10^4")
ax4.scatter(d['He II / He I'].get_value(5),d['O II / O III'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax4.scatter(d['He II / He I'].get_value(8),d['O II / O III'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax4.scatter(d['He II / He I'].get_value(11),d['O II / O III'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax4.plot(baseHe2He1,basexvalO3O2, c = '0')
ax4.plot(linHe2He1,linxvalO3O2, ls = '--', c = '0')
ax4.plot(lin21He2He1, lin12xvalO3O2, ls = ':', lw = 3, c = '0')
ax4.set_xlim(-2,4)
ax4.set_ylim(-2,2)


baseN1N2 = (d['N I 5200 / N II 6584'].get_value(0),d['N I 5200 / N II 6584'].get_value(3),d['N I 5200 / N II 6584'].get_value(6),d['N I 5200 / N II 6584'].get_value(9))
linN1N2 = (d['N I 5200 / N II 6584'].get_value(1),d['N I 5200 / N II 6584'].get_value(4),d['N I 5200 / N II 6584'].get_value(7),d['N I 5200 / N II 6584'].get_value(10))
lin21N1N2 = (d['N I 5200 / N II 6584'].get_value(2),d['N I 5200 / N II 6584'].get_value(5),d['N I 5200 / N II 6584'].get_value(8),d['N I 5200 / N II 6584'].get_value(11))
ax5.scatter(np.log10(np.divide(SDSS_Data_HeII[:,15],SDSS_Data_HeII[:,23])),np.log10(np.divide(SDSS_Data_HeII[:,22],SDSS_Data_HeII[:,28])),edgecolor = '', c = '#000080',s=5)
ax5.scatter(np.log10(np.divide(AGN_Array2[:,15],AGN_Array2[:,23])),np.log10(np.divide(AGN_Array2[:,22],AGN_Array2[:,28])), edgecolor = '', c = '#800000',s=5)
ax5.scatter(d['He II / He I'].get_value(0), d['N I 5200 / N II 6584'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax5.scatter(d['He II / He I'].get_value(3), d['N I 5200 / N II 6584'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax5.scatter(d['He II / He I'].get_value(6),d['N I 5200 / N II 6584'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax5.scatter(d['He II / He I'].get_value(9),d['N I 5200 / N II 6584'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
ax5.scatter(d['He II / He I'].get_value(1),d['N I 5200 / N II 6584'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax5.scatter(d['He II / He I'].get_value(4),d['N I 5200 / N II 6584'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax5.scatter(d['He II / He I'].get_value(7),d['N I 5200 / N II 6584'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax5.scatter(d['He II / He I'].get_value(10),d['N I 5200 / N II 6584'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
ax5.set_xlabel(r'Log$_{10}$([He II] $\lambda 4686$ / [He I] $\lambda 5876$)')
ax5.set_ylabel(r'Log$_{10}$([N I] $\lambda 5200$ / [N II] $\lambda 6584$)')
ax5.scatter(d['He II / He I'].get_value(2),d['N I 5200 / N II 6584'].get_value(2), marker = "s", c='#50DA50', s = 30, label = "10^4")
ax5.scatter(d['He II / He I'].get_value(5),d['N I 5200 / N II 6584'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax5.scatter(d['He II / He I'].get_value(8),d['N I 5200 / N II 6584'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax5 .scatter(d['He II / He I'].get_value(11),d['N I 5200 / N II 6584'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax5.set_xlim(-2,2)
ax5.set_ylim(-3.5,2)
ax5.plot(baseHe2He1, baseN1N2, c = '0')
ax5.plot(linHe2He1,linN1N2, ls = '--', c = '0')
ax5.plot(lin21He2He1, lin21N1N2, ls = ':', lw = 3, c = '0')

#Display the figure full screen
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
ax2.legend(loc = 'best', bbox_to_anchor = [2.5,-0.25])
plt.suptitle('AGN SED Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
plt.show() 
plt.savefig('C:\Users\chris_000\Documents\GitHub\AGN_SED\Diagnostic_Plots\Optical\Separated_By_Diagnostic\With_Linear_Fit\Linear_Variations_Fixed\With_Weak_Lines\SED_Diagnostics.png',dpi = 600)