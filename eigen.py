import numpy as np
rows = int(input('Enter rows: '))
cols = int(input('Enter columns: '))
arr = list(range(rows))
print('Enter elements in the matrix row-wise')
for i in range(rows):
    arr[i] = list(map(int, input().split()))
vals, vecs = np.linalg.eig(arr)
print(vals, vecs)
print(np.dot(np.dot(np.linalg.inv(vecs),arr),vecs))
