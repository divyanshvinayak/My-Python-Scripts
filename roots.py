import numpy as np
poly = list(map(float, input('Enter coefficients of polynomial in order of their degrees\n').split()))
print(np.roots(poly))
