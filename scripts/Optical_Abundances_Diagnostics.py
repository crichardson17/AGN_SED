
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
        if name.startswith('Linear_Fit_ax219') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m']))
            d = pd.concat(dfs, ignore_index=True)
        elif name.startswith('Linear_Fit_ax117') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m']))
            d = pd.concat(dfs, ignore_index=True)
        elif name.startswith('Hden25') and name.endswith('.lin'):
             print name
            #only read columns from list cols
             dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m']))
             d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2

d['O III / H-Beta']=np.log10(np.divide(d['O  3  5007A'],d['TOTL  4861A']))

d['He II / H-Beta'] = np.log10(np.divide(d['HE 2  4686A'],d['TOTL  4861A']))

d['O II / N II'] = np.log10(np.divide(d['TOTL  3727A'],d['N  2  6584A']))

d['N II / H-Alpha']=np.log10(np.divide(d['N  2  6584A'],d['H  1  6563A']))

d['O III / O II'] = np.log10(np.divide(d['O  3  5007A'],d['TOTL  3727A']))

d['O III / Ar III'] = np.log10(np.divide(d['O  3  5007A'],d['AR 3  7135A']))

d['O III / Ne III'] = np.log10(np.divide(d['O  3  5007A'],d['NE 3  3869A']))

d['Ar III / H-Alpha'] = np.log10(np.divide(d['AR 3  7135A'], d['H  1  6563A']))

d['He I / H-Beta'] = np.log10(np.divide(d['HE 1  5876A'],d['TOTL  4861A']))
 
d['O II + O III / H-Beta'] = np.log10(np.divide(np.add(d['O  3  4959A'],np.add(d['TOTL  4363A'],d['O  3  5007A'])),d['TOTL  4861A']))

d['Ne III / H-Alpha'] = np.log10(np.divide(d['NE 3  3869A'], d['H  1  6563A']))

d['S II 6716/ S II 6731'] = np.log10(np.divide(d['S II  6716A'],d['S II  6731A']))

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

mask = (condition1 & (condition2a & condition2b) & (condition3a & condition3b))
mask2 = (Hecondition1 & Hecondition2a & Hecondition2b & (Hecondition3a & Hecondition3b))

AGN_Array= SDSS_Data_Ratios[mask,:]
AGN_Array2 = SDSS_Data_HeII[mask2,:]

