import matplotlib
import scipy as sp
import numpy as np
def data(filename, column):
    results=np.genfromtxt("asu.csv", delimiter=',',skip_header=1)
    return [result[column] for result in results]
#our observed alphax
observedax=data("asu.csv",0)

#our expected alphax based on the trendline (solved the function for actual alphaox values of Y)

expectedax=data("asu.csv",2)
#expectedax2=data("asu.csv",3)

#our actual auv 
observedauv=data("asu.csv",6)

#our expected auv
expectedauv=data("asu.csv",8)

#our expected aox
expaox=data("asu.csv",5)
obsaox=data("asu.csv",4)

#Our uncertainties
axerr=data("asu.csv",1)
#auverr=data("asu.csv",7)

#now we take the difference of the observed and expected values for each and square them

diffax=(np.subtract(observedax,expectedax))/axerr
diffauv=np.subtract(obsaox, expaox)

#square the differences
diffaxsq=np.power(diffax,4)
diffauvsq=np.power(diffauv,4)

#square the uncertainties
#auverrsq=np.power(auverr,2)

#add the errors and the differences
#sumerror=np.add(axerrsq,auverrsq)
sumdiff=np.add(diffaxsq,diffauvsq)

#divide the two and sum up all the values in the array
chisquare=sumdiff
print(sum(np.sqrt(chisquare)))

