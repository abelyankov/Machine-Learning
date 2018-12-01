
from math import sqrt
from numpy import diag
from numpy import dot
from numpy import array
from scipy.linalg import svd

A = array([[0, 1, 1], [sqrt(2),2 , 0], [0,1, 1]])
print(A)
V, d, VT = svd(A)

Sigma = diag(d)
B = V.dot(Sigma.dot(VT))

print(V)
print(B)
print(VT)