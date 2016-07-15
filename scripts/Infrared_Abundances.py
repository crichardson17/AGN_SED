
#Import required modules
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import os
#List all the subdirectories within directory that have the data that we want
def filelist(directory): 
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.lin'):
                print (file)
                
rootdirectory='C:/Users/chris_000/Documents/GitHub/AGN_SED/Cloudy_Data' 

filelist(rootdirectory)

#Generate a CSV file containing all the relevant data points

Output_File=r'C:/Users/chris_000/Documents/GitHub/AGN_SED/All_Emissions.csv' #Create the output file

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
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m','S  4 10.51m']))
            d = pd.concat(dfs, ignore_index=True)
        elif name.startswith('Linear_Fit_ax117') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','S  4 10.51m','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m']))
            d = pd.concat(dfs, ignore_index=True)
        elif name.startswith('Hden25') and name.endswith('.lin'):
             print name
            #only read columns from list cols
             dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'S  4 10.51m','O II  3729A','O  4 25.88m','NE 2 12.81m','NE 5 14.32m','NE 5 24.31m','NE 3 15.55m']))
             d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2

d['O IV / Ne II'] = np.log10(np.divide(d['O  4 25.88m'], d['NE 2 12.81m']))
d['Ne V / Ne II'] = np.log10(np.divide(d['NE 5 14.32m'], d['NE 2 12.81m']))
d['Ne V / Ne III'] = np.log10(np.divide(d['NE 5 14.32m'], d['NE 3 15.55m']))
d['O IV / S IV'] = np.log10(np.divide(d['O  4 25.88m'],d['S  4 10.51m']))
d['Ne V / S IV'] = np.log10(np.divide(d['NE 5 14.32m'],d['S  4 10.51m']))
d['S IV / Ne II'] = np.log10(np.divide(d['S  4 10.51m'], d['NE 2 12.81m']))



Dasyra2011_Data=np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/dasyra2011/dasyra2011_Type1.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Dasyra2011_2_Data = np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/dasyra2011/dasyra2011_Type2.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Weaver2010_Data = np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/weaver2010/weaver2010.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)

fig = plt.figure()
#ax1 = plt.subplot(221)
ax2 = plt.subplot(121)
ax3 = plt.subplot(122)
#ax4 = plt.subplot(224)

