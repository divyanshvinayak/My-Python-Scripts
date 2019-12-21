#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:29:33 2019

@author: jarvis
"""

day_init = list((input().split()))
time_init = list(map(int, input().split(" : ")))
day_final = list(input().split())
time_final = list(map(int, input().split(" : ")))
if time_final[0]-time_init[0] >= 0:
    days = int(day_final[1])-int(day_init[1])
    if time_final[1]-time_init[1] >= 0:
        hours = time_final[0]-time_init[0]
        minutes = time_final[1]-time_init[1]
    else:
        hours = time_final[0]-time_init[0]-1
        minutes = 60+time_final[1]-time_init[1]
    if time_final[2]-time_init[2] >= 0:
        seconds = time_final[2]-time_init[2]
    else:
        minutes -= 1
        seconds = 60+time_final[2]-time_init[2]
if time_final[0]-time_init[0] < 0:
    days = int(day_final[1])-int(day_init[1])-1
    if time_final[1]-time_init[1] >= 0:
        hours = 24+time_final[0]-time_init[0]
        minutes = time_final[1]-time_init[1]
    else:
        hours = 23+time_final[0]-time_init[0]
        minutes = 60+time_final[1]-time_init[1]
    if time_final[2]-time_init[2] >= 0:
        seconds = time_final[2]-time_init[2]
    else:
        minutes -= 1
        seconds = 60+time_final[2]-time_init[2]
print(days, "dia(s)")
print(hours, "hora(s)")
print(minutes, "minuto(s)")
print(seconds, "segundo(s)")