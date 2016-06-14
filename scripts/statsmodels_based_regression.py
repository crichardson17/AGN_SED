import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pandas as pd

Grupe_Data = pd.read_csv('C:/Users/chris_000/Documents/GitHub/AGN_SED/grupe_data/Grupe_Data.csv', sep = ',', header = 0)

Y = Grupe_Data.alphaUVc
X = Grupe_Data.alphaX


print X, Y, Grupe_Data
model = smf.ols(formula = 'Y ~ X + np.power(X,2)' , data= Grupe_Data)
res = model.fit()
print res.summary(), res.predict(X)

X2 = Grupe_Data.alphaX
X2 = sm.add_constant(X)
model2 = sm.RLM(Y,X2)
res2 = model2.fit()

print res2.summary()