baseO4Ne2 = (d['O IV / Ne II'].get_value(0),d['O IV / Ne II'].get_value(3),d['O IV / Ne II'].get_value(6),d['O IV / Ne II'].get_value(9))
linO4Ne2 = (d['O IV / Ne II'].get_value(1),d['O IV / Ne II'].get_value(4),d['O IV / Ne II'].get_value(7),d['O IV / Ne II'].get_value(10))
lin21O4Ne2 = (d['O IV / Ne II'].get_value(2),d['O IV / Ne II'].get_value(5),d['O IV / Ne II'].get_value(8),d['O IV / Ne II'].get_value(11))
baseNe5Ne2 = (d['Ne V / Ne II'].get_value(0),d['Ne V / Ne II'].get_value(3),d['Ne V / Ne II'].get_value(6),d['Ne V / Ne II'].get_value(9))
linNe5Ne2 = (d['Ne V / Ne II'].get_value(1),d['Ne V / Ne II'].get_value(4),d['Ne V / Ne II'].get_value(7),d['Ne V / Ne II'].get_value(10))
lin21Ne5Ne2 = (d['Ne V / Ne II'].get_value(2),d['Ne V / Ne II'].get_value(5),d['Ne V / Ne II'].get_value(8),d['Ne V / Ne II'].get_value(11))
#ax1.scatter(np.log10(np.divide(Weaver2010_Data[14],Weaver2010_Data[5])),np.log10(np.divide(Weaver2010_Data[7],Weaver2010_Data[5])), edgecolor = '', marker ='^' )
#ax1.scatter(np.log10(np.divide(Dasyra2011_Data[8], Dasyra2011_Data[4])), np.log10(np.divide(Dasyra2011_Data[10], Dasyra2011_Data[4])), edgecolor = '', marker = 'x')
#ax1.scatter(np.log10(np.divide(Dasyra2011_2_Data[7], Dasyra2011_2_Data[2])), np.log10(np.divide(Dasyra2011_2_Data[9], Dasyra2011_2_Data[4])), edgecolor = '', marker = '*')
#ax1.scatter(d['O IV / Ne II'].get_value(0),d['Ne V / Ne II'].get_value(0) , marker = "s",c='#FF5D5D', s = 30, label = "10^4")
#ax1.scatter(d['O IV / Ne II'].get_value(3),d['Ne V / Ne II'].get_value(3) , marker = "s",c='#FF0000', s = 30, label = "10^5")
#ax1.scatter(d['O IV / Ne II'].get_value(6),d['Ne V / Ne II'].get_value(6) , marker = "s",c='#C60000', s = 30, label = "10^6")
#ax1.scatter(d['O IV / Ne II'].get_value(9),d['Ne V / Ne II'].get_value(9) , marker = "s",c='#9B0000', s = 30, label = "10^7")
#ax1.scatter(d['O IV / Ne II'].get_value(1),d['Ne V / Ne II'].get_value(1) , marker = "s",c='#7056C5', s = 30, label = "10^4 Fit")
#ax1.scatter(d['O IV / Ne II'].get_value(4),d['Ne V / Ne II'].get_value(4) , marker = "s",c='#3914AF', s = 30, label = "10^5 Fit")
#ax1.scatter(d['O IV / Ne II'].get_value(7),d['Ne V / Ne II'].get_value(7) , marker = "s",c='#2B0E87', s = 30, label = "10^6 Fit")
#ax1.scatter(d['O IV / Ne II'].get_value(10),d['Ne V / Ne II'].get_value(10) , marker = "s",c='#200969', s = 30, label = "10^7 Fit")
#ax1.scatter(d['O IV / Ne II'].get_value(2),d['Ne V / Ne II'].get_value(2) , marker = "s",c='#50DA50', s = 30, label = "10^4 Fit")
#ax1.scatter(d['O IV / Ne II'].get_value(5),d['Ne V / Ne II'].get_value(5) , marker = "s",c='#00CC00', s = 30, label = "10^5 Fit")
#ax1.scatter(d['O IV / Ne II'].get_value(8),d['Ne V / Ne II'].get_value(8) , marker = "s",c='#009D00', s = 30, label = "10^6 Fit")
#ax1.scatter(d['O IV / Ne II'].get_value(11),d['Ne V / Ne II'].get_value(11) , marker = "s",c='#007A00', s = 30, label = "10^7 Fit")
#ax1.plot(baseO4Ne2,baseNe5Ne2, c = '0')
#ax1.plot(linO4Ne2, linNe5Ne2, c = '0')
#ax1.plot(lin21O4Ne2, lin21Ne5Ne2, c = '0')
#ax1.set_xlabel(r'Log$_{10}$([O IV] $\lambda$ 25.88 $\mu$m / [Ne II] $\lambda$ 12.81 $\mu$m)', fontsize = 20)
#ax1.set_ylabel(r'Log$_{10}$([Ne V] $\lambda$ 14.32 $\mu$m / [Ne II] $\lambda$ 12.81 $\mu$m)', fontsize = 20)


