# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as stats

m = [10, 100, 500, 1000, 5000, 10000, 50000]
n = [1, 2, 4, 8, 16, 32]
c = [0, 0, 1, 0, 0]

# Question 1(A)
print('X ~ Exp(1)')
print('E(X) = 1')
x = m
y = list(sum(round(np.random.exponential(scale=1), 2) for j in range(i)) / i for i in x)
fig, ax = plt.subplots()
l1 = ax.plot(x, y)
l2 = ax.axhline(y=1, dashes=[6, 2], color='green')
plt.xlabel('Sample Size')
plt.ylabel('Mean')
plt.title('Exponential Distribution')
plt.show()

# Question 1(B)
print('X ~ Unif(1, 2)')
print('E(X) = 1.5')
x = m
y = list(sum(round(np.random.uniform(1, 2), 2) for j in range(i)) / i for i in x)
fig, ax = plt.subplots()
l1 = ax.plot(x, y)
l2 = ax.axhline(y=1.5, dashes=[6, 2], color='green')
plt.xlabel('Sample Size')
plt.ylabel('Mean')
plt.title('Uniform Distribution')
plt.show()

# Question 1(C)
print('X ~ Bern(0.2)')
print('E(X) = 0.2')
x = m
y = list(sum(np.random.choice(c) for j in range(i)) / i for i in x)
fig, ax = plt.subplots()
l1 = ax.plot(x, y)
l2 = ax.axhline(y=0.2, dashes=[6, 2], color='green')
plt.xlabel('Sample Size')
plt.ylabel('Mean')
plt.title('Bernoulli Distribution')
plt.show()

print('WLLN, verified.')

# Question 2(A)
print('X ~ Exp(1)')
x = n
for i in x:
    dat = sorted(list(sum(np.random.exponential(scale=1) for k in range(i)) / i for j in range(1000)))
    fit = stats.norm.pdf(dat, 1, (1 / i) ** (1 / 2))
    print('For N = {}, E(X) = {:.6f}'.format(i, sum(dat) / len(dat)))
    plt.plot(dat, fit, '-o', label='Normal Distribution')
    plt.hist(dat, bins=20, density=True, label='Approximated Normal Distribution')
    plt.title('Exponential Distribution for N = {}'.format(i))
    plt.legend()
    plt.show()

# Question 2(B)
print('X ~ Unif(1, 2)')
x = n
for i in x:
    dat = sorted(list(sum(np.random.uniform(1, 2) for k in range(i)) / i for j in range(1000)))
    fit = stats.norm.pdf(dat, 1.5, (1 / (i * 12)) ** (1 / 2))
    print('For N = {}, E(X) = {:.6f}'.format(i, sum(dat) / len(dat)))
    plt.plot(dat, fit, '-o', label='Normal Distribution')
    plt.hist(dat, bins=20, density=True, label='Approximated Normal Distribution')
    plt.title('Uniform Distribution for N = {}'.format(i))
    plt.legend()
    plt.show()

# Question 2(C)
print('X ~ Bern(0.2)')
x = n
for i in x:
    dat = sorted(list(sum(np.random.choice(c) for k in range(i)) / i for j in range(1000)))
    fit = stats.norm.pdf(dat, 0.2, (0.16 / i) ** (1 / 2))
    print('For N = {}, E(X) = {:.6f}'.format(i, sum(dat) / len(dat)))
    plt.plot(dat, fit, '-o', label='Normal Distribution')
    plt.hist(dat, bins=20, density=True, label='Approximated Normal Distribution')
    plt.title('Bernoulli Distribution for N = {}'.format(i))
    plt.legend()
    plt.show()

print('CLT, verified.')