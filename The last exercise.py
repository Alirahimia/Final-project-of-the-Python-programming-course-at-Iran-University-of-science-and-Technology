
import numpy as np                           # Ali-Rahimian
import matplotlib.pyplot as pl
Data = np.random.randn(1000)
Datar = np.round(Data,1)
x = [i/10 for i in range(-30,30)]
t= np.zeros(8)
y = []
for i in x:
            u = Datar[np.where(Datar==i)]
            u2 = np.size(u)
            y.append(u2)

pl.title('The Last Project')
pl.grid(True)
pl.xlabel('X',fontsize = 18)
pl.ylabel('Y',fontsize = 18)
pl.bar(x,y,0.4,color = 'c')
pl.plot(x,y,'--*',markersize = 12,color='k')
pl.show()
