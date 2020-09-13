# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from random import random

from numpy.random import permutation


def generate_sample(n):
    return list(round(random(), 3) for _ in range(n))


def check_derangement(a, n):
    for i in range(n):
        if a[i] == i + 1:
            return 0
    return 1


n = [100, 1000, 10000]

# Question 1
print('\u03C0 Estimation')
for i in n:
    x = generate_sample(i)
    y = generate_sample(i)
    print('For n = {}, \u03C0 \u2248 {:.3f}'.format(i, sum(
        1 if x[j] ** 2 + y[j] ** 2 <= 1 else 0 for j in range(i)) / i * 4))

# Question 2
print('Integral Estimation')
for i in n:
    x = generate_sample(i)
    y = generate_sample(i)
    print('For n = {}, I \u2248 {:.3f}'.format(i, 1 + sum(
        1 if 1 + y[j] <= 2 / (1 + x[j] ** 2) else 0 for j in range(i)) / i))

# Question 3
print('e Estimation')
for i in n:
    a = list(range(1, i + 1))
    print('For n = {}, e \u2248 {:.5f}'.format(i, i / sum(check_derangement(permutation(a), i) for j in range(i))))
