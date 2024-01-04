# Script série de Fourier 
from lab import *

T=0.4 #período
a0= 1.75 
w0=2*pi/T #frequência fundamental
T1 = 0.1
T2 = 0.2
t=timevar(20)
t01 = 0.55    
t02 = 0.7
N=10# número de harmónicas   
x_n=a0
#x_t = a0
for k in range(1, N + 1):
    bk1 = (20*sin(((k * pi * (T1)))  / T) / (k * pi))*exp(-1j*k*w0*t01)
    bk2 = ((-10)*sin(((k * pi *(T2)))  / T) / (k * pi))*exp(-1j*k*w0*t02)
    bk = (bk1 + bk2)
    ak = bk / (1j * w0 * k)
    if k == 3:
        print("b",k, "=", bk)
        print("a",k, "=", ak)
    b_k1 = 20*sin((((-k) * pi * (T1)))  / T) / ((-k) * pi) *exp(-1j*(-k)*w0*t01)
    b_k2 = (-10)*sin((((-k) * pi * (T2)))/ T) / ((-k) * pi) *exp(-1j*(-k)*w0*t02)
    b_k = b_k1 + b_k2
    a_k = b_k / (1j * w0 * (-k))
    if k == 1:
        print("b",-k, "=", b_k)
        print("a",-k, "=", a_k)
    x_n = x_n+ak*exp(k*w0*t*1j)+a_k*exp((-k)*w0*t*1j)
    #x_n = x_n + 2 * abs(ak) * cos(k * w0 * t + angle(ak))
    tplot(x_n)
    