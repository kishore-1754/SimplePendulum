import numpy as np
from math import sin
"""General equation of pendulum is
θ'' + (g/L)sinθ = 0
For small angles: θ < 0.24 rad ≈ 13.7°
then: sinθ ≈ θ
Hence: θ'' + (g/L)θ = 0
Comparing with the general SHM equation:
x'' + ω²x = 0
we get:
ω² = g/L
and x ↔ θ
let :
θ = e^(rt)
Then:
θ' = re^(rt)
θ'' = r²e^(rt)
Substituting into the equation:
r²e^(rt) + ω²e^(rt) = 0
e^(rt)(r² + ω²) = 0
Since: e^(rt) ≠ 0
we get the characteristic equation:
r² + ω² = 0
Solving: r = ± iω
Hence the solutions are:
e^(iωt) and e^(-iωt)
Using Euler's formulas:
e^(iθ) = cosθ + isinθ
e^(-iθ) = cosθ - isinθ
The general solution becomes:
θ(t) = C₁e^(iωt) + C₂e^(-iωt)
Substituting Euler's formulas and rearranging:
θ(t) = A cos(ωt) + B sin(ωt)
This can also be written as:
θ(t) = C cos(ωt + φ)
hence 
x=Lsinθ
y=-Lcosθ
"""
def RK4(F,x,y,h,L,g=9.8):
    k0=h*F(x,y,L)
    k1=h*F(x+h/2.0,y+k0/2.0,L,g)
    k2=h*F(x+h/2.0,y+k1/2.0,L,g)
    k3=h*F(x+h,y+k2,L,g)
    return (k0+2.0*k1+2.0*k2+k3)/6.0

def IntegrateUsingRK(F,x,y,stopx,h,L,g):
    X=[]
    Y=[]
    X.append(x)
    Y.append(y)
    while x < stopx:
        h=min(h,stopx-x)
        y=y+RK4(F,x,y,h,L,g)
        x=x+h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)
    