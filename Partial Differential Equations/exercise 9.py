import matplotlib.pyplot as plt
import numpy as np
import math

c = float(1)
t = float(input("Masukkan nilai t: "))

y = []
x = np.arange(0,11,0.01)

for i in x :
    y.append(((1/2)*t) + ((1/(4*c))*math.sin(2*c*t) * math.cos(2*i)))
    
plt.plot(x,y,'r')
plt.xlabel('sumbu x')
plt.ylabel('u(x,t)')
plt.legend(['grafiknya'],loc="best")
plt.title('Grafik Penyelesaian dengan c=1 dan t=15')
plt.axis([0,math.pi,min(y)-0.1,max(y)+0.1])
plt.grid()
plt.show()