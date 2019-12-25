#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 12:00:00 2019

@author: divyanshvinayak
"""

N,M = map(int, input('Order of matrix A (N x M): ').split(' x '))
A = list(range(N))
print('Enter elements in matrix rowwise')
for i in range(N):
    A[i] = list(map(float, input().split()))
flag = 1
for i in range(N):
    for j in range(M):
        if A[i][j] != A[j][i]:
            flag = 0
            break
if flag == 1:
    print('Symmetric')
else:
    print('Asymmetric')
B = [[0 for x in range(M)] for y in range(N)]
for i in range(N):
    for j in range(M):
        B[j][i] = A[i][j]
C = [[0 for x in range(N)] for y in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(M):
            C[k][i]+=int(A[k][j]*B[j][i])
flag = 1
for i in range(N):
    for j in range(M):
        if i!=j and C[i][j]!=0:
            flag = 0
            break
        if i==j and C[i][j]!=1:
            flag = 0
            break
if flag == 1:
    print('Orthogonal')
else:
    print('Non-Orthogonal')
