#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 12:00:00 2019

@author: divyanshvinayak
"""

import numpy as np
n = int(input('Enter the degree of curve to be fitted: '))
N = int(input('Enter the number of points: '))
print('Enter values of x and y in space separated form')
x = [0 for x in range(N)]
y = [0 for x in range(N)]
for i in range(N):
    x[i], y[i] = map(float, input().split())
sx = [0 for x in range(2*n+1)]
sxy = [0 for x in range(n+1)]
for i in range(2*n+1):
    for j in range(N):
        sx[i] += x[j]**(i)
for i in range(n+1):
    for j in range(N):
        sxy[i] += y[j]*x[j]**i
M = []
for i in range(n+1):
    r = []
    for j in range(i,n+1+i):
        r.append(sx[j])
    M.append(r)
C = np.dot(np.linalg.inv(M), sxy)
print(C)
