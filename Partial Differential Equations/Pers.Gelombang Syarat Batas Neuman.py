import matplotlib.pyplot as plt
import numpy as np
import math


u = []
n = float(input("Masukkan nilai n: ")) # n = 1 (bebas)
t = float(input("Masukkan nilai t: ")) #Masukkan t dari 0 sampe 3
c= float(input("Masukkan nilai c: "))
L = 10 #bebas
x = np.arange(0,11,0.01)

'''Gambar grafik masing2 U_n'''
for i in (x) :
    u_z = (math.cos((n*math.pi*t*c)/L) - 12 * math.sin((n*math.pi*t*c)/L))*(math.cos((n*math.pi*i)/L))
#    u_z += 1/2 + 1/2 * t #setel A0 =0 dan B0 = 0
    u.append(u_z)

plt.plot(x,u)
plt.xlabel('sumbu x')
plt.ylabel('u(x,t)')
plt.legend(['grafiknya'],loc="best")
plt.title('Pers.gelombang dengan syarat batas Neumann U_({1}) saat t = {0}'.format(t, n))
plt.axis([0,10,-15,15])
plt.grid()
plt.show()



'''Untuk menjumlahkan sigma nya, Pake yang ini'''
#for i in (x) :
#    u_z = 0
#    for k in range(1,int(n+1)):
#        u_z += (math.cos((k*math.pi*t*c)/L) + math.sin((k*math.pi*t*c)/L)) * math.cos((k*math.pi*i)/L)
#    u_z += 1/2 + 1/2*t #setel A0 =0 dan B0 = 0
#    u.append(u_z)
#
#plt.plot(x,u)
#plt.xlabel('sumbu x')
#plt.ylabel('u(x,t)')
#plt.legend(['grafiknya'],loc="best")
#plt.title('Pers.gelombang syarat batas Neumann dengan n = {1} dan t = {0}'.format(t, n))
#plt.axis([0,10,-15,15])
#plt.grid()
#plt.show()



