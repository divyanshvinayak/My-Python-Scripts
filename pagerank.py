#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 12:00:00 2019

@author: divyanshvinayak
"""

import numpy as np
N = int(input('Enter number of webpages: '))
A = []
print('Enter 1 if there is a link from it to that webpage else enter 0 for all webpages in space separated form')
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    S = 0
    for j in range(N):
        S += A[j][i]
    for j in range(N):
        A[j][i] /= S
X = [1 for y in range(N)]
while True:
    C = np.dot(A,X)
    print(C)
    X = C
    D = np.dot(A,X)
    if max(C-D) < 0.01:
        print(D)
        break
