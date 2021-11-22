#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

print('Hello python')

print(sys.argv[0])
print("====================")

#1,2,3,4 arange
ndarray1 = np.arange(4)+1
ndarray1 = np.arange(1,5)
print(ndarray1)


#5,6,7,8 arange
ndarray2 = np.arange(5,9)

print(ndarray2)

print(ndarray1 + ndarray2)
print(np.add(ndarray1, ndarray2))

print(np.sum(ndarray1))
print(np.sum(np.arange(1,11)))
print(np.cumsum(np.arange(1,11))) # show calculating process by 1D ndarray

print(np.arange(1,11).sum())
print(np.arange(1,11).cumsum())

print(ndarray1 - ndarray2)
print(np.subtract(ndarray1, ndarray2))

print(ndarray1 * ndarray2)
print(np.multiply(ndarray1, ndarray2))

print(np.prod(np.arange(1,11))) # 10!
print(np.cumprod(np.arange(1,11)))
print("====================")
print(ndarray1 / ndarray2)
print(np.divide(ndarray1, ndarray2))

print("====================")
print(ndarray1 % ndarray2)
print(np.mod(ndarray1, ndarray2))

print("====================")
print(np.floor(3.14))
print(np.int32([3.14]))
print(np.array([3.14], dtype=int))

print(np.ceil(3.14))

print(np.rint(3.14))
print(np.rint(3.64))

print(ndarray1/ndarray2)
print(np.floor(ndarray1/ndarray2))
print(np.floor_divide(ndarray1, ndarray2)) # return as int type ndarray

print(np.ceil(ndarray1/ndarray2))
print(np.rint(ndarray1/ndarray2))

print("====================square")
print(ndarray1 ** ndarray2)
print(np.power(ndarray1, ndarray2))

print(np.arange(1,11) ** 2)
print(np.square(np.arange(1,11)))

print("====================square root")

print(np.arange(1,11) **(1/2))
print(np.sqrt(np.arange(1,11)))
print("====================")

print(ndarray1)
print(ndarray2)

print(np.multiply(ndarray1,ndarray2))
print(np.multiply(ndarray1,ndarray2).sum())
print(np.sum(np.multiply(ndarray1,ndarray2)))

#(i1,i2) . (j1,j2) = i1*j1 + i2*j2 => inner product of vector(Scalar value)
print(ndarray1.dot(ndarray2)) # multiply cols and sum all -> inner product of vector
print(np.dot(ndarray1,ndarray2))
print("====================")
#matrix . vector 
#[[a11 a12] [a21 a22]] . [b1, b2] = [(a11*b1 + a12*b2) (a21*b1 + a22*b2)]
arrs = np.arange(1,4+1).reshape(2,2)
print(arrs)

arr = np.arange(1,2+1)
print(arr)

print(arrs.dot(arr))
print(np.dot(arrs, arr))
print("====================")
#matrix . matrix
# |a11 a12| . |b11 b12| = |(a11*b11 + a12*b21) (a11*b12 + a12*b22)|  
# |a21 a22|   |b21 b22|   |(a21*b11 + a22*b21) (a21*b12 + a22*b22)|
print(arrs)

arrs2 = np.arange(5,8+1).reshape(2,2)
print(arrs2)

print(arrs.dot(arrs2))
print(np.dot(arrs, arrs2))

print("====================")
s = {1,2,3,1,2,3}
print(s)

print(np.unique(np.array([1,2,3,1,2,3]))) #just like set
