
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
        if name.startswith('Linear_Fit') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['NE 5 24.31m','NE 3 15.55m','TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A', 'O  4 25.88m','NE 2 12.81m','NE 5 14.32m']))
            d = pd.concat(dfs, ignore_index=True)
        if name.startswith('Hden25') and name.endswith('.lin'):
             print name
            #only read columns from list cols
             dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['NE 5 24.31m','NE 3 15.55m','TOTL  4861A','O  3  5007A', 'NE 5  3426A', 'NE 3  3869A',
            'TOTL  4363A', 'O  1  6300A', 'H  1  6563A','N  2  6584A','S  2  6720A' , 'HE 2  4686A','TOTL  3727A', 'S II  6716A', 'S II  6731A',
            'NE 3  3869A','AR 3  7135A','HE 1  5876A','TOTL  4363A','O  3  4959A','O II  3726A', 'O II  3729A','NE 2 12.81m','O  4 25.88m','NE 5 14.32m']))
             d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2

d['O IV / Ne II'] = np.log10(np.divide(d['O  4 25.88m'], d['NE 2 12.81m']))
d['Ne V / Ne II'] = np.log10(np.divide(d['NE 5 14.32m'], d['NE 2 12.81m']))
d['Ne V / Ne III'] = np.log10(np.divide(d['NE 5 14.32m'], d['NE 3 15.55m']))





Dasyra2011_Data=np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/dasyra2011/dasyra2011_Type1.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Dasyra2011_2_Data = np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/dasyra2011/dasyra2011_Type2.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)
Weaver2010_Data = np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/ir_data/weaver2010/weaver2010.csv', skip_header=1, delimiter = ',',dtype=float,unpack=True)

fig = plt.figure()

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)
ax1.scatter(np.log10(np.divide(Weaver2010_Data[7],Weaver2010_Data[9])), np.log10(np.divide(Weaver2010_Data[7], Weaver2010_Data[5])), marker = '^',label = 'Weaver 2010', edgecolor = '')
ax1.scatter(np.log10(np.divide(Dasyra2011_Data[10],Dasyra2011_Data[6])), np.log10 (np.divide(Dasyra2011_Data[10],Dasyra2011_Data[2])), marker = 'x', c = 'r', label = 'Dasyra 2011 Type 1')
ax1.scatter(np.log10(np.divide(Dasyra2011_2_Data[9],Dasyra2011_2_Data[5])), np.log10 (np.divide(Dasyra2011_2_Data[9], Dasyra2011_2_Data[2])), marker = '*', c = 'r', label = 'Dasyra 2011 Type 2', edgecolor = '')
ax1.scatter(d['Ne V / Ne III'].get_value(0),d['Ne V / Ne II'].get_value(0), marker = "s",c='c', s = 30, label = "10^4")
ax1.scatter(d['Ne V / Ne III'].get_value(2),d['Ne V / Ne II'].get_value(2), marker = "s",c='g', s = 30, label = "10^5")
ax1.scatter(d['Ne V / Ne III'].get_value(4),d['Ne V / Ne II'].get_value(4), marker = "s",c='yellow', s = 30, label = "10^6")
ax1.scatter(d['Ne V / Ne III'].get_value(6),d['Ne V / Ne II'].get_value(6), marker = "s",c='magenta', s = 30, label = "10^7")
ax1.scatter(d['Ne V / Ne III'].get_value(1),d['Ne V / Ne II'].get_value(1), marker = "s",c='#F06E07', s = 30, label = "10^4 Fit")
ax1.scatter(d['Ne V / Ne III'].get_value(3),d['Ne V / Ne II'].get_value(3), marker = "s",c='#111DD9', s = 30, label = "10^5 Fit")
ax1.scatter(d['Ne V / Ne III'].get_value(5),d['Ne V / Ne II'].get_value(5), marker = "s",c='#ABF036', s = 30, label = "10^6 Fit")
ax1.scatter(d['Ne V / Ne III'].get_value(7),d['Ne V / Ne II'].get_value(7), marker = "s",c='#D91C82', s = 30, label = "10^7 Fit")
ax1.plot((d['Ne V / Ne III'].get_value(0),d['Ne V / Ne III'].get_value(2),d['Ne V / Ne III'].get_value(4),d['Ne V / Ne III'].get_value(6)),(d['Ne V / Ne II'].get_value(0),d['Ne V / Ne II'].get_value(2),
d['Ne V / Ne II'].get_value(4),d['Ne V / Ne II'].get_value(6)), c = '0')
ax1.plot((d['Ne V / Ne III'].get_value(1),d['Ne V / Ne III'].get_value(3),d['Ne V / Ne III'].get_value(5),d['Ne V / Ne III'].get_value(7)),(d['Ne V / Ne II'].get_value(1),d['Ne V / Ne II'].get_value(3), d['Ne V / Ne II'].get_value(5),d['Ne V / Ne II'].get_value(7)), c = '0')
ax1.set_xlabel(r'Log$_{10}$([Ne V] / [Ne III]')
ax1.set_ylabel(r'Log$_{10}$([Ne V] / [Ne II]')



