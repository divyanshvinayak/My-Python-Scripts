n = int(input('Enter number of points: '))
print('Enter values of x and y in space separated form')
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    x[i], y[i] = map(float, input().split())
X = float(input('X = '))
Y = 0
Q = [1 for i in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j:
            Q[i] *= (X-x[j])/(x[i]-x[j])
for i in range(n):
    Y += y[i]*Q[i]
print('Y =', Y)
