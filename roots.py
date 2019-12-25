#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 12:00:00 2019

@author: divyanshvinayak
"""

import numpy as np
poly = list(map(float, input('Enter coefficients of polynomial in order of their degrees\n').split()))
print(np.roots(poly))
