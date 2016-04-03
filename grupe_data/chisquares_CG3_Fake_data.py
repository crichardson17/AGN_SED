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

# Define constants

data_file = "Fake_Data.csv"

fv = 1

#Define a function to call our data

def data(filename, column):
    results=np.genfromtxt(filename, delimiter=',',skip_header=1)
    return [result[column] for result in results]
    
#Define a function to call the fake data that is produced

# Our observed ax, auv, aox
observedax=data(data_file,0)
observedauv=data(data_file,1)



# Our uncertainties

axerr=data(data_file,2)
auverr=data(data_file,3)

# Define a function to create a constant line
def constfit(x,a):
    return a
constparams=curve_fit(constfit,observedax,observedauv)
[a]=constparams[0]
print(a)

#Define a function to create a linear regression

def linfit(x,m,b):
    return m*x+b
"define our parameters" 
linparams = curve_fit(linfit,observedax,observedauv)
[m,b] = linparams[0]
print(m,b)

#Define a function to create a quadratic regression

def quadfit(x,c,d,e):
    return (c*x**2)+d*x+e
quadparams = curve_fit(quadfit,observedax,observedauv)
[c,d,e]=quadparams[0]
print(c,d,e)

def quadfit2(x,f,g,h):
    return ((c*x**2)+d*x+e)
quadparams2 = curve_fit(quadfit2,observedauv,observedax)
[f,g,h]=quadparams2[0]
#use the functions to create data points

#The expected ax values
row_expax=[]
for item in observedauv:
    expected_ax=((item-b)/m)
    row_expax.append(expected_ax)
    
    
row_expax2=[]
for item in observedauv:
    expected_ax_quad=(f*item**2+g*item+h)
    row_expax2.append(expected_ax_quad)
    
row_expax3=[]
for item in observedauv:
    expected_ax_const=(a)
    row_expax3.append(expected_ax_const)
    
#the expected auv values
row_expauv=[]
row_expauv2=[]
row_expauv3=[]
for item in observedax:
    expected_auv=(m*item+b)
    row_expauv.append(expected_auv)
    
for item in observedax:
    expected_auv_quad=(c*item**2+d*item+e)
    row_expauv2.append(expected_auv_quad)
    
for item in observedax:
    expected_auv_const=(a)
    row_expauv3.append(expected_auv_const)
    

data_pts = len(observedax)

print(row_expax,row_expauv)
# Now we take the difference of the observed and expected values for each spectral index and divide them by the uncertainty
diffax=np.subtract(observedax,row_expax)/axerr
diffauv=(np.subtract(observedauv, row_expauv))/auverr


#Raise the differences to the fourth power
diffaxquad=np.power(diffax,4)
diffauvquad=np.power(diffauv,4)


#add these two 
sumdifferences=np.add(diffaxquad,diffauvquad)
print(sumdifferences)

sumdiffroot=np.sqrt(sumdifferences)
print(sumdiffroot)

#sum this over all our data points
chisquare=sum(float(i) for i in sumdiffroot)


print chisquare/data_pts

