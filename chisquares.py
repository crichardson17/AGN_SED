import matplotlib
import scipy as sp
import numpy as np
def data(filename, column):
    results=np.genfromtxt("asu.csv", delimiter=',',skip_header=1)
    return [result[column] for result in results]
#our observed alphax
observedax=data("asu.csv",0)

#our expected alphax based on the trendline (solved the function for actual alphaox values of Y)

#expectedax=data("asu.csv",7)
expectedax2=data("asu.csv",8)

#our actual auv 
observedauv=data("asu.csv",4)

#our expected auv
expectedauv=data("asu.csv",3)

#our expected aox
expaox=data("asu.csv",1)
obsaox=data("asu.csv",2)

#Our uncertainties
axerr=data("asu.csv",5)
#auverr=data("asu.csv",6)

#now we take the difference of the observed and expected values for each and square them

diffax=np.subtract(observedax,expectedax2)
diffauv=np.subtract(obsaox, expaox)

#square the differences
diffaxsq=np.power(diffax,2)
diffauvsq=np.power(diffauv,2)

#square the uncertainties
axerrsq=np.power(axerr,2)
#auverrsq=np.power(auverr,2)

#add the errors and the differences
#sumerror=np.add(axerrsq,auverrsq)
sumdiff=np.add(diffaxsq,diffauvsq)

#divide the two and sum up all the values in the array
chisquare=sumdiff/axerrsq
print(sum(chisquare)/68)