ax1 = plt.subplot(231, aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax2 = plt.subplot(232, aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax3 = plt.subplot(233, aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax4 = plt.subplot(234, aspect = 'equal', adjustable = 'box-forced', autoscale_on = False)
ax5 = plt.subplot(235)
ax6 = plt.subplot(236)
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
color5 = np.where(Shirazi_Data[6] >= np.subtract(np.divide(1,np.add(np.multiply(8.92, Shirazi_Data[7]),1.32)),1.22),1,0)


basexvalO3A3 = (d['O III / Ar III'].get_value(0),d['O III / Ar III'].get_value(3),d['O III / Ar III'].get_value(6),d['O III / Ar III'].get_value(9))
baseyvalueNe3 = (d['Ne III / H-Alpha'].get_value(0),d['Ne III / H-Alpha'].get_value(3),d['Ne III / H-Alpha'].get_value(6),d['Ne III / H-Alpha'].get_value(9))
linxval03A3 = (d['O III / Ar III'].get_value(1),d['O III / Ar III'].get_value(4),d['O III / Ar III'].get_value(7),d['O III / Ar III'].get_value(10))
linyvalNe3 = (d['Ne III / H-Alpha'].get_value(1),d['Ne III / H-Alpha'].get_value(4),d['Ne III / H-Alpha'].get_value(7),d['Ne III / H-Alpha'].get_value(10))
lin16xval03A3 = (d['O III / Ar III'].get_value(2),d['O III / Ar III'].get_value(5),d['O III / Ar III'].get_value(8),d['O III / Ar III'].get_value(11))
lin16yvalNe3 = (d['Ne III / H-Alpha'].get_value(2),d['Ne III / H-Alpha'].get_value(5),d['Ne III / H-Alpha'].get_value(8),d['Ne III / H-Alpha'].get_value(11))
ax1.scatter(np.log10(SDSS_Data_Ratios[:,9]),np.log10(SDSS_Data_Ratios[:,11]) , c = '#000080', edgecolor = '', s = 5)
ax1.scatter(np.log10(AGN_Array[:,9]),np.log10(AGN_Array[:,11]) , c = '#800000',edgecolor = '', s = 5)
ax1.scatter(d['O III / Ar III'].get_value(0),d['Ne III / H-Alpha'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax1.scatter(d['O III / Ar III'].get_value(3),d['Ne III / H-Alpha'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax1.scatter(d['O III / Ar III'].get_value(6),d['Ne III / H-Alpha'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax1.scatter(d['O III / Ar III'].get_value(9),d['Ne III / H-Alpha'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax1.scatter(d['O III / Ar III'].get_value(1),d['Ne III / H-Alpha'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4 ax=1.17")
ax1.scatter(d['O III / Ar III'].get_value(4),d['Ne III / H-Alpha'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5 ax=1.17")
ax1.scatter(d['O III / Ar III'].get_value(7),d['Ne III / H-Alpha'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6 ax=1.17")
ax1.scatter(d['O III / Ar III'].get_value(10),d['Ne III / H-Alpha'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7 ax=1.17")

ax1.scatter(d['O III / Ar III'].get_value(2),d['Ne III / H-Alpha'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4 ax=2.9")
ax1.scatter(d['O III / Ar III'].get_value(5),d['Ne III / H-Alpha'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5 ax=2.9")
ax1.scatter(d['O III / Ar III'].get_value(8),d['Ne III / H-Alpha'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6 ax=2.9")
ax1.scatter(d['O III / Ar III'].get_value(11),d['Ne III / H-Alpha'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7 ax=2.9")
ax1.plot(basexvalO3A3, baseyvalueNe3, c = '0')
ax1.plot(linxval03A3,linyvalNe3,c = '0')
ax1.plot(lin16xval03A3,lin16yvalNe3, c = '0')
ax1.set_xlim(-1.5,4)
ax1.set_ylim(-4,1)
ax1.set_xlabel(r'Log$_{10}$([O III] $\lambda 5007$ / [Ar III] $\lambda 7135$)')
ax1.set_ylabel(r'Log$_{10}$([Ne III] $\lambda 3869$ / H$\alpha$)')

basexvalO2N2 = (d['O II / N II'].get_value(0),d['O II / N II'].get_value(3),d['O II / N II'].get_value(6),d['O II / N II'].get_value(9))
baseyvalS2 = (d['S II 6716/ S II 6731'].get_value(0),d['S II 6716/ S II 6731'].get_value(3),d['S II 6716/ S II 6731'].get_value(6),d['S II 6716/ S II 6731'].get_value(9))
linyvalS2 = (d['S II 6716/ S II 6731'].get_value(1),d['S II 6716/ S II 6731'].get_value(4),d['S II 6716/ S II 6731'].get_value(7),d['S II 6716/ S II 6731'].get_value(10))
linxvalO2N2 =  (d['O II / N II'].get_value(1),d['O II / N II'].get_value(4),d['O II / N II'].get_value(7),d['O II / N II'].get_value(10))
lin16yvalS2 = (d['S II 6716/ S II 6731'].get_value(2),d['S II 6716/ S II 6731'].get_value(5),d['S II 6716/ S II 6731'].get_value(8),d['S II 6716/ S II 6731'].get_value(11))
lin16xvalO2N2 =  (d['O II / N II'].get_value(2),d['O II / N II'].get_value(5),d['O II / N II'].get_value(8),d['O II / N II'].get_value(11))
ax2.scatter(np.log10(SDSS_Data_Ratios[:,3]),np.log10(SDSS_Data_Ratios[:,14]),edgecolor = '', c = '#000080',s = 5)
ax2.scatter(np.log10(AGN_Array[:,3]),np.log10(AGN_Array[:,14]),edgecolor = '', s = 5, c = '#800000')
ax2.scatter(d['O II / N II'].get_value(0),d['S II 6716/ S II 6731'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax2.scatter(d['O II / N II'].get_value(3),d['S II 6716/ S II 6731'].get_value(2), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax2.scatter(d['O II / N II'].get_value(6),d['S II 6716/ S II 6731'].get_value(4), marker = "s",c='#C60000', s = 30, label = "10^6")
ax2.scatter(d['O II / N II'].get_value(9),d['S II 6716/ S II 6731'].get_value(6), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax2.scatter(d['O II / N II'].get_value(1),d['S II 6716/ S II 6731'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4 Fit")
ax2.scatter(d['O II / N II'].get_value(4),d['S II 6716/ S II 6731'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5 Fit")
ax2.scatter(d['O II / N II'].get_value(7),d['S II 6716/ S II 6731'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6 Fit ")
ax2.scatter(d['O II / N II'].get_value(10),d['S II 6716/ S II 6731'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7 Fit")

ax2.scatter(d['O II / N II'].get_value(2),d['S II 6716/ S II 6731'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4 Fit")
ax2.scatter(d['O II / N II'].get_value(5),d['S II 6716/ S II 6731'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5 Fit")
ax2.scatter(d['O II / N II'].get_value(8),d['S II 6716/ S II 6731'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6 Fit ")
ax2.scatter(d['O II / N II'].get_value(11),d['S II 6716/ S II 6731'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7 Fit")
ax2.plot(basexvalO2N2,baseyvalS2,c = '0')
ax2.plot(linxvalO2N2,linyvalS2, c = '0')
ax2.plot(lin16xvalO2N2,lin16yvalS2, c = '0')
ax2.set_ylabel(r'Log$_{10}$([S II] $\lambda 6716$ / [S II] $\lambda 6731$')
ax2.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / [N II] $\lambda 6584$)')
ax2.set_xlim(-1,2)
ax2.set_ylim(-1,1.5)


basexvalR23 = (d['O II + O III / H-Beta'].get_value(0),d['O II + O III / H-Beta'].get_value(3),d['O II + O III / H-Beta'].get_value(6),d['O II + O III / H-Beta'].get_value(9))
baseyvalO3 = (d['O III / H-Beta'].get_value(0),d['O III / H-Beta'].get_value(3),d['O III / H-Beta'].get_value(6),d['O III / H-Beta'].get_value(9))
linxvalR23 = (d['O II + O III / H-Beta'].get_value(1),d['O II + O III / H-Beta'].get_value(4),d['O II + O III / H-Beta'].get_value(7),d['O II + O III / H-Beta'].get_value(10))
linyvalO3 = (d['O III / H-Beta'].get_value(1),d['O III / H-Beta'].get_value(4),d['O III / H-Beta'].get_value(7),d['O III / H-Beta'].get_value(10))
lin16xvalR23 = (d['O II + O III / H-Beta'].get_value(2),d['O II + O III / H-Beta'].get_value(5),d['O II + O III / H-Beta'].get_value(8),d['O II + O III / H-Beta'].get_value(11))
lin16yvalO3 = (d['O III / H-Beta'].get_value(2),d['O III / H-Beta'].get_value(5),d['O III / H-Beta'].get_value(8),d['O III / H-Beta'].get_value(11))
ax3.scatter(np.log10(SDSS_Data_Ratios[:,17]),np.log10(SDSS_Data_Ratios[:,3]), edgecolor = '', c = '#000080',s=5.0)
ax3.scatter(np.log10(AGN_Array[:,17]),np.log10(AGN_Array[:,3]),edgecolor = '', c = '#800000', s = 5)
ax3.scatter(d['O II + O III / H-Beta'].get_value(0),d['O II / N II'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax3.scatter(d['O II + O III / H-Beta'].get_value(3),d['O II / N II'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax3.scatter(d['O II + O III / H-Beta'].get_value(6),d['O II / N II'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax3.scatter(d['O II + O III / H-Beta'].get_value(9),d['O II / N II'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
ax3.scatter(d['O II + O III / H-Beta'].get_value(1),d['O II / N II'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax3.scatter(d['O II + O III / H-Beta'].get_value(4),d['O II / N II'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax3.scatter(d['O II + O III / H-Beta'].get_value(7),d['O II / N II'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax3.scatter(d['O II + O III / H-Beta'].get_value(10),d['O II / N II'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
ax3.scatter(d['O II + O III / H-Beta'].get_value(2),d['O II / N II'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax3.scatter(d['O II + O III / H-Beta'].get_value(5),d['O II / N II'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax3.scatter(d['O II + O III / H-Beta'].get_value(8),d['O II / N II'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax3.scatter(d['O II + O III / H-Beta'].get_value(11),d['O II / N II'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax3.plot(basexvalR23,basexvalO2N2,c = '0')
ax3.plot(linxvalR23,linxvalO2N2, c = '0')
ax3.plot(lin16xvalR23,lin16xvalO2N2, c = '0')
ax3.set_xlim(np.log10(10**(-1)),np.log10(10**2))
ax3.set_ylim(np.log10(10**(-1.5)), np.log10(10**(2)))
ax3.set_ylabel(r'Log$_{10}$([N II] $\lambda 6584$ / H$\alpha$)')
ax3.set_xlabel(r'Log$_{10}$([O III] $\lambda 4363$ + [O III] $\lambda 4959$ + [O III] $\lambda 5007$/ H$\beta$)')


ax4.scatter(np.log10(SDSS_Data_Ratios[:,3]),np.log10(SDSS_Data_Ratios[:,8]),edgecolor = '', c = '#000080',s = 5)
ax4.scatter(np.log10(AGN_Array[:,3]),np.log10(AGN_Array[:,8]),edgecolor = '', s = 5, c = '#800000')
ax4.scatter(d['O II / N II'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax4.scatter(d['O II / N II'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax4.scatter(d['O II / N II'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax4.scatter(d['O II / N II'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax4.scatter(d['O II / N II'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax4.scatter(d['O II / N II'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax4.scatter(d['O II / N II'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax4.scatter(d['O II / N II'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")

ax4.scatter(d['O II / N II'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax4.scatter(d['O II / N II'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax4.scatter(d['O II / N II'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax4.scatter(d['O II / N II'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax4.plot(basexvalO2N2,baseyvalO3, c = '0')
ax4.plot(linxvalO2N2,linyvalO3, c = '0')
ax4.plot(lin16xvalO2N2, lin16yvalO3, c = '0')
ax4.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$')
ax4.set_xlabel(r'Log$_{10}$([O II] $\lambda 3727$ / [N II] $\lambda 6584$)')
ax4.set_xlim(-1,2)
ax4.set_ylim(-1,1.5)

basexvalO3Ne3 = (d['O III / Ne III'].get_value(0),d['O III / Ne III'].get_value(3),d['O III / Ne III'].get_value(6),d['O III / Ne III'].get_value(9))
baseyvalAr3 = (d['Ar III / H-Alpha'].get_value(0),d['Ar III / H-Alpha'].get_value(3),d['Ar III / H-Alpha'].get_value(6),d['Ar III / H-Alpha'].get_value(9))
linxvalO3Ne3 = (d['O III / Ne III'].get_value(1),d['O III / Ne III'].get_value(4),d['O III / Ne III'].get_value(7),d['O III / Ne III'].get_value(10))
linyvalAr3 = (d['Ar III / H-Alpha'].get_value(1),d['Ar III / H-Alpha'].get_value(4),d['Ar III / H-Alpha'].get_value(7),d['Ar III / H-Alpha'].get_value(10))
lin16xvalO3Ne3 = (d['O III / Ne III'].get_value(2),d['O III / Ne III'].get_value(5),d['O III / Ne III'].get_value(8),d['O III / Ne III'].get_value(11))
lin16yvalAr3 = (d['Ar III / H-Alpha'].get_value(2),d['Ar III / H-Alpha'].get_value(5),d['Ar III / H-Alpha'].get_value(8),d['Ar III / H-Alpha'].get_value(11))
ax5.scatter(np.log10(SDSS_Data_Ratios[:,10]),np.log10(SDSS_Data_Ratios[:,12]),edgecolor = '', c = '#000080',s = 5)
ax5.scatter(np.log10(AGN_Array[:,10]),np.log10(AGN_Array[:,12]),edgecolor = '', s = 5, c = '#800000')
ax5.scatter(d['O III / Ne III'].get_value(0),d['Ar III / H-Alpha'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax5.scatter(d['O III / Ne III'].get_value(3),d['Ar III / H-Alpha'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax5.scatter(d['O III / Ne III'].get_value(6),d['Ar III / H-Alpha'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax5.scatter(d['O III / Ne III'].get_value(9),d['Ar III / H-Alpha'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax5.scatter(d['O III / Ne III'].get_value(1),d['Ar III / H-Alpha'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax5.scatter(d['O III / Ne III'].get_value(4),d['Ar III / H-Alpha'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax5.scatter(d['O III / Ne III'].get_value(7),d['Ar III / H-Alpha'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax5.scatter(d['O III / Ne III'].get_value(10),d['Ar III / H-Alpha'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")

ax5.scatter(d['O III / Ne III'].get_value(2),d['Ar III / H-Alpha'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax5.scatter(d['O III / Ne III'].get_value(5),d['Ar III / H-Alpha'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax5.scatter(d['O III / Ne III'].get_value(8),d['Ar III / H-Alpha'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax5.scatter(d['O III / Ne III'].get_value(11),d['Ar III / H-Alpha'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax5.plot(basexvalO3Ne3,baseyvalAr3, c= '0')
ax5.plot(linxvalO3Ne3, linyvalAr3, c='0')
ax5.plot(lin16xvalO3Ne3,lin16yvalAr3, c = '0')
ax5.set_xlabel(r'Log$_{10}$([O III] $\lambda 5007$ / [Ne III] $\lambda 3869$')
ax5.set_ylabel(r'Log$_{10}$([Ar III] $\lambda 7135$ / H$\alpha$)')
ax5.set_xlim(-1,3)
ax5.set_ylim(-4,1.5)


ax6.scatter(np.log10(np.divide(SDSS_Data_HeII[:,23],SDSS_Data_HeII[:,18])),np.log10(np.divide(SDSS_Data_HeII[:,20], SDSS_Data_HeII[:,18])),edgecolor = '', c = '#000080', s = 5)
ax6.scatter(np.log10(np.divide(AGN_Array2[:,23],AGN_Array2[:,18])),np.log10(np.divide(AGN_Array2[:,20], AGN_Array2[:,18])),edgecolor = '', c = '#800000', s = 5)
ax6.scatter(d['He I / H-Beta'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax6.scatter(d['He I / H-Beta'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax6.scatter(d['He I / H-Beta'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax6.scatter(d['He I / H-Beta'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax6.scatter(d['He I / H-Beta'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax6.scatter(d['He I / H-Beta'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax6.scatter(d['He I / H-Beta'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax6.scatter(d['He I / H-Beta'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")

ax6.scatter(d['He I / H-Beta'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax6.scatter(d['He I / H-Beta'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax6.scatter(d['He I / H-Beta'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax6.scatter(d['He I / H-Beta'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")

ax6.set_xlabel(r'Log$_{10}$([He I] $\lambda 5876$ / H$\beta$)')
ax6.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)')


plt.suptitle('AGN Metallicity Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
ax1.legend(loc = 'upper left', bbox_to_anchor= [-0.5,1], fontsize = 'small')

#Display the figure full screen
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show() 
