import numpy as np
rows = int(input('Enter rows: '))
cols = int(input('Enter columns: '))
matrix = []
print('Enter elements in the matrix row-wise')
for i in range(rows):
    matrix.append(list(map(int, input().split())))
matrix = np.array(matrix)
vals, vecs = np.linalg.eig(matrix)
am = {}
for i in vals:
    if i not in am:
        am[i] = list(vals).count(i)
print(am)
