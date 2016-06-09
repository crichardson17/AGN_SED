"""
Christopher Greene & Chris Richardson
Elon University

Description:A generalized code for generating 3 different best-fit curves to data 
to determine any relationship between the 3 spectral indices used to fit a Spectral
Energy Distribution, these best-fit curves then produce points that act as data so that 
we may perform a Chi-Square Goodness of Fit Test. 
"""



import numpy as np
import matplotlib.pyplot as plt
import sklearn as skl
from sklearn.linear_model import LinearRegression
# Define constants

data_file = "/users/compastro/greene/AGN_SED/grupe_data/grupe_data.csv"

Grupe_Data = np.genfromtxt(data_file,skip_header = 1,delimiter = ',', usecols = [0,2,3,4,5,6], unpack = True)


ax_data = Grupe_Data[1,:]
ax_error = Grupe_Data[2]
auv_data = Grupe_Data[3,:]
auv_error = Grupe_Data[4]
aox_data = Grupe_Data[5]

ax_data = ax_data.reshape(36,1)
auv_data = auv_data.reshape(36,1)
print auv_data.shape

poly = skl.preprocessing.PolynomialFeatures(degree = 2)
ax_data= poly.fit_transform(ax_data)
linmodel = LinearRegression(fit_intercept = True, normalize = True)

axauv_model = linmodel.fit(ax_data,auv_data)
axauv_model.
print axauv_model.coef_, axauv_model.intercept_ 