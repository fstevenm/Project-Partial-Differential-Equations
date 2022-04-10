import matplotlib.pyplot as plt
import numpy as np
import math


u = []
n = float(input("Masukkan nilai n: ")) #Masukin n = 1
t = float(input("Masukkan nilai t: ")) # NOTE :Masukin 0, 0.001, 0.002, dst maks 1 udah datar
kons = float(input("Masukkan nilai k: "))
L = 0.3 #bebas
x = np.arange(0,11,0.01)

'''Gambar grafik masing2 U_n'''
for i in (x) :
    u_z = (math.e)**(-(((2*n-1)*math.pi)**2/(2*L)**2) *t*kons) * math.sin(((2*n-1)*math.pi*i)/2*L)
    u.append(u_z)

plt.plot(x,u)
plt.xlabel('sumbu x')
plt.ylabel('u(x,t)')
plt.legend(['grafiknya'],loc="best")
plt.title('Pers.difusi dengan syarat batas campuran U_({1}) saat t = {0}'.format(t, n))
plt.axis([0,10,-1,1])
plt.grid()
plt.show()


'''Untuk menjumlahkan sigma nya, Pake yang ini'''
#for i in (x) :
#    u_z = 0
#    for k in range(1,int(n+1)):
#        u_z += (math.e)**(-(((2*n-1)*math.pi)**2/(2*L)**2) *t*kons) * math.sin(((2*k-1)*math.pi*i)/2*L)
#    u.append(u_z)
#
#plt.plot(x,u)
#plt.xlabel('sumbu x')
#plt.ylabel('u(x,t)')
#plt.legend(['grafiknya'],loc="best")
#plt.title('Pers.difusi syarat batas campuran dengan n = {1} dan t = {0}'.format(t, n))
#plt.axis([0,10,-2,2])
#plt.grid()
#plt.show()



