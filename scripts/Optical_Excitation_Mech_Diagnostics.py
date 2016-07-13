#Import required modules
import matplotlib.pyplot as plt
import matplotlib.colors as cm
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


normSource=os.path.normpath(rootdirectory)

dfs=[] #Create an empty array for our Data

d=pd.DataFrame() 
d=d.reset_index()
d2=pd.DataFrame({'Temperature': [10**4,10**5, 10**6, 10**7]},dtype=float) #Create a Dataframe of labels for each file used
Output_File=r'C:/Users/chris_000/Documents/GitHub/AGN_SED/All_Emissions.csv' #Create the output file

for root, dirs, files in os.walk(rootdirectory, topdown=False):
    for name in files:
        if name.startswith('Linear_Fit_ax219') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A']))
            d = pd.concat(dfs, ignore_index=True)
        if name.startswith('Linear_Fit_ax117') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A']))
        if name.startswith('Hden25') and name.endswith('.lin'):
             print name
            #only read columns from list cols
             dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A']))
             d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2
d['O III / H-Beta']= np.log10(d['O  3  5007A'] / d['TOTL  4861A'])

d['O I / H-Alpha']=np.log10(np.divide(d['O  1  6300A'],d['H  1  6563A']))

d['N II / H-Alpha']=np.log10(d['N  2  6584A'] / d['H  1  6563A'])

d['S II / H-Alpha']=np.log10(np.divide(d['S  2  6720A'],d['H  1  6563A']))

d['O II / O III'] = np.log10(np.divide(d['TOTL  3727A'],d['O  3  5007A']))

d['O II / H-Beta'] = np.log10(np.divide(d['TOTL  3727A'], d['TOTL  4861A'])) 

d['O III / O II'] = np.log10(np.divide(d['O  3  5007A'],d['TOTL  3727A']))

d['He II / H-Beta'] = np.log10(np.divide(d['HE 2  4686A'],d['TOTL  4861A']))


#Plot these data points
SDSS_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/flux_norm.csv'
Shirazi_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/Shirazi12_Only_Data.csv'
SDSS_Ratios_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/flux_norm_AGN.csv'
SDSS_HeII_File = r'C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/HeII_sample.csv'
SDSS_Data=np.genfromtxt(SDSS_File, skip_header=1, delimiter = ',',dtype=float,unpack=True)
Shirazi_Data=np.genfromtxt(Shirazi_File, skip_header=3, delimiter = ',',dtype = float)
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
condition5a = Shirazi_Data[:,0] >= np.add(-1.22, np.divide(1,np.add(np.multiply(8.92,Shirazi_Data[:,1]),1.32)))
condition5b = Shirazi_Data[:,1] >= -0.2

Hecondition1 = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.19, np.divide(0.61, np.subtract(np.log10(np.divide(SDSS_Data_HeII[:,28],SDSS_Data_HeII[:,27])),.47)))
Hecondition2a = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.3,np.multiply(1.18,np.log10(np.divide(SDSS_Data_HeII[:,24],SDSS_Data_HeII[:,27]))))  #From Kewley et al. 2006
Hecondition2b = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.33, np.divide(0.73, np.add(np.log10(np.divide(SDSS_Data_HeII[:,24],SDSS_Data_HeII[:,27])),.59)))
Hecondition3a = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(0.76, np.multiply(1.89,np.log10(np.divide(np.add(SDSS_Data_HeII[:,29],SDSS_Data_HeII[:,30]),SDSS_Data_HeII[:,27]))))
Hecondition3b = np.log10(np.divide(SDSS_Data_HeII[:,20],SDSS_Data_HeII[:,18])) > np.add(1.30,np.divide(0.72, np.subtract(np.log10(np.divide(np.add(SDSS_Data_HeII[:,29],SDSS_Data_HeII[:,30]),SDSS_Data_HeII[:,27])),0.32)))
mask = (condition1 & (condition2a & condition2b) & (condition3a & condition3b))

AGN_Array= SDSS_Data_Ratios[mask,:]
mask2 = (Hecondition1 & Hecondition2a & Hecondition2b & (Hecondition3a & Hecondition3b))

AGN_Array2 = SDSS_Data_HeII[mask2,:]