baseNe5Ne3 = (d['Ne V / Ne III'].get_value(0),d['Ne V / Ne III'].get_value(2),d['Ne V / Ne III'].get_value(4),d['Ne V / Ne III'].get_value(6))
linNe5Ne3 = (d['Ne V / Ne III'].get_value(1),d['Ne V / Ne III'].get_value(3),d['Ne V / Ne III'].get_value(5),d['Ne V / Ne III'].get_value(7))
baseNe52431 = np.log10((d['NE 5 24.31m'].get_value(0),d['NE 5 24.31m'].get_value(2),d['NE 5 24.31m'].get_value(4),d['NE 5 24.31m'].get_value(6)))
linNe52431 = np.log10((d['NE 5 24.31m'].get_value(1),d['NE 5 24.31m'].get_value(3),d['NE 5 24.31m'].get_value(5),d['NE 5 24.31m'].get_value(7)))
ax2.scatter(np.log10(np.divide(Weaver2010_Data[7],Weaver2010_Data[9])),np.log10(Weaver2010_Data[11]),edgecolor = '', marker =  '^')
ax2.scatter(d['Ne V / Ne III'].get_value(0),np.log10(d['NE 5 24.31m'].get_value(0)), marker = "s",c='green', s = 30, label = "10^4")
ax2.scatter(d['Ne V / Ne III'].get_value(2),np.log10(d['NE 5 24.31m'].get_value(2)), marker = "s",c='cyan', s = 30, label = "10^5")
ax2.scatter(d['Ne V / Ne III'].get_value(4),np.log10(d['NE 5 24.31m'].get_value(4)), marker = "s",c='r', s = 30, label = "10^6")
ax2.scatter(d['Ne V / Ne III'].get_value(6),np.log10(d['NE 5 24.31m'].get_value(6)), marker = "s",c='magenta', s = 30, label = "10^7")
ax2.scatter(d['Ne V / Ne III'].get_value(1),np.log10(d['NE 5 24.31m'].get_value(1)), marker = "s",c='#F06E07', s = 30, label = "10^4 Fit")
ax2.scatter(d['Ne V / Ne III'].get_value(3),np.log10(d['NE 5 24.31m'].get_value(3)), marker = "s",c='#111DD9', s = 30, label = "10^5 Fit")
ax2.scatter(d['Ne V / Ne III'].get_value(5),np.log10(d['NE 5 24.31m'].get_value(5)), marker = "s",c='#ABF036', s = 30, label = "10^6 Fit")
ax2.scatter(d['Ne V / Ne III'].get_value(7),np.log10(d['NE 5 24.31m'].get_value(7)), marker = "s",c='#D91C82', s = 30, label = "10^7 Fit")
ax2.plot(baseNe5Ne3,baseNe52431, c= '0')
ax2.plot(linNe5Ne3,linNe52431, c = '0')
ax2.set_xlabel(r'Log$_{10}$([Ne V] / [Ne III]')
ax2.set_ylabel(r'Log$_{10}$([Ne V] $\lambda$ 24.32 $\mu$m')
ax1.legend(loc = 'lower right', prop = {'size': 12})

baseNe5Ne2 = (d['Ne V / Ne II'].get_value(0),d['Ne V / Ne II'].get_value(2),d['Ne V / Ne II'].get_value(4),d['Ne V / Ne II'].get_value(6))
linNe5Ne2 = (d['Ne V / Ne II'].get_value(1),d['Ne V / Ne II'].get_value(3),d['Ne V / Ne II'].get_value(5),d['Ne V / Ne II'].get_value(7))
ax3.scatter(np.log10(np.divide(Weaver2010_Data[7], Weaver2010_Data[5])),np.log10(Weaver2010_Data[7]),edgecolor = '', marker =  '^')
ax3.scatter(d['Ne V / Ne II'].get_value(0),np.log10(d['NE 5 24.31m'].get_value(0)), marker = "s",c='green', s = 30, label = "10^4")
ax3.scatter(d['Ne V / Ne II'].get_value(2),np.log10(d['NE 5 24.31m'].get_value(2)), marker = "s",c='cyan', s = 30, label = "10^5")
ax3.scatter(d['Ne V / Ne II'].get_value(4),np.log10(d['NE 5 24.31m'].get_value(4)), marker = "s",c='r', s = 30, label = "10^6")
ax3.scatter(d['Ne V / Ne II'].get_value(6),np.log10(d['NE 5 24.31m'].get_value(6)), marker = "s",c='magenta', s = 30, label = "10^7")
ax3.scatter(d['Ne V / Ne II'].get_value(1),np.log10(d['NE 5 24.31m'].get_value(1)), marker = "s",c='#F06E07', s = 30, label = "10^4 Fit")
ax3.scatter(d['Ne V / Ne II'].get_value(3),np.log10(d['NE 5 24.31m'].get_value(3)), marker = "s",c='#111DD9', s = 30, label = "10^5 Fit")
ax3.scatter(d['Ne V / Ne II'].get_value(5),np.log10(d['NE 5 24.31m'].get_value(5)), marker = "s",c='#ABF036', s = 30, label = "10^6 Fit")
ax3.scatter(d['Ne V / Ne II'].get_value(7),np.log10(d['NE 5 24.31m'].get_value(7)), marker = "s",c='#D91C82', s = 30, label = "10^7 Fit")
ax3.set_xlabel(r'Log$_{10}$([Ne V] / [Ne II]')
ax3.set_ylabel(r'Log$_{10}$([Ne V] $\lambda$ 24.32 $\mu$m')
ax3.plot(baseNe5Ne2,baseNe52431, c= '0')
ax3.plot(linNe5Ne2,linNe52431, c = '0')
plt.suptitle('AGN Infrared SED Diagnostic Plots: Metallicity = 1.5, Efrac = 0.01, Phi(h) = 10.4771, n(h) = 2.5')
plt.show()


