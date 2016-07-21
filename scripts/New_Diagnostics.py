# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 13:23:16 2016

@author: chris_000
"""


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
            #print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  3203A','HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','AR 4  4740A','N  1  5200A',
            'TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m']))
            d = pd.concat(dfs, ignore_index=True)
        elif name.startswith('Linear_Fit_ax117') and name.endswith('.lin'):
           # print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'N  1  5200A', 'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A', 'AR 4  4740A',
            'NE 3  3869A','AR 3  7135A','HE 2  3203A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m']))
            d = pd.concat(dfs, ignore_index=True)
        elif name.startswith('Hden25') and name.endswith('.lin'):
             #print name
            #only read columns from list cols
             dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'N  1  5200A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  3203A', 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','AR 4  4740A', 'TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m']))
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

d['Ne V / Ne III'] = np.log10(np.divide(d['NE 5  3426A'], d['NE 3  3869A']))

d['He II / He I'] = np.log10(np.divide(d['HE 2  4686A'], d['HE 1  5876A']))

d['Ar IV / H-Beta'] = np.log10(np.divide(d['AR 4  4740A'], d['TOTL  4861A']))

d['O III / Ar IV'] = np.log10(np.divide(d['O  3  5007A'], d['AR 4  4740A']))

d['He II / He II'] = np.log10(np.divide(d['HE 2  4686A'], d['HE 2  3203A']))

d['N I / He I'] = np.log10(np.divide(d['N  1  5200A'], d['HE 1  5876A']))
#Plot these data points
SDSS_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/flux_norm.csv'
Shirazi_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/shirazi12.csv'
SDSS_Ratios_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/flux_norm_AGN.csv'
SDSS_HeII_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/HeII_z_lt_1.csv'
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

errorconditionNeV = SDSS_Data_HeII[:,6] > 3*SDSS_Data_HeII[:,33]
errorconditionNeIII = SDSS_Data_HeII[:,9] > 3*SDSS_Data_HeII[:,36]
errorconditionHeII = SDSS_Data_HeII[:,15] > 3*SDSS_Data_HeII[:,42]
errorconditionHeI = SDSS_Data_HeII[:,23] > 3*SDSS_Data_HeII[:,50]
errorconditionArIV = SDSS_Data_HeII[:,17] > 3*SDSS_Data_HeII[:,43]
errorconditionNI = SDSS_Data_HeII[:,22] > 3*SDSS_Data_HeII[:,49]
errorconditionHeII3202 = SDSS_Data_HeII[:, 4] > 3*SDSS_Data_HeII[:,31]
NeVErr1 = SDSS_Data_HeII[(errorconditionNeV & errorconditionNeIII & errorconditionHeII & errorconditionHeI),:]
NeVErr2 = SDSS_Data_HeII[(errorconditionNeV & errorconditionNeIII & errorconditionArIV),:]
NeVErr3 = SDSS_Data_HeII[(errorconditionNeV & errorconditionNeIII),:]
HeIIErr = SDSS_Data_HeII[(errorconditionHeII & errorconditionHeII3202),:]
N1Err = SDSS_Data_HeII[(errorconditionNI & errorconditionNeIII),:]

NeVHecondition1 = np.log10(np.divide(NeVErr1[:,20],NeVErr1[:,18])) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(np.divide(NeVErr1[:,28],NeVErr1[:,27])),.47)))
NeVHecondition2a = np.log10(np.divide(NeVErr1[:,20],NeVErr1[:,18])) > np.add(1.3,np.multiply(1.18,np.log10(np.divide(NeVErr1[:,24],NeVErr1[:,27]))))  #From Kewley et al. 2006
NeVHecondition2b = np.log10(np.divide(NeVErr1[:,20],NeVErr1[:,18])) > np.add(1.33, np.divide(0.73, np.add(np.log10(np.divide(NeVErr1[:,24],NeVErr1[:,27])),.59)))
NeVHecondition3a = np.log10(np.divide(NeVErr1[:,20],NeVErr1[:,18])) > np.add(0.76, np.multiply(1.89,np.log10(np.divide(np.add(NeVErr1[:,29],NeVErr1[:,30]),NeVErr1[:,27]))))
NeVHecondition3b = np.log10(np.divide(NeVErr1[:,20],NeVErr1[:,18])) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(np.divide(np.add(NeVErr1[:,29],NeVErr1[:,30]),NeVErr1[:,27])),0.32)))

ArIVHecondition1 = np.log10(np.divide(NeVErr2[:,20],NeVErr2[:,18])) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(np.divide(NeVErr2[:,28],NeVErr2[:,27])),.47)))
ArIVHecondition2a = np.log10(np.divide(NeVErr2[:,20],NeVErr2[:,18])) > np.add(1.3,np.multiply(1.18,np.log10(np.divide(NeVErr2[:,24],NeVErr2[:,27]))))  #From Kewley et al. 2006
ArIVHecondition2b = np.log10(np.divide(NeVErr2[:,20],NeVErr2[:,18])) > np.add(1.33, np.divide(0.73, np.add(np.log10(np.divide(NeVErr2[:,24],NeVErr2[:,27])),.59)))
ArIVHecondition3a = np.log10(np.divide(NeVErr2[:,20],NeVErr2[:,18])) > np.add(0.76, np.multiply(1.89,np.log10(np.divide(np.add(NeVErr2[:,29],NeVErr2[:,30]),NeVErr2[:,27]))))
ArIVHecondition3b = np.log10(np.divide(NeVErr2[:,20],NeVErr2[:,18])) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(np.divide(np.add(NeVErr2[:,29],NeVErr2[:,30]),NeVErr2[:,27])),0.32)))


HeIIcondition1 = np.log10(np.divide(HeIIErr[:,20],HeIIErr[:,18])) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(np.divide(HeIIErr[:,28],HeIIErr[:,27])),.47)))
HeIIcondition2a = np.log10(np.divide(HeIIErr[:,20],HeIIErr[:,18])) > np.add(1.3,np.multiply(1.18,np.log10(np.divide(HeIIErr[:,24],HeIIErr[:,27]))))  #From Kewley et al. 2006
HeIIcondition2b = np.log10(np.divide(HeIIErr[:,20],HeIIErr[:,18])) > np.add(1.33, np.divide(0.73, np.add(np.log10(np.divide(HeIIErr[:,24],HeIIErr[:,27])),.59)))
HeIIcondition3a = np.log10(np.divide(HeIIErr[:,20],HeIIErr[:,18])) > np.add(0.76, np.multiply(1.89,np.log10(np.divide(np.add(HeIIErr[:,29],HeIIErr[:,30]),HeIIErr[:,27]))))
HeIIcondition3b = np.log10(np.divide(HeIIErr[:,20],HeIIErr[:,18])) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(np.divide(np.add(HeIIErr[:,29],HeIIErr[:,30]),HeIIErr[:,27])),0.32)))

NIcondition1 = np.log10(np.divide(N1Err[:,20],N1Err[:,18])) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(np.divide(N1Err[:,28],N1Err[:,27])),.47)))
NIcondition2a = np.log10(np.divide(N1Err[:,20],N1Err[:,18])) > np.add(1.3,np.multiply(1.18,np.log10(np.divide(N1Err[:,24],N1Err[:,27]))))  #From Kewley et al. 2006
NIcondition2b = np.log10(np.divide(N1Err[:,20],N1Err[:,18])) > np.add(1.33, np.divide(0.73, np.add(np.log10(np.divide(N1Err[:,24],N1Err[:,27])),.59)))
NIcondition3a = np.log10(np.divide(N1Err[:,20],N1Err[:,18])) > np.add(0.76, np.multiply(1.89,np.log10(np.divide(np.add(N1Err[:,29],N1Err[:,30]),N1Err[:,27]))))
NIcondition3b = np.log10(np.divide(N1Err[:,20],N1Err[:,18])) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(np.divide(np.add(N1Err[:,29],N1Err[:,30]),N1Err[:,27])),0.32)))

mask = (condition1 & (condition2a & condition2b) & (condition3a & condition3b))
mask2 = (Hecondition1 & Hecondition2a & Hecondition2b & (Hecondition3a & Hecondition3b))
mask3 = (NeVHecondition1 & NeVHecondition2a & NeVHecondition2b & (NeVHecondition3a & NeVHecondition3b))
mask4 = (ArIVHecondition1 & ArIVHecondition2a & ArIVHecondition2b & (ArIVHecondition3a & ArIVHecondition3b))
mask5 = (HeIIcondition1 & HeIIcondition2a & HeIIcondition2b & (HeIIcondition3a & HeIIcondition3b))
mask6 = (NIcondition1 & NIcondition2a & NIcondition2b & (NIcondition3a & NIcondition3b))
AGN_Array= SDSS_Data_Ratios[mask,:]
AGN_Array2 = SDSS_Data_HeII[mask2,:]
AGN_Array3 = NeVErr1[mask3,:]
AGN_Array4 = NeVErr2[mask4,:]
AGN_Array5 = HeIIErr[mask5,:]
AGN_Array6 = N1Err[mask6, :]

ax1 = plt.subplot(231, adjustable = 'box-forced', autoscale_on = False)
ax2 = plt.subplot(232, adjustable = 'box-forced')
ax3 = plt.subplot(233,  adjustable = 'box-forced')
ax4 = plt.subplot(234, adjustable = 'box-forced')
ax5 = plt.subplot(235)
ax6 = plt.subplot(236)
z = [10^4,10^5, 10^6, 10^7]
x1=np.arange(-2,0.3,0.01)
y1=1.19+np.divide(0.61,x1-0.47)
x2=np.arange(-2,0,0.01)
y2 = 1.3+np.divide(0.61,x2-0.05)



#Make arrays for that have just the data from AGN

color5 = np.where(Shirazi_Data[6] >= np.subtract(np.divide(1,np.add(np.multiply(8.92, Shirazi_Data[7]),1.32)),1.22),1,0)


ax1.scatter(np.log10(np.divide(NeVErr1[:,6],NeVErr1[:,9])),np.log10(np.divide(NeVErr1[:,15],NeVErr1[:,23])) , c = '#000080', edgecolor = '', s = 10)
ax1.scatter(np.log10(np.divide(AGN_Array3[:,6],AGN_Array3[:,9])),np.log10(np.divide(AGN_Array3[:,15],AGN_Array3[:,23])) , c = '#800000',edgecolor = '', s = 10)
ax1.scatter(d['Ne V / Ne III'].get_value(0),d['He II / He I'].get_value(0), marker = "s",c='#FF5D5D', s = 50, label = "10^4")
ax1.scatter(d['Ne V / Ne III'].get_value(3),d['He II / He I'].get_value(3), marker = "s",c='#FF0000', s = 50, label = "10^5")
ax1.scatter(d['Ne V / Ne III'].get_value(6),d['He II / He I'].get_value(6), marker = "s",c='#C60000', s = 50, label = "10^6")
ax1.scatter(d['Ne V / Ne III'].get_value(9),d['He II / He I'].get_value(9), marker = "s",c='#9B0000', s = 50, label = "10^7")

ax1.scatter(d['Ne V / Ne III'].get_value(1),d['He II / He I'].get_value(1), marker = "s",c='#7056C5', s = 50, label = "10^4 ax=1.17")
ax1.scatter(d['Ne V / Ne III'].get_value(4),d['He II / He I'].get_value(4), marker = "s",c='#3914AF', s = 50, label = "10^5 ax=1.17")
ax1.scatter(d['Ne V / Ne III'].get_value(7),d['He II / He I'].get_value(7), marker = "s",c='#2B0E87', s = 50, label = "10^6 ax=1.17")
ax1.scatter(d['Ne V / Ne III'].get_value(10),d['He II / He I'].get_value(10), marker = "s",c='#200969', s = 50, label = "10^7 ax=1.17")

ax1.scatter(d['Ne V / Ne III'].get_value(2),d['He II / He I'].get_value(2), marker = "s",c='#50DA50', s = 50, label = "10^4 ax=2.9")
ax1.scatter(d['Ne V / Ne III'].get_value(5),d['He II / He I'].get_value(5), marker = "s",c='#00CC00', s = 50, label = "10^5 ax=2.9")
ax1.scatter(d['Ne V / Ne III'].get_value(8),d['He II / He I'].get_value(8), marker = "s",c='#009D00', s = 50, label = "10^6 ax=2.9")
ax1.scatter(d['Ne V / Ne III'].get_value(11),d['He II / He I'].get_value(11), marker = "s",c='#007A00', s = 50, label = "10^7 ax=2.9")
#ax1.plot(basexvalO3A3, baseyvalueNe3, c = '0')
#ax1.plot(linxval03A3,linyvalNe3,c = '0')
#ax1.plot(lin16xval03A3,lin16yvalNe3, c = '0')
ax1.set_xlim(-3,2)
ax1.set_ylim(-1,2)
ax1.set_xlabel(r'Log$_{10}$([Ne V] $\lambda 3426$ / [Ne III] $\lambda 3868$)', fontsize = 20)
ax1.set_ylabel(r'Log$_{10}$([He II] $\lambda 4686$ / [He I] $\lambda 5876$)', fontsize = 20)


ax2.scatter(np.log10(np.divide(NeVErr2[:,6],NeVErr2[:,9])),np.log10(np.divide(NeVErr2[:,17],NeVErr2[:,19])),edgecolor = '', c = '#000080',s = 10)
ax2.scatter(np.log10(np.divide(AGN_Array4[:,6],AGN_Array4[:,9])),np.log10(np.divide(AGN_Array4[:,17],AGN_Array4[:,19])),edgecolor = '', s = 10, c = '#800000')
ax2.scatter(d['Ne V / Ne III'].get_value(0),d['Ar IV / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 50, label = "10^4")
ax2.scatter(d['Ne V / Ne III'].get_value(3),d['Ar IV / H-Beta'].get_value(2), marker = "s",c='#FF0000', s = 50, label = "10^5")
ax2.scatter(d['Ne V / Ne III'].get_value(6),d['Ar IV / H-Beta'].get_value(4), marker = "s",c='#C60000', s = 50, label = "10^6")
ax2.scatter(d['Ne V / Ne III'].get_value(9),d['Ar IV / H-Beta'].get_value(6), marker = "s",c='#9B0000', s = 50, label = "10^7")

ax2.scatter(d['Ne V / Ne III'].get_value(1),d['Ar IV / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 50, label = "10^4 Fit")
ax2.scatter(d['Ne V / Ne III'].get_value(4),d['Ar IV / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 50, label = "10^5 Fit")
ax2.scatter(d['Ne V / Ne III'].get_value(7),d['Ar IV / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 50, label = "10^6 Fit ")
ax2.scatter(d['Ne V / Ne III'].get_value(10),d['Ar IV / H-Beta'].get_value(10), marker = "s",c='#200969', s = 50, label = "10^7 Fit")

ax2.scatter(d['Ne V / Ne III'].get_value(2),d['Ar IV / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 50, label = "10^4 Fit")
ax2.scatter(d['Ne V / Ne III'].get_value(5),d['Ar IV / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 50, label = "10^5 Fit")
ax2.scatter(d['Ne V / Ne III'].get_value(8),d['Ar IV / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 50, label = "10^6 Fit ")
ax2.scatter(d['Ne V / Ne III'].get_value(11),d['Ar IV / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 50, label = "10^7 Fit")
#ax2.plot(basexvalO2N2,baseyvalS2,c = '0')
#ax2.plot(linxvalO2N2,linyvalS2, c = '0')
#ax2.plot(lin16xvalO2N2,lin16yvalS2, c = '0')
ax2.set_xlabel(r'Log$_{10}$([Ne V] $\lambda 3426$ / [Ne III] $\lambda 3868$)', fontsize = 20)
ax2.set_ylabel(r'Log$_{10}$([Ar IV] $\lambda 4740$ / H$\beta$)', fontsize = 20)
ax2.set_xlim(-5,5)
ax2.set_ylim(-5,5)



ax3.scatter(np.log10(np.divide(NeVErr3[:,6],NeVErr3[:,9])),np.log10(np.divide(NeVErr3[:,20],NeVErr3[:,18])), edgecolor = '', c = '#000080',s=10)
ax3.scatter(np.log10(np.divide(AGN_Array3[:,6],AGN_Array3[:,9])),np.log10(np.divide(AGN_Array3[:,20], AGN_Array3[:,18])), edgecolor = '', c = '#800000', s = 10)
ax3.scatter(d['Ne V / Ne III'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 50, label = "10^4")
ax3.scatter(d['Ne V / Ne III'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 50, label = "10^5")
ax3.scatter(d['Ne V / Ne III'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 50, label = "10^6")
ax3.scatter(d['Ne V / Ne III'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 50, label = "10^7")
ax3.scatter(d['Ne V / Ne III'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 50, label = "10^4")
ax3.scatter(d['Ne V / Ne III'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 50, label = "10^5")
ax3.scatter(d['Ne V / Ne III'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 50, label = "10^6")
ax3.scatter(d['Ne V / Ne III'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 50, label = "10^7")
ax3.scatter(d['Ne V / Ne III'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 50, label = "10^4")
ax3.scatter(d['Ne V / Ne III'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 50, label = "10^5")
ax3.scatter(d['Ne V / Ne III'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 50, label = "10^6")
ax3.scatter(d['Ne V / Ne III'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 50, label = "10^7")

ax3.set_xlim(-3,3)
#ax3.set_ylim(np.log10(10**(-1.5)), np.log10(10**(2)))
ax3.set_xlabel(r'Log$_{10}$([Ne V] $\lambda 3426$ / [Ne III] $\lambda 3868$)', fontsize = 20)
ax3.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)', fontsize = 20)


ax4.scatter(np.log10(np.divide(HeIIErr[:,15],HeIIErr[:,4])),np.log10(np.divide(HeIIErr[:,29],HeIIErr[:,30])),edgecolor = '', c = '#000080',s = 10)
ax4.scatter(np.log10(np.divide(AGN_Array5[:,15],AGN_Array5[:,4])),np.log10(np.divide(AGN_Array5[:,29], AGN_Array5[:,30])),edgecolor = '', s = 10, c = '#800000')
ax4.scatter(d['He II / He II'].get_value(0),d['S II 6716/ S II 6731'].get_value(0), marker = "s",c='#FF5D5D', s = 50, label = "10^4")
ax4.scatter(d['He II / He II'].get_value(3),d['S II 6716/ S II 6731'].get_value(3), marker = "s",c='#FF0000', s = 50, label = "10^5")
ax4.scatter(d['He II / He II'].get_value(6),d['S II 6716/ S II 6731'].get_value(6), marker = "s",c='#C60000', s = 50, label = "10^6")
ax4.scatter(d['He II / He II'].get_value(9),d['S II 6716/ S II 6731'].get_value(9), marker = "s",c='#9B0000', s = 50, label = "10^7")
ax4.scatter(d['He II / He II'].get_value(1),d['S II 6716/ S II 6731'].get_value(1), marker = "s",c='#7056C5', s = 50, label = "10^4")
ax4.scatter(d['He II / He II'].get_value(4),d['S II 6716/ S II 6731'].get_value(4), marker = "s",c='#3914AF', s = 50, label = "10^5")
ax4.scatter(d['He II / He II'].get_value(7),d['S II 6716/ S II 6731'].get_value(7), marker = "s",c='#2B0E87', s = 50, label = "10^6")
ax4.scatter(d['He II / He II'].get_value(10),d['S II 6716/ S II 6731'].get_value(10), marker = "s",c='#200969', s = 50, label = "10^7")
ax4.scatter(d['He II / He II'].get_value(2),d['S II 6716/ S II 6731'].get_value(2), marker = "s",c='#50DA50', s = 50, label = "10^4")
ax4.scatter(d['He II / He II'].get_value(5),d['S II 6716/ S II 6731'].get_value(5), marker = "s",c='#00CC00', s = 50, label = "10^5")
ax4.scatter(d['He II / He II'].get_value(8),d['S II 6716/ S II 6731'].get_value(8), marker = "s",c='#009D00', s = 50, label = "10^6")
ax4.scatter(d['He II / He II'].get_value(11),d['S II 6716/ S II 6731'].get_value(11), marker = "s",c='#007A00', s = 50, label = "10^7")
#ax4.plot(basexvalO2N2,baseyvalO3, c = '0')
#ax4.plot(linxvalO2N2,linyvalO3, c = '0')
#ax4.plot(lin16xvalO2N2, lin16yvalO3, c = '0')
ax4.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)', fontsize = 20)
ax4.set_xlabel(r'Log$_{10}$([O III] $\lambda 5007$ / [Ne III] $\lambda 3869$)', fontsize = 20)
ax4.set_xlim(-2,2)
ax4.set_ylim(-2,2)


ax5.scatter(np.log10(np.divide(HeIIErr[:,15],HeIIErr[:,4])),np.log10(np.divide(HeIIErr[:,20],HeIIErr[:,18])),edgecolor = '', c = '#000080',s = 10)
ax5.scatter(np.log10(np.divide(AGN_Array5[:,15],AGN_Array5[:,4])),np.log10(np.divide(AGN_Array5[:,20], AGN_Array5[:,18])),edgecolor = '', s = 10, c = '#800000')
ax5.scatter(d['He II / He II'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 50, label = "10^4")
ax5.scatter(d['He II / He II'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 50, label = "10^5")
ax5.scatter(d['He II / He II'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 50, label = "10^6")
ax5.scatter(d['He II / He II'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 50, label = "10^7")

ax5.scatter(d['He II / He II'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 50, label = "10^4")
ax5.scatter(d['He II / He II'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 50, label = "10^5")
ax5.scatter(d['He II / He II'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 50, label = "10^6")
ax5.scatter(d['He II / He II'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 50, label = "10^7")

ax5.scatter(d['He II / He II'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 50, label = "10^4")
ax5.scatter(d['He II / He II'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 50, label = "10^5")
ax5.scatter(d['He II / He II'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 50, label = "10^6")
ax5.scatter(d['He II / He II'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 50, label = "10^7")
#ax5.plot(basexvalO3Ne3,baseyvalAr3, c= '0')
#ax5.plot(linxvalO3Ne3, linyvalAr3, c='0')
#ax5.plot(lin16xvalO3Ne3,lin16yvalAr3, c = '0')
ax5.set_xlabel(r'Log$_{10}$([He II] $\lambda 4686$ / [He II] $\lambda 3203$)', fontsize = 20)
ax5.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / H$\beta$)', fontsize = 20)
ax5.set_xlim(-1,3)
ax5.set_ylim(-1,3)

ax6.scatter(np.log10(np.divide(N1Err[:,22],N1Err[:,23])),np.log10(np.divide(N1Err[:,20],N1Err[:,9])),edgecolor = '', c = '#000080',s = 10)
ax6.scatter(np.log10(np.divide(AGN_Array6[:,22],AGN_Array6[:,23])),np.log10(np.divide(AGN_Array6[:,20], AGN_Array6[:,9])),edgecolor = '', s = 10, c = '#800000')
ax6.scatter(d['N I / He I'].get_value(0),d['O III / Ne III'].get_value(0), marker = "s",c='#FF5D5D', s = 50, label = "10^4")
ax6.scatter(d['N I / He I'].get_value(3),d['O III / Ne III'].get_value(3), marker = "s",c='#FF0000', s = 50, label = "10^5")
ax6.scatter(d['N I / He I'].get_value(6),d['O III / Ne III'].get_value(6), marker = "s",c='#C60000', s = 50, label = "10^6")
ax6.scatter(d['N I / He I'].get_value(9),d['O III / Ne III'].get_value(9), marker = "s",c='#9B0000', s = 50, label = "10^7")

ax6.scatter(d['N I / He I'].get_value(1),d['O III / Ne III'].get_value(1), marker = "s",c='#7056C5', s = 50, label = "10^4")
ax6.scatter(d['N I / He I'].get_value(4),d['O III / Ne III'].get_value(4), marker = "s",c='#3914AF', s = 50, label = "10^5")
ax6.scatter(d['N I / He I'].get_value(7),d['O III / Ne III'].get_value(7), marker = "s",c='#2B0E87', s = 50, label = "10^6")
ax6.scatter(d['N I / He I'].get_value(10),d['O III / Ne III'].get_value(10), marker = "s",c='#200969', s = 50, label = "10^7")

ax6.scatter(d['N I / He I'].get_value(2),d['O III / Ne III'].get_value(2), marker = "s",c='#50DA50', s = 50, label = "10^4")
ax6.scatter(d['N I / He I'].get_value(5),d['O III / Ne III'].get_value(5), marker = "s",c='#00CC00', s = 50, label = "10^5")
ax6.scatter(d['N I / He I'].get_value(8),d['O III / Ne III'].get_value(8), marker = "s",c='#009D00', s = 50, label = "10^6")
ax6.scatter(d['N I / He I'].get_value(11),d['O III / Ne III'].get_value(11), marker = "s",c='#007A00', s = 50, label = "10^7")
ax6.set_xlim(-2,2.5)
ax6.set_ylim(-1,3)

ax6.set_xlabel(r'Log$_{10}$([N I] $\lambda 5200$ / [He I] $\lambda 5876$)', fontsize = 20)
ax6.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$ / [Ne III] $\lambda 3869$)', fontsize = 20)
#plt.suptitle('AGN Metallicity Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
ax1.legend(loc = 'upper left', bbox_to_anchor= [-0.5,1], fontsize = 'small')

#Display the figure full screen

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()
