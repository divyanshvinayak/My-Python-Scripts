# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def pdf(x):
    return exp_lambda * np.exp(-exp_lambda * x)


def cdf(x):
    return 1 - np.exp(-exp_lambda * x)


def correlate(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sx2 = sum(i ** 2 for i in x)
    sy2 = sum(i ** 2 for i in y)
    sxy = sum(x[i] * y[i] for i in range(n))
    return (n * sxy - sx * sy) / ((n * sx2 - sx * sx) * (n * sy2 - sy * sy)) ** 0.5


# Question 1(A)
exp_lambda = 57  # average confirmed cases per hour
x = np.arange(0, 0.1, 10 ** -6)
y = pdf(x)
plt.xlabel('Wait time in hours')
plt.ylabel('Probability density')
plt.plot(x, y)
plt.show()

# Question 1(B)
print("P(X < 1/60) = {:.6f}".format(cdf(1 / 60)))

# Question 1(C)
print("P(1/60 < X < 2/60) = {:.6f}".format(cdf(1 / 30) - cdf(1 / 60)))

# Question 1(D)
print("P(X > 2/60) = {:.6f}".format(1 - cdf(1 / 30)))

# Question 1(E)
exp_lambda = 114  # average confirmed cases per hour doubles
print("P(1/60 < X < 2/60) = {:.6f}".format(cdf(1 / 30) - cdf(1 / 60)))

# Question 2(A)
df = pd.read_csv('IC252_Lab8.csv')
df['Status'] = df['Status'].replace({"Hospitalized": 1, "Recovered": 2, "Dead": 3})

# Question 2(B)
r = [['Status,Population', correlate(df['Status'], df['Population'])],
     ['Status,SexRatio', correlate(df['Status'], df['SexRatio'])],
     ['Status,Literacy', correlate(df['Status'], df['Literacy'])],
     ['Status,Age', correlate(df['Status'], df['Age'])],
     ['Status,SmellTrend', correlate(df['Status'], df['SmellTrend'])],
     ['Status,Gender', correlate(df['Status'], df['Gender'])]]
print('\n'.join('r({}) = {:.6f}'.format(k[0], k[1]) for k in r))

# Question 2(C)
print(' > '.join(['r({})'.format(k[0]) for k in sorted(r, key=lambda x: x[1], reverse=True)]))