baseO4S4 = (d['O IV / S IV'].get_value(0),d['O IV / S IV'].get_value(3),d['O IV / S IV'].get_value(6),d['O IV / S IV'].get_value(9))
linO4S4 = (d['O IV / S IV'].get_value(1),d['O IV / S IV'].get_value(4),d['O IV / S IV'].get_value(7),d['O IV / S IV'].get_value(10))
lin21O4S4 = (d['O IV / S IV'].get_value(2),d['O IV / S IV'].get_value(5),d['O IV / S IV'].get_value(8),d['O IV / S IV'].get_value(11))
baseNe5S4 = (d['Ne V / S IV'].get_value(0),d['Ne V / S IV'].get_value(3),d['Ne V / S IV'].get_value(6),d['Ne V / S IV'].get_value(9))
linNe5S4 = (d['Ne V / S IV'].get_value(1),d['Ne V / S IV'].get_value(4),d['Ne V / S IV'].get_value(7),d['Ne V / S IV'].get_value(10))
lin21Ne5S4 = (d['Ne V / S IV'].get_value(2),d['Ne V / S IV'].get_value(5),d['Ne V / S IV'].get_value(8),d['Ne V / S IV'].get_value(11))
ax2.scatter(np.log10(np.divide(Dasyra2011_Data[8], Dasyra2011_Data[2])), np.log10(np.divide(Dasyra2011_Data[10], Dasyra2011_Data[2])), edgecolor = '', marker = 'x')
ax2.scatter(np.log10(np.divide(Dasyra2011_2_Data[7], Dasyra2011_2_Data[2])), np.log10(np.divide(Dasyra2011_2_Data[9], Dasyra2011_2_Data[2])), edgecolor = '', marker = '*')
ax2.scatter(d['O IV / S IV'].get_value(0),d['Ne V / S IV'].get_value(0) , marker = "s",c='#FF5D5D', s = 50, label = "10^4")
ax2.scatter(d['O IV / S IV'].get_value(3),d['Ne V / S IV'].get_value(3) , marker = "s",c='#FF0000', s = 50, label = "10^5")
ax2.scatter(d['O IV / S IV'].get_value(6),d['Ne V / S IV'].get_value(6) , marker = "s",c='#C60000', s = 50, label = "10^6")
ax2.scatter(d['O IV / S IV'].get_value(9),d['Ne V / S IV'].get_value(9) , marker = "s",c='#9B0000', s = 50, label = "10^7")
ax2.scatter(d['O IV / S IV'].get_value(1),d['Ne V / S IV'].get_value(1) , marker = "s",c='#7056C5', s = 50, label = "10^4 ax = 1.17")
ax2.scatter(d['O IV / S IV'].get_value(4),d['Ne V / S IV'].get_value(4) , marker = "s",c='#3914AF', s = 50, label = "10^5 ax = 1.17")
ax2.scatter(d['O IV / S IV'].get_value(7),d['Ne V / S IV'].get_value(7) , marker = "s",c='#2B0E87', s = 50, label = "10^6 ax = 1.17")
ax2.scatter(d['O IV / S IV'].get_value(10),d['Ne V / S IV'].get_value(10) , marker = "s",c='#200969', s = 50, label = "10^7 ax = 1.17")
ax2.scatter(d['O IV / S IV'].get_value(2),d['Ne V / S IV'].get_value(2) , marker = "s",c='#50DA50', s = 50, label = "10^4 ax = 2.19")
ax2.scatter(d['O IV / S IV'].get_value(5),d['Ne V / S IV'].get_value(5) , marker = "s",c='#00CC00', s = 50, label = "10^5 ax = 2.19")
ax2.scatter(d['O IV / S IV'].get_value(8),d['Ne V / S IV'].get_value(8) , marker = "s",c='#009D00', s = 50, label = "10^6 ax = 2.19")
ax2.scatter(d['O IV / S IV'].get_value(11),d['Ne V / S IV'].get_value(11) , marker = "s",c='#007A00', s = 50, label = "10^7 ax = 2.19")
ax2.plot(baseO4S4,baseNe5S4, c= '0')
ax2.plot(linO4S4,linNe5S4, ls = '--', c = '0')
ax2.plot(lin21O4S4,lin21Ne5S4, ls = ':', lw = 3, c = '0')
ax2.set_xlabel(r'Log$_{10}$([O IV] $\lambda$ 25.88 $\mu$m / [S IV] $\lambda$ 10.51 $\mu$m)', fontsize = 20)
ax2.set_ylabel(r'Log$_{10}$([Ne V] $\lambda$ 14.32 $\mu$m / [S IV] $\lambda$ 10.51 $\mu$m)', fontsize = 20)

