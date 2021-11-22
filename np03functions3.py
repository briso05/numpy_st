#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

print('Hello python')

print(sys.argv[0])
print("====================")

ndarray = np.arange(10)
print(ndarray)
print(ndarray[0])

print(ndarray[0:]) # from index 0 ~
print(ndarray[5:]) # from index 5 ~
print(ndarray[5:7]) # from index 5 ~ to index 6[7-1]
print(ndarray[0:9:2]) # from index 0 ~ to index 8[9-1] by 2 steps


print("====================")
ndarray = np.arange(12).reshape(3,4)

print(ndarray)
print(ndarray[0]) # row 0(1st)
print(ndarray[1]) # 2nd row
print(ndarray[0:]) # row 0~END
print(ndarray[0:2]) # row 0~1[2-1]
# ndarray[:2]

print(ndarray[0:2,0:]) # row 0-1 col 0-End
print(ndarray[0:2,0:2]) # row 0-1 col 0-1
print(ndarray[0:2, 1:3]) # row 0-1 col 1-2
print(ndarray[1:,1:3]) # row 1-End col 1-2
print(ndarray[1:,:2]) # row 1-End col 0-2

print(ndarray[::2,::2]) # row 0,2 col 0,2

print("====================")
ndarray = np.arange(48).reshape(6,8)

print(ndarray)
print(ndarray[2:4,4:6])
print("====================")
print(ndarray)

print(ndarray[0]) # row 0
print(ndarray[3]) # row 3
print(ndarray[0:3]) # row 0-2
print(ndarray[[0,3]]) # row 0,3
print(ndarray[:,[1,5]]) # col 1,5
print(ndarray[[0,3],[1,5]]) # (0,1), (3,5)

print(ndarray[[0]]) # row 0
print(ndarray[[0,2]]) # row 0, 2
print("====================")

print(ndarray)
print(ndarray[0][3]) # both are the same!
print(ndarray[0,3])  # same!

print(ndarray[4,5])
print(ndarray[5,6])
print([ndarray[4,5], ndarray[5,6]])
print(np.array([ndarray[4,5],ndarray[5,6]]))
print(ndarray[[4,5],[5,6]])
print(ndarray[[2,3],[1,3]])
print(ndarray[[1,4],[4,2]])


print("====================")
lst = [0, 1, 2]
ndarray = np.array(lst*2)
print(ndarray)
ndarray = np.sort(ndarray)
print(ndarray)

print("====================")
lst = [0,1,2] + [0,1,2]
ndarray = np.array(lst).reshape(2,3)

lst = [0,1,2]
ndarray = np.array([lst,lst])
print(ndarray)
print(ndarray.T.flatten())
print(np.ravel(ndarray.T))

print(np.tile(np.array(lst),(2,1)))
print(np.ravel(np.tile(np.array(lst),(2,1)).T))
