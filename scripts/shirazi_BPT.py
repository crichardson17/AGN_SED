import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dfs=[] #Create an empty array for our Data

d=pd.DataFrame() 
d=d.reset_index()
d2=pd.DataFrame({'Temperature': ['10^4','10^5', '10^6', '10^7']},dtype=object) #Create a Dataframe of labels for each file used

rootdirectory='C:/Users/chris_000/Documents/GitHub/AGN_SED/Cloudy_Data' 

for root, dirs, files in os.walk(rootdirectory, topdown=False):
    for name in files:
        if name.startswith('Pressure') and name.endswith('.lin'):
            print name
            #only read columns from list cols
            dfs.append(pd.read_csv(os.path.join(root, name), delimiter="\t", usecols=['TOTL  4861A','H  1  6563A', 'HE 2  4686A' ,'N  2  6584A']))
            d = pd.concat(dfs, ignore_index=True)
            
d['Temperature']=d2
            
d['N II / H-Alpha']=np.log10(d['N  2  6584A']/d['TOTL  4861A'])
d['He II / H-Beta']= np.log10(d['HE 2  4686A']/d['H  1  6563A'])
Shirazi_Data=np.genfromtxt('C:/Users/chris_000/Documents/GitHub/AGN_SED/sdss_data/shirazi12.csv', skip_header=3, delimiter = ',',unpack=True)


x = np.arange(-3,-0.2,0.01)
y = -1.22 + np.divide(1,8.92*x+1.32)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(Shirazi_Data[7],Shirazi_Data[6], s = 2)
ax.scatter(d['N II / H-Alpha'],d['He II / H-Beta'], c= 'r')
ax.plot(x,y)
xlimit = ax.set_xlim(-3,1)
ax.set_ylim(xlimit)
ax.set_title(r'Log$_{10}$([N II] $\lambda 6583$ / H$\alpha$) vs Log$_{10}$(He II] $\lambda 4686$ / H$\beta$)')
ax.set_xlabel(r'Log$_{10}$([N II] $\lambda 6583$ / H$\alpha$)')
ax.set_ylabel(r'Log$_{10}$([He II] $\lambda 4686$ / H$\beta$)')
plt.show()