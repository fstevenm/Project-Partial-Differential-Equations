import matplotlib.pyplot as plt
import numpy as np
import math

'''Peny. Pers. Gelombang dengan syarat batas u_x(0,t) = u(L,t) = 0'''
u = []
n = float(input("Masukkan nilai n: ")) # NOTE : masukin 2 biar sama sperti punya Bu Lusi
t = float(input("Masukkan nilai t: ")) # NOTE : Masukin 0,1,2,3,4....
c = float(input("Masukkan nilai c: ")) # c = 1
L = 10 
x = np.arange(0,11,0.01)

'''Gambar grafik masing2 U_n'''
for i in (x) :
    u_z = (math.cos(((2*n-1)*math.pi*t*c)/(2*L)) + math.sin(((2*n-1)*math.pi*t*c)/(2*L))) * math.cos(((2*n-1)*math.pi*i)/(2*L))
    u.append(u_z)

plt.plot(x,u)
plt.xlabel('sumbu x')
plt.ylabel('u(x,t)')
plt.legend(['grafiknya'],loc="best")
plt.title('Peny. Pers.gelombang dengan syarat batas u_x(0,t) = u(L,t) = 0 untuk U_({1}) saat t = {0}'.format(t, n))
plt.axis([0,10,-1.5,1.5])
plt.grid()
plt.show()



'''Untuk menjumlahkan sigma nya, Pake yang ini'''
#for i in (x) :
#    u_z = 0
#    for k in range(1,int(n+1)):
#        u_z += (math.cos(((2*k-1)*math.pi*t*c)/(2*L)) + math.sin(((2*k-1)*math.pi*t*c)/(2*L))) * math.cos(((2*k-1)*math.pi*i)/(2*L))
#    u.append(u_z)
#
#plt.plot(x,u)
#plt.xlabel('sumbu x')
#plt.ylabel('u(x,t)')
#plt.legend(['grafiknya'],loc="best")
#plt.title('Peny. Pers.gelombang syarat batas u_x(0,t) = u(L,t) = 0 dengan n = {1} dan t = {0}'.format(t, n))
#plt.axis([0,10,-3,3])
#plt.grid()
#plt.show()




