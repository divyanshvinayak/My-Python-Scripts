import numpy as np
rows = int(input('Enter rows: '))
cols = int(input('Enter columns: '))
matrix = list(range(rows))
print('Enter elements in the matrix row-wise')
for i in range(rows):
    matrix[i] = list(map(float, input().split()))
arr = np.array(matrix)
inverse = np.linalg.inv(arr)
print(inverse)
