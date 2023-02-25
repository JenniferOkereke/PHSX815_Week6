import numpy as np
import math as m
import scipy.integrate as integrate

#importing my Numerical Integration Class
from Int import Integrate as I

a=-(m.pi)/2
b=(m.pi)/2
n=5
def f(X):
    func=m.cos(X)
    return func


numint1=I.rectint(f, a, b, n)
numint3=I.GaussLeg(f,a,b)
exactint=integrate.quad(f, a, b)

#returns the approximated area values and there values
print("Area by rectanles is:", numint1)
print("The error is:", numint1-2)
print("Area by Gauss-Legendre Quadrature:", numint3)
print("The error is:", numint3-2)

#returns the exact value of my integral and an estimation of it's error
print("Exact Area is:", exactint)