#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

print('Hello python')

print(sys.argv[0])
print("====================")

#list : memory address(pointer) array
#numpy ndarray : consecutive list, dimensions(row,col)-shape, strides

data = [11,22,33,44,55,66]
print(data, len(data))

datas = [[11,22,33],[44,55,66]]
print(datas, len(datas))
print("====================")

ndarray = np.array(data)
print(ndarray, len(ndarray), ndarray.size, ndarray.shape, ndarray.strides)

ndarray2 = np.array(datas)
print(ndarray2, len(ndarray2), ndarray2.size, ndarray2.shape, ndarray2.strides)


print("====================")
#Transpose
ndarray = np.array([[11,22,33],[44,55,66]])
print(ndarray)

print(ndarray.transpose())
print(ndarray.swapaxes(0,1))
print(ndarray.T)
print(np.transpose(ndarray))

print(ndarray.strides, ndarray.T.strides)
print(ndarray.shape, ndarray.T.shape)
print("====================")
ndarray = np.array([11,22,33]) + 10
print(ndarray)
ndarray = np.array([11,22,33]) * 10
print(ndarray)
ndarray = np.array([11,22,33]) * np.array([10])
print(ndarray)

print("====================")
ndarray = np.array([[11,22,33],[44,55,66]]) + 10
print(ndarray)
ndarray = np.array([[11,22,33],[44,55,66]]) * 10
print(ndarray)
ndarray = np.array([[11,22,33],[44,55,66]]) * np.array([10])
print(ndarray)

ndarray = np.array([[11,22,33],[44,55,66]]) * np.array([[10,100,1000]])
print(ndarray)

ndarray = np.array([[11,22,33],[44,55,66]]) * np.array([[10, 100]]).T
print(ndarray)


ndarray = np.array([[11,22,33],[44,55,66]]).T * np.array([10])
print(ndarray)

ndarray = np.array([[11,22,33],[44,55,66]]).T * np.array([[10],[100],[1000]])
print(ndarray)

ndarray = np.array([[11,22,33],[44,55,66]]).T * np.array([[10,100,1000]]).T
print(ndarray)


print("====================")
ndarray = np.array([[11,22,33],[44,55,66],[1,2,3]])
print(ndarray)
row = np.array([[77,88,99]])
print(ndarray + row)

print(np.concatenate((ndarray,row),axis=0))
print(np.concatenate((ndarray,row.T),axis=1))
