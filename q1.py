import numpy as np
from scipy.linalg import svd


arr=[[1,3,5,7],[9,11,13,15],[17,19,21,23],[25,27,29,31]]
X,B,T=svd(arr)
print("X= ",X)
print("\n B= ",B)
print("\n T= ",T)

print("\n X+T= ",np.add(X,T))
print("\n X-T= ",np.subtract(X,T))

x=np.multiply(X,np.square(X))

print("\n 2X3 =",np.multiply(2,x))
