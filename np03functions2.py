#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

print('Hello python')

print(sys.argv[0])
print("====================")

ndarray = np.array([1,2,3])
ndarray = np.array([[1,2,3],[4,5,6]])

print(ndarray) #[1 2 3]  or  array([1,2,3])
print(type(ndarray)) #class 'numpy.ndarray'

print("====================")

ndarray = np.array(range(1,4))
print(ndarray)

ndarray = np.array([range(1,4), range(4,7)])
print(ndarray)
print("====================")

ndarray = np.random.randint(7, size=(3))
print(ndarray)

ndarray = np.random.randint(7, size=(2,3))
print(ndarray)

print("====================empty")
ndarray = np.empty(3, dtype=int)
print(ndarray)

ndarray = np.empty((2,3), dtype=int)
print(ndarray)

print("====================zeros :dtype=int")
ndarray = np.zeros(3, dtype=int)
print(ndarray)

ndarray = np.zeros((2,3), dtype=int)
print(ndarray)

ndarray = np.array([0 for i in range(3)])
print(ndarray)

print("====================zeros : dtype=float")

ndarray = np.zeros(3)
print(ndarray)

ndarray = np.zeros((2,3))
print(ndarray)
print("====================ones : dtype:int")

ndarray = np.ones(3, dtype=int)
print(ndarray)

ndarray = np.ones((2,3), dtype=int)
print(ndarray)

print("====================")
ndarray = np.array([range(5), range(5)])
print(ndarray)

print(np.empty_like(ndarray))
print(np.zeros_like(ndarray))
print(np.ones_like(ndarray))

print("====================")

print(np.full(3,3)) #[3 3 3]
print(np.full(4,3)) #[3 3 3 3]
print(np.full((2,4), 3)) #[[3 3 3 3][3 3 3 3]]
print("====================")

print(np.eye(3))
print(np.eye(3,1))
print(np.eye(2,3,1))

print("====================arange")
print(np.array(range(10)))
print(np.arange(10))

print(np.arange(start=10, stop=20, step=2))
print(np.arange(10,20,2))

print(np.arange(10,20,2)+1)
print(np.arange(10)+1)

print("====================reshape")
ndarray = np.arange(10)
print(ndarray)
print(ndarray.shape, ndarray.ndim)

ndarray = ndarray.reshape(2,5)
print(ndarray)
print(ndarray.shape, ndarray.ndim)

print(ndarray.reshape(10))
print("====================flatten : n-D array -> 1-D array")
ndarray = np.arange(12).reshape(3,4)
print(ndarray)

print(ndarray.flatten())
print("====================ravel :  n-D array -> 1-D array (numpy function)")
ndarray = np.arange(12).reshape(3,4)
print(ndarray)

print(np.ravel(ndarray))

print("====================linspace(numpy function)")
ndarray = np.linspace(0,9,5)
print(ndarray)

ndarray = np.linspace((0,0,0),(9,9,9),5)
print(ndarray)

ndarray = np.linspace(0,1,20)
print(ndarray)

#import matplotlib.pyplot as plt
#plt.plot(ndarray, 'o')
#plt.show()

