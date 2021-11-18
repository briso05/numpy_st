#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

print('Hello python')

print(sys.argv[0])
print("====================")

ndarray = np.array([[11,22,33],[44,55,66],[77,88,99]])
print(ndarray)

print(ndarray.tolist())

print(ndarray.__eq__(33))
print(ndarray.__ne__(33))

print(ndarray.__lt__(33))
print(ndarray.__gt__(33))

print(ndarray.__le__(33))
print(ndarray.__ge__(33))

print("====================min, max")
print(ndarray.min())
print(ndarray.max())

print("====================amin, amax [axis=0] : find row where min/max value exists")
print(np.amin(ndarray,axis=0)) #axis= can be omitted
print(np.amin(ndarray,0))
print(np.amax(ndarray,axis=0))
print(np.amax(ndarray,0))

print("====================amin, amax [axis=1]")
print(np.amin(ndarray,axis=1))
print(np.amin(ndarray,1))
print(np.amax(ndarray,axis=1))
print(np.amax(ndarray,1))


print("====================ptp : max value - min value")
ndarray = np.random.randint(100,size=(3,3))
print(ndarray)
print(ndarray.max())
print(ndarray.min())
print(ndarray.ptp()) #max-min
print(ndarray.ptp(0)) #max value in a col - min value in a col
print(ndarray.ptp(1)) #max value in a row - min value in a row


print("====================median")
ndarray = np.random.randint(100,size=(3,4))
print(ndarray)
print(np.median(ndarray)) #the value which exists in the middle of row*col
print(np.median(ndarray,0)) # the value exists in the middle of the col
print(np.median(ndarray,1)) # the value exists in the middle og the row


print("====================var(): variance")
ndarray = np.array([3,4,5,6,7])
print(ndarray)
print((4+1+0+1+4)/5)
print(np.var(ndarray))


print("====================std(): standard deviation")
#sqrt(var()) == std()
print(np.sqrt(np.var(ndarray)))
print(np.std(ndarray))


print("====================2d var(): variance")
ndarray = np.array([[3,4,5,6,7],[1,3,5,7,9],[10,20,30,40,50]])
print(ndarray)
print(np.var(ndarray,0))
print(np.var(ndarray,1))
