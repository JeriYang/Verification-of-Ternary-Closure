import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
y = np.array([0.06 ,0.15 ,0.24 ,0.31 ,0.34 ,0.38 ,0.32 ,0.36 ,0.37 ,0.38 ,0.35 ,0.17 ,0.15 ,0.23 ,0.25 ,0.20 ,0.50 ,0.50 ,0.67 ,0.33 ,0.33 ])
def func(x,a,b):
    return a*np.exp(b/x)
popt, pcov = curve_fit(func, x, y)
a=popt[0]#popt里面是拟合系数，读者可以自己help其用法
b=popt[1]
yvals=func(x,a,b)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
plt.xlabel("k")
plt.ylabel("T(k)")
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title("Average probability function2_zct")
plt.show()
