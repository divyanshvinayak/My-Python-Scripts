from random import randint, random
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

p = .25
q = .35
n = 10000
X = [0] * n
Y = [0] * n
x0y0 = x1y0 = x0y1 = x1y1 = 0
for i in range(n):
    x = randint(0, 1)
    if x == 0:
        if random() < p:
            Y[i] = 1
            x0y1 += 1
        else:
            x0y0 += 1
    else:
        if random() < q:
            x1y0 += 1
        else:
            Y[i] = 1
            x1y1 += 1
        X[i] = 1
for i in range(1, n):
    X[i] += X[i - 1]
    Y[i] += Y[i - 1]

# Question 1
print('P(Y = 0) = P(Y = 0 | X = 0).P(X = 0) + P(Y = 0 | X = 1).P(X = 1) = {:.4f} + {:.4f} = {:.4f}'.format(x0y0 / n,
                                                                                                           x1y0 / n,
                                                                                                           1 - Y[
                                                                                                               -1] / n))
print('P(Y = 1) = P(Y = 1 | X = 0).P(X = 0) + P(Y = 1 | X = 1).P(X = 1) = {:.4f} + {:.4f} = {:.4f}'.format(x0y1 / n,
                                                                                                           x1y1 / n,
                                                                                                           Y[-1] / n))

# To plot the scatter diagram of Y and size of input sequence
plt.scatter(list(range(n)), Y)
plt.title('Distribution of Y')
plt.xlabel('Size of input sequence')
plt.ylabel('Count of Y = 1')
plt.show()

# Question 2
print('P(Y = 0 | X = 0) = P(X = 0, Y = 0) / P(X = 0) = {:.4f} / {:.4f} = {:.4f}'.format(x0y0 / n, 1 - X[-1] / n,
                                                                                        x0y0 / (n - X[-1])))
print('P(Y = 1 | X = 0) = P(X = 0, Y = 1) / P(X = 0) = {:.4f} / {:.4f} = {:.4f}'.format(x0y1 / n, 1 - X[-1] / n,
                                                                                        x0y1 / (n - X[-1])))
print('P(Y = 0 | X = 1) = P(X = 1, Y = 0) / P(X = 1) = {:.4f} / {:.4f} = {:.4f}'.format(x1y0 / n, X[-1] / n,
                                                                                        x1y0 / X[-1]))
print('P(Y = 1 | X = 1) = P(X = 1, Y = 1) / P(X = 1) = {:.4f} / {:.4f} = {:.4f}'.format(x1y1 / n, X[-1] / n,
                                                                                        x1y1 / X[-1]))

# To plot the 3D graph of X, Y and P(X, Y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [0, 0, 1, 1]
y = [1, 0, 1, 0]
z = [x0y0 / (n - X[-1]), x0y1 / (n - X[-1]), x1y0 / X[-1], x1y1 / X[-1]]
ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('P(X, Y)')
plt.show()
