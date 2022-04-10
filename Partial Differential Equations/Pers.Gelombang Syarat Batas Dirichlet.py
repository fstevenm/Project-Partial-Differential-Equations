import matplotlib.pyplot as plt
import numpy as np
import math


u = []
n = int(input("Masukkan nilai n: "))
t = float(input("Masukkan nilai t: "))
c = float(input("Masukkan nilai c: "))
L = 10
x = np.arange(0,11,0.01)

'''Gambar grafik masing2 U_n'''
for i in (x) :
    u_z = (math.cos((n*math.pi*t*c)/L) + math.sin((n*math.pi*t*c)/L))*math.sin((n*math.pi*i)/L)
    u.append(u_z)
    
plt.plot(x,u)
plt.xlabel('sumbu x')
plt.ylabel('u(x,t)')
plt.legend(['grafiknya'],loc="best")
plt.title('Pers.gelombang dengan syarat batas Dirichlet U_({1}) saat t = {0}'.format(t, n))
plt.axis([0,10.5,-2,2])
plt.grid()
plt.show()


    
'''Untuk menjumlahkan sigma nya, Pake yang ini'''
#for i in (x) :
#    u_z = 0
#    for k in range(1,n+1):
#        u_z += (math.cos((k*math.pi*t*c)/L) + math.sin((k*math.pi*t*c)/L))*math.sin((k*math.pi*i)/L)
#    u.append(u_z)
#
#plt.plot(x,u)
#plt.xlabel('sumbu x')
#plt.ylabel('u(x,t)')
#plt.legend(['grafiknya'],loc="best")
#plt.title('Pers.gelombang syarat dengan batas Dirichlet dengan n = {1} dan t = {0}'.format(t, n))
#plt.axis([0,10.5,-2,2])
#plt.grid()
#plt.show()
