############################################################################
#
# Chris Richardson & Helen Meskhidze
# Elon University
#
# Given a metals scale factor (ki), which is supplied directly to Cloudy,
# calculate the helium scale factor for Cloudy (alpha) in order to conserve
# mass. Output the actual metallicity mass fractions, before and after.
#
# 1. Use the ki value on both the metals and nitrogen line in Cloudy
# 2. Use the He scale factor output to terminal in Cloudy
#
#############################################################################

from numpy import *

# Enter the metals scale factor

ki = 3.4
#ki = raw_input("Enter the metals scale factor: ")



# Calculate for the solar abundaces from GASS10
# with depletion factors given in Cloudy c13.03


#abundances by number
abundHe =	8.51e-2 # * 		
abundLi = 	1.12e-11 *		0.16 
abundBe = 	2.40e-11 * 		0.6
abundB = 	5.01e-10 * 		0.13
abundC = 	2.69e-04 * 		0.4	
abundN = 	6.76e-05# * 		
abundO = 	4.90e-04 *		0.6
abundF = 	3.63e-08 * 		0.3	
abundNe = 	8.51e-05# * 		
abundNa = 	1.74e-06 * 		0.2
abundMg = 	3.98e-05 * 	 	0.2
abundAl = 	2.82e-06 * 		0.01
abundSi = 	3.24e-05 *	 	0.03
abundP = 	2.57e-07 * 		0.25
abundS = 	1.32e-05# * 	 	
abundCl = 	3.16e-07 * 		0.4
abundAr = 	2.51e-06# * 	 	
abundK = 	1.07e-07 * 		0.3
abundCa = 	2.19e-06 * 	 	0.0001
abundSc = 	1.41e-09 * 		0.005
abundTi = 	8.91e-08 * 	 	0.008
abundV = 	8.51e-09 * 		0.006
abundCr = 	4.37e-07 * 		0.006
abundMn = 	2.69e-07 * 	 	0.005
abundFe = 	3.16e-05 * 		0.01
abundCo = 	9.77e-08 * 		0.01
abundNi = 	1.66e-06 * 		0.01
abundCu = 	1.55e-08 * 		0.1	
abundZi = 	3.63e-08 * 		0.25
#-------------------------------------
#mass abundances
mabundHe =	abundHe  * 		4.0026
mabundLi = 	abundLi *		6.941 
mabundBe = 	abundBe * 		9.0122
mabundB = 	abundB * 		10.811
mabundC = 	abundC * 		12.0107	
mabundN = 	abundN * 		14.0067
mabundO = 	abundO *		15.9994
mabundF = 	abundF * 		18.9984	
mabundNe = 	abundNe * 		20.1797
mabundNa = 	abundNa * 		22.9897
mabundMg = 	abundMg * 	 	24.305
mabundAl = 	abundAl * 		26.9815
mabundSi = 	abundSi *	 	28.0855
mabundP = 	abundP * 		30.9738
mabundS = 	abundS * 	 	32.065
mabundCl =  abundCl * 		35.453
mabundAr = 	abundAr * 	 	39.948
mabundK = 	abundK * 		39.0983
mabundCa = 	abundCa * 	 	40.078
mabundSc = 	abundSc * 		44.9559
mabundTi = 	abundTi * 	 	47.867
mabundV = 	abundV * 		50.9415
mabundCr = 	abundCr * 		51.9961
mabundMn = 	abundMn * 	 	54.938
mabundFe = 	abundFe * 		55.845
mabundCo = 	abundCo * 		58.9332
mabundNi = 	abundNi * 		58.6934
mabundCu = 	abundCu * 		63.546	
mabundZi = 	abundZi * 		65.39

#-------------------------------------
# Computing the total metals abundance by mass and by number 

totalz =  abundLi + abundBe + abundB + abundC + abundN + abundO + abundF + abundNe + abundNa + abundMg + abundAl+ abundSi + abundP + abundS + abundCl + abundAr + abundK + abundCa+ abundSc + abundTi + abundV + abundCr + abundMn + abundFe + abundCo + abundNi + abundCu + abundZi
mtotalz =  mabundLi + mabundBe + mabundB + mabundC + mabundN + mabundO + mabundF + mabundNe + mabundNa + mabundMg + mabundAl+ mabundSi + mabundP + mabundS + mabundCl + mabundAr + mabundK + mabundCa+ mabundSc + mabundTi + mabundV + mabundCr + mabundMn + mabundFe + mabundCo + mabundNi + mabundCu + mabundZi
new_mtotalz = (mabundLi + mabundBe + mabundB + mabundC + mabundO + mabundF + mabundNe + mabundNa + mabundMg + mabundAl+ mabundSi + mabundP + mabundS + mabundCl + mabundAr + mabundK + mabundCa+ mabundSc + mabundTi + mabundV + mabundCr + mabundMn + mabundFe + mabundCo + mabundNi + mabundCu + mabundZi)*ki + mabundN*ki**2

#print abundC

#-------------------------------------

# For new solar abundances
x_ini = 1.0 / (1.0 +  mabundHe + mtotalz) #X_solar
y_ini = 1.0 - (x_ini) - (mtotalz)*(x_ini) #Y_solar
z_ini = 1.0 - (x_ini) - (mabundHe)*(x_ini) #Z_solar


new_z_f = (z_ini * ki)/(x_ini + y_ini + ((2.0*ki)-1.0)*z_ini)
new_y_f = ((z_ini * ki)/(x_ini + y_ini + ((2.0*ki)-1.0)*z_ini))-z_ini+y_ini
x_new = 1.0 - new_y_f - new_z_f

newalpha = new_y_f * (1/4.0/x_new) * (1.0/abundHe) #new scale factor

print "The He scale factor for ki", ki, "is", newalpha
print "The previous Z (mass fraction) was", mtotalz, "and the new Z (mass fraction) is", new_mtotalz

