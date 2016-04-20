"""
Christopher Greene & Chris Richardson
Elon University

Description:A generalized code for generating 3 different best-fit curves to data 
to determine any relationship between the 3 spectral indices used to fit a Spectral
Energy Distribution, these best-fit curves then produce points that act as data so that 
we may perform a Chi-Square Goodness of Fit Test. 
"""


from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
# Define constants

data_file = "Fake_Data.csv"
data_file2= "Fake_Data_Constant.csv"



#Define a function to call our data

def data(filename, column):
    results=np.genfromtxt(filename, delimiter=',',skip_header=1)
    return [result[column] for result in results]
    
#Define a function to call the fake data that is produced

# Our observed ax, auv, aox
observedax=data(data_file2,0)
observedauv=data(data_file2,1)



# Our uncertainties
axerr=data(data_file2,2)
auverr=data(data_file2,2)

# Define a function to create a constant line
def constfit(x,a):
    return a
"define our parameters"
constparams=curve_fit(constfit,observedax,observedauv)
[a]=constparams[0]
print(a)

#Define a function to create a linear regression
def linfit(x,m,b):
    return m*x+b
"define our parameters" 
linparams = curve_fit(linfit,observedax,observedauv)
[m,b] = linparams[0]
#print(m,b)

def linfit2(x,m1,b1):
    return m1*x+b1
"define our parameters" 
linparams = curve_fit(linfit2,observedauv,observedax)
[m1,b1] = linparams[0]

#Define a function to create a quadratic regression
def quadfit(x,c,d,e):
    return (c*x**2)+d*x+e
quadparams = curve_fit(quadfit,observedax,observedauv)
[c,d,e]=quadparams[0]
#print(c,d,e)

def quadfit2(x,f,g,h):
    return ((c*x**2)+d*x+e)
quadparams2 = curve_fit(quadfit2,observedauv,observedax)
[f,g,h]=quadparams2[0]

#The expected ax values
expax=[]
expax2=[]
expax3=[]

for item in observedauv:
    expected_ax=(m1*item+b1)
    expax.append(expected_ax)
    
    
for item in observedauv:
    expected_ax_quad=(f*item**2+g*item+h)
    expax2.append(expected_ax_quad)
    
for item in observedauv:
    expected_ax_const=(a)
    expax3.append(expected_ax_const)

#The expected auv values
expauv=[]
expauv2=[]
expauv3=[]

for item in observedax:
    expected_auv=(m*item+b)
    expauv.append(expected_auv)
    
for item in observedax:
    expected_auv_quad=(c*item**2+d*item+e)
    expauv2.append(expected_auv_quad)
    
for item in observedax:
    expected_auv_const=(a)
    expauv3.append(expected_auv_const)

data_pts = len(observedax)

#print(expax3,expauv3)

# Now we take the difference of the observed and expected values for each spectral index and divide them by the uncertainty
#diffax=np.subtract(observedax,expax)
diffax=np.subtract(observedax,observedax)
diffauv=np.subtract(observedauv,expauv3)
#print(diffax,diffauv)

#Raise the differences to the fourth power
diffaxquad=np.power(diffax/axerr,4)
diffauvquad=np.power(diffauv/auverr,4)
print(diffaxquad,diffauvquad)

#add these two
sumdifferences=np.add(diffaxquad,diffauvquad)
#print(sumdifferences)

sumdiffquad=np.power(sumdifferences,0.5)

#sum this over all our data points
#chisquare=np.power(sum(float(i) for i in sumdifferences),.5)
chisquare=sum(float(i) for i in sumdiffquad)
print chisquare/data_pts


#Make a plot of the residuals
"""residualplot=plt.figure()
axes=residualplot.add_subplot(111)
axes.set_title('Observed Ax vs. Residuals')
axes.set_xlabel('Observed Ax')
axes.set_ylabel('Residuals')
plt.plot(observedax,diffauv,"o")

plt.show()"""
