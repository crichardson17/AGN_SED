"""
Christopher Greene & Chris Richardson
Elon University

Description:A generalized code for generating 3 different best-fit curves to data 
to determine any relationship between the 3 spectral indices used to fit a Spectral
Energy Distribution, these best-fit curves then produce points that act as data so that 
we may perform a Chi-Square Goodness of Fit Test. 
"""

import csv
import matplotlib
from scipy.optimize import curve_fit
import numpy as np

# Define constants

data_file = "asu3.csv"
fv = 1

#Define a function to call our data

def data(filename, column):
    results=np.genfromtxt(filename, delimiter=',',skip_header=1)
    return [result[column] for result in results]

# Our observed ax, auv, aox
observedax=data(data_file,2)
observedauv=data(data_file,4)
obsaox=data(data_file,6)


# Our uncertainties

axerr=data(data_file,3)
auverr=data(data_file,5)

# Define a function to create a constant line
def constfit(x,a):
    return a
constparams=curve_fit(constfit,observedax,obsaox)
[a]=constparams[0]
print(a)

#Define a function to create a linear regression

def linfit(x,m,b):
    return m*x+b
"define our parameters" 
linparams = curve_fit(linfit,observedax,obsaox)
[m,b] = linparams[0]
print(m,b)

#Define a function to create a quadratic regression

def quadfit(x,c,d,e):
    return (c*x**2)+d*x+e
quadparams = curve_fit(quadfit,observedax,obsaox)
[c,d,e]=quadparams[0]
print(c,d,e)

#use the functions to create data points
row_expax=[]
for item in observedax:
    expected_ax=np.array(m*item+b)
    row_expax.append(expected_ax)
    print(expected_ax)
    
row_expax2=[]
for item in observedax:
    expected_ax_quad=np.array(c*item**2+d*item+e)
    row_expax2.append(expected_ax_quad)
#write these data points to csv file
with open('expected_ax.csv', 'wb') as myfile:
    wr=csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(row_expax)

"""
1. Check other fits with excel
2. Alter chisq code below
3. Create fake date file
4. Check code with fake data
"""

#data_pts = len(obsaox)
#print size

# Now we take the difference of the observed and expected values for each and square them

#diffax=(np.subtract(observedax,expectedax))/axerr
#diffauv=np.subtract(obsaox, expaox)

#square the differences
#diffaxsq=np.power(diffax,4)
#diffauvsq=np.power(diffauv,4)

#square the uncertainties
#auverrsq=np.power(auverr,2)

#add the errors and the differences
#sumerror=np.add(axerrsq,auverrsq)
#sumdiff=np.add(diffaxsq,diffauvsq)

#divide the two and sum up all the values in the array
#chisquare=sumdiff
#print(sum(np.sqrt(chisquare)))

