import numpy as np
import os
import matplotlib.pyplot as plt
def data(filename, column):
    results=np.genfromtxt("asu.csv", delimiter=',',skip_header=1)
    return [result[column] for result in results]
ax=data("asu.csv",0)
aox=data("asu.csv",4)
auv=data("asu.csv",6)
auverr=data("asu.csv",7)
axerr=data("asu.csv",1)
line=np.polyfit(ax,aox,1)
p=np.poly1d(line)
fig=plt.figure()
graph=fig.add_subplot(111)
graph.errorbar( ax, aox,xerr=axerr, ls='none' , marker="o")
graph.set_ylabel(r'$\alpha_{uv}$')
graph.set_xlabel(r'$\alpha_x$')
plt.plot(ax,aox,'yo',ax, p(ax),'--k')
plt.show()
print(line)