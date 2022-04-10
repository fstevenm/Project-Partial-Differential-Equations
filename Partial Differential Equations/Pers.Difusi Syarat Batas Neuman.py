import matplotlib.pyplot as plt
import numpy as np
import math


u = []
n = float(input("Masukkan nilai n: "))
t = float(input("Masukkan nilai t: "))
kons = float(input("Masukkan nilai k: "))
L = 10
x = np.arange(0,11,0.01)

'''Gambar grafik masing2 U_n'''
for i in (x) :
    u_z = (math.e)**(-((n*math.pi)**2/(L)**2) *t*kons) * math.cos((n*math.pi*i)/L)
    u_z += 1/2
    u.append(u_z)

plt.plot(x,u)
plt.xlabel('sumbu x')
plt.ylabel('u(x,t)')
plt.legend(['grafiknya'],loc="best")
plt.title('Pers.difusi dengan syarat batas Neumann U_({1}) saat t = {0}'.format(t, n))
plt.axis([0,10,min(u),max(u)])
plt.grid()
plt.show()



'''Untuk menjumlahkan sigma nya, Pake yang ini'''
#for i in (x) :
#    u_z = 0
#    for k in range(1,int(n+1)):
#        u_z += (math.e)**(-((k*math.pi)**2/(L)**2) *t*kons) * math.cos((k*math.pi*i)/L)
#    u_z += 1/2
#    u.append(u_z)
#
#plt.plot(x,u)
#plt.xlabel('sumbu x')
#plt.ylabel('u(x,t)')
#plt.legend(['grafiknya'],loc="best")
#plt.title('Pers.difusi syarat batas Neumann dengan n = {1} dan t = {0}'.format(t, n))
#plt.axis([0,10,min(u),max(u)])
#plt.grid()
#plt.show()


