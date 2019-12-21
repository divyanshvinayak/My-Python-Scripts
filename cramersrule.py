import numpy as np
print('Enter values of coefficients of the equation ax + by + cz = d in space separated form')
eqs = []
det = []
detx = []
dety = []
detz = []
while True:
    try:
        a, b, c, d = map(int, input().split())
        eqs.append([a,b,c,d])
        det.append([a,b,c])
        detx.append([b,c,d])
        dety.append([a,c,d])
        detz.append([a,b,d])
    except ValueError:
        break
flag = 0
for i in range(len(eqs)):
    if eqs[i][2] != 0:
        flag = 1
        break
if flag == 0:
    for i in range(len(eqs)):
        del eqs[i][2]
        del det[i][2]
        del detx[i][1]
        del dety[i][1]
d = np.linalg.det(det)
dx = np.linalg.det(detx)
dy = np.linalg.det(dety)
dz = 0
if flag == 1:
    dz = np.linalg.det(detz)
if d != 0:
    print('Unique Solution')
else:
    if dx == 0 and dy == 0 and dz == 0:
        print('Infinite Solution')
    else:
        print('No Solution')