baseS4Ne2 = (d['S IV / Ne II'].get_value(0),d['S IV / Ne II'].get_value(3),d['S IV / Ne II'].get_value(6),d['S IV / Ne II'].get_value(9))
linS4Ne2 = (d['S IV / Ne II'].get_value(1),d['S IV / Ne II'].get_value(4),d['S IV / Ne II'].get_value(7),d['S IV / Ne II'].get_value(10))
lin21S4Ne2 = (d['S IV / Ne II'].get_value(2),d['S IV / Ne II'].get_value(5),d['S IV / Ne II'].get_value(8),d['S IV / Ne II'].get_value(11))
ax3.scatter(np.log10(np.divide(Dasyra2011_Data[4], Dasyra2011_Data[2])), np.log10(np.divide(Dasyra2011_Data[8], Dasyra2011_Data[2])), edgecolor = '', marker = 'x')
ax3.scatter(np.log10(np.divide(Dasyra2011_2_Data[4], Dasyra2011_2_Data[2])), np.log10(np.divide(Dasyra2011_2_Data[7], Dasyra2011_2_Data[2])), edgecolor = '', marker = '*')
ax3.scatter(d['S IV / Ne II'].get_value(0),d['O IV / Ne II'].get_value(0) , marker = "s",c='#FF5D5D', s = 50, label = "10^4")
ax3.scatter(d['S IV / Ne II'].get_value(3),d['O IV / Ne II'].get_value(3) , marker = "s",c='#FF0000', s = 50, label = "10^5")
ax3.scatter(d['S IV / Ne II'].get_value(6),d['O IV / Ne II'].get_value(6) , marker = "s",c='#C60000', s = 50, label = "10^6")
ax3.scatter(d['S IV / Ne II'].get_value(9),d['O IV / Ne II'].get_value(9) , marker = "s",c='#9B0000', s = 50, label = "10^7")
ax3.scatter(d['S IV / Ne II'].get_value(1),d['O IV / Ne II'].get_value(1) , marker = "s",c='#7056C5', s = 50, label = "10^4 Fit")
ax3.scatter(d['S IV / Ne II'].get_value(4),d['O IV / Ne II'].get_value(4) , marker = "s",c='#3914AF', s = 50, label = "10^5 Fit")
ax3.scatter(d['S IV / Ne II'].get_value(7),d['O IV / Ne II'].get_value(7) , marker = "s",c='#2B0E87', s = 50, label = "10^6 Fit")
ax3.scatter(d['S IV / Ne II'].get_value(10),d['O IV / Ne II'].get_value(10) , marker = "s",c='#200969', s = 50, label = "10^7 Fit")
ax3.scatter(d['S IV / Ne II'].get_value(2),d['O IV / Ne II'].get_value(2) , marker = "s",c='#50DA50', s = 50, label = "10^4 Fit")
ax3.scatter(d['S IV / Ne II'].get_value(5),d['O IV / Ne II'].get_value(5) , marker = "s",c='#00CC00', s = 50, label = "10^5 Fit")
ax3.scatter(d['S IV / Ne II'].get_value(8),d['O IV / Ne II'].get_value(8) , marker = "s",c='#009D00', s = 50, label = "10^6 Fit")
ax3.scatter(d['S IV / Ne II'].get_value(11),d['O IV / Ne II'].get_value(11) , marker = "s",c='#007A00', s = 50, label = "10^7 Fit")
ax3.plot(baseS4Ne2, baseO4Ne2, c= '0')
ax3.plot(linS4Ne2, linO4Ne2, ls = '--', c= '0')
ax3.plot(lin21S4Ne2, lin21O4Ne2, ls = ':', lw = 3, c= '0')