ax1 = plt.subplot(231, adjustable = 'box-forced', autoscale_on = False)
ax2 = plt.subplot(232, adjustable = 'box-forced', autoscale_on = False)
ax3 = plt.subplot(233, adjustable = 'box-forced', autoscale_on = False)
ax4 = plt.subplot(234, adjustable = 'box-forced', autoscale_on = False)
ax5 = plt.subplot(235, adjustable = 'box-forced', autoscale_on = False)
ax6 = plt.subplot(236, adjustable = 'box-forced', autoscale_on = False)
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

ax1.scatter(np.log10(SDSS_Data_Ratios[:,7]),np.log10(SDSS_Data_Ratios[:,8]),  marker = 'o',edgecolor = '', c = '#000080',s = 5)
ax1.scatter(np.log10(AGN_Array[:,7]),np.log10(AGN_Array[:,8]),edgecolor = '', s = 5, c = '#800000')
basexvalues = (d['N II / H-Alpha'].get_value(0),d['N II / H-Alpha'].get_value(3),d['N II / H-Alpha'].get_value(6),d['N II / H-Alpha'].get_value(9))
baseyvalues = (d['O III / H-Beta'].get_value(0),d['O III / H-Beta'].get_value(3),d['O III / H-Beta'].get_value(6),d['O III / H-Beta'].get_value(9))
linearxvalues = (d['N II / H-Alpha'].get_value(1),d['N II / H-Alpha'].get_value(4),d['N II / H-Alpha'].get_value(7),d['N II / H-Alpha'].get_value(10))
linearyvalues = (d['O III / H-Beta'].get_value(1),d['O III / H-Beta'].get_value(4),d['O III / H-Beta'].get_value(7),d['O III / H-Beta'].get_value(10))
linear16xvalues = (d['N II / H-Alpha'].get_value(2),d['N II / H-Alpha'].get_value(5),d['N II / H-Alpha'].get_value(8),d['N II / H-Alpha'].get_value(11))
linear16yvalues = (d['O III / H-Beta'].get_value(2),d['O III / H-Beta'].get_value(5),d['O III / H-Beta'].get_value(8),d['O III / H-Beta'].get_value(11))
l1 = ax1.scatter(d['N II / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s", c = '#FF5D5D', s = 30, label = "10^4")
l2 = ax1.scatter(d['N II / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s", c = '#FF0000', s = 30, label = "10^5")
l3 = ax1.scatter(d['N II / H-Alpha'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s", c = '#C60000',s = 30, label = "10^6")
l4 = ax1.scatter(d['N II / H-Alpha'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s", c = '#9B0000', s = 30, label = "10^7")
l5 = ax1.scatter(d['N II / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4 ax=1.17")
l6 = ax1.scatter(d['N II / H-Alpha'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5 ax=1.17")
l7 = ax1.scatter(d['N II / H-Alpha'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6 ax=1.17")
l8 = ax1.scatter(d['N II / H-Alpha'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7 ax=1.17")
l9 = ax1.scatter(d['N II / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4 ax=2.19")
l10 = ax1.scatter(d['N II / H-Alpha'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5 ax=2.19")
l11 = ax1.scatter(d['N II / H-Alpha'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6 ax=2.19")
l12 = ax1.scatter(d['N II / H-Alpha'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7 ax=2.19")
ax1.plot(x1,y1,c = '0',linewidth = 2)
ax1.plot(x2,y2, c = '0',ls = '--', lw = 2)
ax1.plot(linear16xvalues,linear16yvalues, c='0')
ax1.plot(basexvalues,baseyvalues, c = '0')
ax1.plot(linearxvalues, linearyvalues, ls = '--', c = '0')
ax1.plot(linear16xvalues,linear16yvalues,ls = ':', c = '0')
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
basexvalues2 = (d['O I / H-Alpha'].get_value(0),d['O I / H-Alpha'].get_value(3),d['O I / H-Alpha'].get_value(6),d['O I / H-Alpha'].get_value(9))
baseyvalues2 = (d['O III / H-Beta'].get_value(0),d['O III / H-Beta'].get_value(3),d['O III / H-Beta'].get_value(6),d['O III / H-Beta'].get_value(9))

linxvalues2 = (d['O I / H-Alpha'].get_value(1),d['O I / H-Alpha'].get_value(4),d['O I / H-Alpha'].get_value(7),d['O I / H-Alpha'].get_value(10))

lin16xvalues2 = (d['O I / H-Alpha'].get_value(2),d['O I / H-Alpha'].get_value(5),d['O I / H-Alpha'].get_value(8),d['O I / H-Alpha'].get_value(11))
ax2.scatter(np.log10(SDSS_Data_Ratios[:,5]),np.log10(SDSS_Data_Ratios[:,8]), edgecolor = '', c = '#000080', s=5)
ax2.scatter(np.log10(AGN_Array[:,5]),np.log10(AGN_Array[:,8]),edgecolor = '', s = 5, c = '#800000')
ax2.scatter(d['O I / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax2.scatter(d['O I / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax2.scatter(d['O I / H-Alpha'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax2.scatter(d['O I / H-Alpha'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
ax2.scatter(d['O I / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax2.scatter(d['O I / H-Alpha'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax2.scatter(d['O I / H-Alpha'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax2.scatter(d['O I / H-Alpha'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
ax2.scatter(d['O I / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax2.scatter(d['O I / H-Alpha'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax2.scatter(d['O I / H-Alpha'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax2.scatter(d['O I / H-Alpha'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax2.plot(x3,y3,c = '0', ls = '-', linewidth = 2)
ax2.plot(basexvalues2, baseyvalues2, c = '0')
ax2.plot(linxvalues2, linearyvalues, ls = '--', c = '0')
ax2.plot(lin16xvalues2,linear16yvalues, ls = ':', lw = '3', c = '0')

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

basexvalues3 = (d['S II / H-Alpha'].get_value(0),d['S II / H-Alpha'].get_value(3),d['S II / H-Alpha'].get_value(6),d['S II / H-Alpha'].get_value(9))

linxvalues3 = (d['S II / H-Alpha'].get_value(1),d['S II / H-Alpha'].get_value(4),d['S II / H-Alpha'].get_value(7),d['S II / H-Alpha'].get_value(10))

lin16xvalues3 = (d['S II / H-Alpha'].get_value(2),d['S II / H-Alpha'].get_value(5),d['S II / H-Alpha'].get_value(8),d['S II / H-Alpha'].get_value(11))

ax3.scatter(np.log10(SDSS_Data_Ratios[:,18]),np.log10(SDSS_Data_Ratios[:,8]), edgecolor = '', c = '#000080',s=5.0)
ax3.scatter(np.log10(AGN_Array[:,18]),np.log10(AGN_Array[:,8]),edgecolor = '', c = '#800000', s = 5)
ax3.scatter(d['S II / H-Alpha'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax3.scatter(d['S II / H-Alpha'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax3.scatter(d['S II / H-Alpha'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax3.scatter(d['S II / H-Alpha'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")

ax3.scatter(d['S II / H-Alpha'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax3.scatter(d['S II / H-Alpha'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax3.scatter(d['S II / H-Alpha'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax3.scatter(d['S II / H-Alpha'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
ax3.scatter(d['S II / H-Alpha'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax3.scatter(d['S II / H-Alpha'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax3.scatter(d['S II / H-Alpha'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax3.scatter(d['S II / H-Alpha'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax3.plot(x5,y5, c='0',ls = '-',linewidth=2)
ax3.plot(x6,y6, c='0',ls = '--',linewidth=3.0)
ax3.plot(basexvalues3, baseyvalues, c = '0')
ax3.plot(linxvalues3, linearyvalues, ls = '--', c = '0')
ax3.plot(lin16xvalues3,linear16yvalues, ls = ':', lw = '3', c = '0')
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

basexvalues4 = (d['O II / H-Beta'].get_value(0),d['O II / H-Beta'].get_value(3),d['O II / H-Beta'].get_value(6),d['O II / H-Beta'].get_value(9))
linxvalues4 = (d['O II / H-Beta'].get_value(1),d['O II / H-Beta'].get_value(4),d['O II / H-Beta'].get_value(7),d['O II / H-Beta'].get_value(10))
lin16xvalues4 = (d['O II / H-Beta'].get_value(2),d['O II / H-Beta'].get_value(5),d['O II / H-Beta'].get_value(8),d['O II / H-Beta'].get_value(11))
ax4.scatter(np.log10(SDSS_Data_Ratios[:,0]),np.log10(SDSS_Data_Ratios[:,8]),edgecolor = '', c = '#000080',s=5)
ax4.scatter(np.log10(AGN_Array[:,0]),np.log10(AGN_Array[:,8]),edgecolor = '', c = '#800000',s=5)
ax4.scatter(d['O II / H-Beta'].get_value(0),d['O III / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax4.scatter(d['O II / H-Beta'].get_value(3),d['O III / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax4.scatter(d['O II / H-Beta'].get_value(6),d['O III / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax4.scatter(d['O II / H-Beta'].get_value(9),d['O III / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
ax4.scatter(d['O II / H-Beta'].get_value(1),d['O III / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax4.scatter(d['O II / H-Beta'].get_value(4),d['O III / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax4.scatter(d['O II / H-Beta'].get_value(7),d['O III / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax4.scatter(d['O II / H-Beta'].get_value(10),d['O III / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
ax4.scatter(d['O II / H-Beta'].get_value(2),d['O III / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax4.scatter(d['O II / H-Beta'].get_value(5),d['O III / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax4.scatter(d['O II / H-Beta'].get_value(8),d['O III / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax4.scatter(d['O II / H-Beta'].get_value(11),d['O III / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax4.plot(x9,y9,x10,y10,c = '0', lw = 2)
ax4.axhline(y = 0.3,xmin = -2, xmax = 0.65, c = '0', lw =3)
ax4.plot(basexvalues4,baseyvalues, c = '0')
ax4.plot(linxvalues4,linearyvalues,ls = '--', c = '0')
ax4.plot(lin16xvalues4,linear16yvalues, ls = ':', lw = '3', c = '0')
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
baseyvalues5 = (d['He II / H-Beta'].get_value(0),d['He II / H-Beta'].get_value(3),d['He II / H-Beta'].get_value(6),d['He II / H-Beta'].get_value(9))
linyvalues5 = (d['He II / H-Beta'].get_value(1),d['He II / H-Beta'].get_value(4),d['He II / H-Beta'].get_value(7),d['He II / H-Beta'].get_value(10))
lin16yvalues5 = (d['He II / H-Beta'].get_value(2),d['He II / H-Beta'].get_value(5),d['He II / H-Beta'].get_value(8),d['He II / H-Beta'].get_value(11))
ax5.scatter(np.log10(np.divide(SDSS_Data_HeII[:,28],SDSS_Data_HeII[:,27])),np.log10(np.divide(SDSS_Data_HeII[:,15],SDSS_Data_HeII[:,18])), c ='#000080' ,edgecolor = '', s = 15)
ax5.scatter(np.log10(np.divide(AGN_Array2[:,28],AGN_Array2[:,27])),np.log10(np.divide(AGN_Array2[:,15],AGN_Array2[:,18])), c = '#800000',edgecolor = '', s = 15)
ax5.scatter(d['N II / H-Alpha'].get_value(0),d['He II / H-Beta'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax5.scatter(d['N II / H-Alpha'].get_value(3),d['He II / H-Beta'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax5.scatter(d['N II / H-Alpha'].get_value(6),d['He II / H-Beta'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax5.scatter(d['N II / H-Alpha'].get_value(9),d['He II / H-Beta'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
ax5.scatter(d['N II / H-Alpha'].get_value(1),d['He II / H-Beta'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax5.scatter(d['N II / H-Alpha'].get_value(4),d['He II / H-Beta'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax5.scatter(d['N II / H-Alpha'].get_value(7),d['He II / H-Beta'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax5.scatter(d['N II / H-Alpha'].get_value(10),d['He II / H-Beta'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
ax5.scatter(d['N II / H-Alpha'].get_value(2),d['He II / H-Beta'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax5.scatter(d['N II / H-Alpha'].get_value(5),d['He II / H-Beta'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax5.scatter(d['N II / H-Alpha'].get_value(8),d['He II / H-Beta'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax5.scatter(d['N II / H-Alpha'].get_value(11),d['He II / H-Beta'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax5.plot(x,y, c = '0', ls = '-', lw = 2.0)
ax5.plot(basexvalues,baseyvalues5, c ='0')
ax5.plot(linearxvalues, linyvalues5, ls = '--', c = '0')
ax5.plot(linear16xvalues,lin16yvalues5, ls = ':', lw = 3, c = '0')
ax5.set_xlim(-3,0.5)
ax5.set_ylim(-3,2)

ax5.set_xlabel(r'Log$_{10}$([N II] $\lambda 6584$ / H$\alpha$)')
ax5.set_ylabel(r'Log$_{10}$([He II] $\lambda 4686$ / H$\beta$)')
ax5.text(-1,-2.5, 'Starburst')
ax5.text(-2,0,'AGN')

x7 = np.arange(-2.5,1.5)
y7 = -1.701*x7-2.163
x8 = np.arange(-1.1,1)
y8 = 1.0*x8+0.7
baseyvalues6 = (d['O III / O II'].get_value(0),d['O III / O II'].get_value(3),d['O III / O II'].get_value(6),d['O III / O II'].get_value(9))
linyvalues6 = (d['O III / O II'].get_value(1),d['O III / O II'].get_value(4),d['O III / O II'].get_value(7),d['O III / O II'].get_value(10))
lin16yvalues6 = (d['O III / O II'].get_value(2),d['O III / O II'].get_value(5),d['O III / O II'].get_value(8),d['O III / O II'].get_value(11))
ax6.scatter(np.log10(SDSS_Data_Ratios[:,5]),np.log10(SDSS_Data_Ratios[:,2]),edgecolor = '', s = 5,c = '#000080', )
ax6.scatter(np.log10(O3O2AGN[:,5]), np.log10(O3O2AGN[:,2]), edgecolor = '', s = 5, c = '#800000')
ax6.scatter(d['O I / H-Alpha'].get_value(0),d['O III / O II'].get_value(0), marker = "s",c='#FF5D5D', s = 30, label = "10^4")
ax6.scatter(d['O I / H-Alpha'].get_value(3),d['O III / O II'].get_value(3), marker = "s",c='#FF0000', s = 30, label = "10^5")
ax6.scatter(d['O I / H-Alpha'].get_value(6),d['O III / O II'].get_value(6), marker = "s",c='#C60000', s = 30, label = "10^6")
ax6.scatter(d['O I / H-Alpha'].get_value(9),d['O III / O II'].get_value(9), marker = "s",c='#9B0000', s = 30, label = "10^7")
ax6.scatter(d['O I / H-Alpha'].get_value(1),d['O III / O II'].get_value(1), marker = "s",c='#7056C5', s = 30, label = "10^4")
ax6.scatter(d['O I / H-Alpha'].get_value(4),d['O III / O II'].get_value(4), marker = "s",c='#3914AF', s = 30, label = "10^5")
ax6.scatter(d['O I / H-Alpha'].get_value(7),d['O III / O II'].get_value(7), marker = "s",c='#2B0E87', s = 30, label = "10^6")
ax6.scatter(d['O I / H-Alpha'].get_value(10),d['O III / O II'].get_value(10), marker = "s",c='#200969', s = 30, label = "10^7")
ax6.scatter(d['O I / H-Alpha'].get_value(2),d['O III / O II'].get_value(2), marker = "s",c='#50DA50', s = 30, label = "10^4")
ax6.scatter(d['O I / H-Alpha'].get_value(5),d['O III / O II'].get_value(5), marker = "s",c='#00CC00', s = 30, label = "10^5")
ax6.scatter(d['O I / H-Alpha'].get_value(8),d['O III / O II'].get_value(8), marker = "s",c='#009D00', s = 30, label = "10^6")
ax6.scatter(d['O I / H-Alpha'].get_value(11),d['O III / O II'].get_value(11), marker = "s",c='#007A00', s = 30, label = "10^7")
ax6.plot(x7,y7, x8,y8, c = '0', lw = 3.0)
ax6.plot(basexvalues2,baseyvalues6, c = '0')
ax6.plot(linxvalues2,linyvalues6,ls = '--', c =  '0')
ax6.plot(lin16xvalues2,lin16yvalues6, ls = ':', lw = '3',c = '0')
ax6.set_xlim(-3,0.5)
ax6.set_ylim(-1.5,1.5)
ax6.set_xlabel(r'Log$_{10}$([O I] $\lambda 6300$ / H$\alpha$)')
ax6.set_ylabel(r'Log$_{10}$([O III] $\lambda 5007$) / [O II] $\lambda 3727$)')
ax6.text(-1.5,1,'Seyfert')
ax6.text(-0.1,0,'LINER')
ax6.text(-2.2,-1.3, 'Starburst')
plt.suptitle('AGN Excitation Mechanism Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
ax1.legend(loc = 'upper right', fontsize = 'small')

#Display the figure full screen
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show() 
plt.savefig('C:\Users\chris_000\Documents\GitHub\AGN_SED\Diagnostic_Plots\Optical\Separated_By_Diagnostic\With_Linear_Fit\Linear_Variations_Fixed\With_Weak_Lines\Excitation_Mechanism.png',dpi = 600)