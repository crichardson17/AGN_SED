import matplotlib
from scipy.optimize import curve_fit
import numpy as np
"Define a function to call our data"
def data(filename, column):
    results=np.genfromtxt("asu3.csv", delimiter=',',skip_header=1)
    return [result[column] for result in results]
"our observed alpha x"
observedax=data("asu3.csv",2)

#our actual auv 
observedauv=data("asu3.csv",4)

#our expected aox
obsaox=data("asu3.csv",6)

#Our uncertainties
axerr=data("asu3.csv",3)
#auverr=data("asu3.csv",5)

"define a function to create a constant line"
def constfit(x,a):
    return a
constparams=curve_fit(constfit,observedax,obsaox)
[a]=constparams[0]
print(a)

"define a function to create a linear regression"
def linfit(x,m,b):
    return m*x+b
"define our parameters" 
linparams = curve_fit(linfit,observedax,obsaox)
[a,b] = linparams[0]
print(a,b)

"Define a function to create a quadratic regression"
def quadfit(x,c,d,e):
    return (c*x**2)+d*x+e
quadparams = curve_fit(quadfit,observedax,obsaox)
[c,d,e]=quadparams[0]
print(c,d,e)
#now we take the difference of the observed and expected values for each and square them

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

