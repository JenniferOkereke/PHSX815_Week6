import numpy as np
import math as m
import scipy.integrate as integrate

#importing my Numerical Integration Class
from Integration.Int import Integrate as I

a=-(m.pi)/2
b=(m.pi)/2
n=5
N=5
def f(X):
    func=m.cos(X)
    return func

#integral calculations for rectangle, Guass quadrature, and Monte Carlo
numint1=I.rectint(f, a, b, n)
numint2=I.GaussLeg(f,a,b)
numint3=I.MCint(f,a,b,N)
exactint=integrate.quad(f, a, b)

#Respective Errors
RectError=abs(I.rectint(f, a, b, n+1)-I.rectint(f, a, b, n))
GaussError=abs(I.GaussLeg(f, a, b)-2)
MCerror=abs(I.MCint(f,a,b,N+1)-I.MCint(f,a,b,N))

print("Area by rectangles is:", numint1, "+/-", RectError)
print("Area by Gauss-Legendre Quadrature:", numint2, "+/-", GaussError)
print("Area by Monte Carlo is:", numint3, "+/-", MCerror )

#returns the exact value of my integral and an estimation of it's error
print("Exact Area is:", exactint)