ax3.set_xlabel(r'Log$_{10}$([S IV] $\lambda$ 10.51 $\mu$m / [Ne II] $\lambda$ 12.81 $\mu$m)', fontsize = 20)
ax3.set_ylabel(r'Log$_{10}$([O IV] $\lambda$ 25.88 $\mu$m / [Ne II] $\lambda$ 12.81 $\mu$m)', fontsize = 20)


#ax4.scatter(np.log10(np.divide(Dasyra2011_Data[4], Dasyra2011_Data[2])), np.log10(np.divide(Dasyra2011_Data[10], Dasyra2011_Data[2])), edgecolor = '', marker = 'x')
#ax4.scatter(np.log10(np.divide(Dasyra2011_2_Data[4], Dasyra2011_2_Data[2])), np.log10(np.divide(Dasyra2011_2_Data[9], Dasyra2011_2_Data[2])), edgecolor = '', marker = '*')
#ax4.scatter(d['S IV / Ne II'].get_value(0),d['Ne V / Ne II'].get_value(0) , marker = "s",c='#FF5D5D', s = 30, label = "10^4")
#ax4.scatter(d['S IV / Ne II'].get_value(3),d['Ne V / Ne II'].get_value(3) , marker = "s",c='#FF0000', s = 30, label = "10^5")
#ax4.scatter(d['S IV / Ne II'].get_value(6),d['Ne V / Ne II'].get_value(6) , marker = "s",c='#C60000', s = 30, label = "10^6")
#ax4.scatter(d['S IV / Ne II'].get_value(9),d['Ne V / Ne II'].get_value(9) , marker = "s",c='#9B0000', s = 30, label = "10^7")
#ax4.scatter(d['S IV / Ne II'].get_value(1),d['Ne V / Ne II'].get_value(1) , marker = "s",c='#7056C5', s = 30, label = "10^4 Fit")
#ax4.scatter(d['S IV / Ne II'].get_value(4),d['Ne V / Ne II'].get_value(4) , marker = "s",c='#3914AF', s = 30, label = "10^5 Fit")
#ax4.scatter(d['S IV / Ne II'].get_value(7),d['Ne V / Ne II'].get_value(7) , marker = "s",c='#2B0E87', s = 30, label = "10^6 Fit")
#ax4.scatter(d['S IV / Ne II'].get_value(10),d['Ne V / Ne II'].get_value(10) , marker = "s",c='#200969', s = 30, label = "10^7 Fit")
#ax4.scatter(d['S IV / Ne II'].get_value(2),d['Ne V / Ne II'].get_value(2) , marker = "s",c='#50DA50', s = 30, label = "10^4 Fit")
#ax4.scatter(d['S IV / Ne II'].get_value(5),d['Ne V / Ne II'].get_value(5) , marker = "s",c='#00CC00', s = 30, label = "10^5 Fit")
#ax4.scatter(d['S IV / Ne II'].get_value(8),d['Ne V / Ne II'].get_value(8) , marker = "s",c='#009D00', s = 30, label = "10^6 Fit")
#ax4.scatter(d['S IV / Ne II'].get_value(11),d['Ne V / Ne II'].get_value(11) , marker = "s",c='#007A00', s = 30, label = "10^7 Fit")
#ax4.plot(baseS4Ne2, baseNe5Ne2, c= '0')
#ax4.plot(linS4Ne2, linNe5Ne2, c= '0')
#ax4.plot(lin21S4Ne2, lin21Ne5Ne2, c= '0')
#ax4.set_xlabel(r'Log$_{10}$([S IV] $\lambda$ 10.51 $\mu$m / [Ne II] $\lambda$ 12.81 $\mu$m)', fontsize = 20)
#ax4.set_ylabel(r'Log$_{10}$([Ne V] $\lambda$ 25.88 $\mu$m / [Ne II] $\lambda$ 12.81 $\mu$m)', fontsize = 20)

ax2.legend(loc = 'upper left', prop = {'size': 12})

#plt.suptitle('AGN Infrared Abundance Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
plt.show()
