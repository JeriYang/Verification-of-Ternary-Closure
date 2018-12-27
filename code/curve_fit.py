import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
y = np.array([0.06 ,0.15 ,0.24 ,0.31 ,0.34 ,0.38 ,0.32 ,0.36 ,0.37 ,0.38 ,0.35 ,0.17 ,0.15 ,0.23 ,0.25 ,0.20 ,0.50 ,0.50 ,0.67 ,0.33 ,0.33 ])
z1 = np.polyfit(x, y, 2)#用3次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)

plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
plt.xlabel("k")
plt.ylabel("T(k)")
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title("Average probability function1_zct")
plt.show()
