#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

print('Hello python')

print(sys.argv[0])
print("====================")

lst = ["kim",100,3.14]


print(lst)

print("====================")
#numpy array should contains the same datas
ndarray = np.array([1,2,3])
print(ndarray)
print(ndarray.dtype)

print("====================")
ndarray = np.array([1,2,3,3.14])
print(ndarray)
print(ndarray.dtype)

print("====================")
ndarray = np.array([1,2,3,3.14,"kim"])
print(ndarray)
print(ndarray.dtype)

print("====================")
print(type(ndarray))

print("====================")

ndarray = np.int32([1,2,3,3.14]) #float will be casted into int(3.14 -> 3)
#ndarray = np.int32([1,2,3,3.14,'aaa']) #Error
print(ndarray)
print(ndarray.dtype)

print("====================")

ndarray = np.float64([1,2,3,3.14]) #int will be casted into float(1 -> 1.|2 -> 2. |3 -> 3.)
#ndarray = np.float64([1,2,3,3.14,'aaa']) #Error
print(ndarray)
print(ndarray.dtype)

print("====================")

lst = [1.1,3.14,55.55]
ndarray = np.array(lst)
print(ndarray)

ndarray = np.array(lst, dtype=np.int32)
print(ndarray)

ndarray = np.int32(lst)
print(ndarray)

print("====================")

ndarray = np.array([True, False, False])
print(ndarray)

ndarry = np.array([0,1,True], dtype=np.bool8)
print(ndarray)

ndarray = np.bool8([0, True, 1, False])
print(ndarray)

print("====================")

ndarray = np.array(['kim', 'lee', 'choi'])
print(ndarray)
print(ndarray.dtype)

print("====================")

ndarray = np.array(["kim", "lee", "choi"])
print(ndarray)
print(ndarray.dtype)

print("====================")

ndarray = np.array([1+1j,2+2j,3+3j])
print(ndarray)
print(ndarray.dtype)

print("====================")
ndarray = np.array([[1,2,3],[3,4,5]])
print(ndarray)
print(type(ndarray))
print(ndarray.dtype)

print("====================")
lst = [range(10)]
print(lst)

lst = list(range(10))
print(lst)

lst = [i for i in range(10)]
print(lst)

ndarray = np.array(range(10))
print(ndarray)

ndarray = np.array(range(1,20))
print(ndarray)

ndarray = np.array(range(10, 30, 2))
print(ndarray)

ndarray = np.array(range(10, 0, -1))
print(ndarray)
print("====================")

#Using N Variables

bean01 = 100
bean02 = 200
bean03 = 300

sum = bean01 + bean02 + bean03
print(sum)
print(sum/3)

print("====================")
#Using List

beans = [100,200,300,400]
sum = 0
for bean in beans:
    sum += bean
print(sum, sum/len(beans))

print("====================")
#Using List + increase 10 all items

beans = [100,200,300,400]
beans2 = []

for bean in beans:
    beans2.append(bean+10)

sum = 0
for bean in beans2:
    sum += bean
print(sum, sum/len(beans2))
print("====================")
#numpy.array

beans = [100,200,300,400]
ndarray = np.array(beans)

print(np.sum(ndarray), np.mean(ndarray))
print("====================")
#numpy.array + 10
beans = [100,200,300,400]
ndarray = np.array(beans) + 25

print(np.sum(ndarray), np.mean(ndarray))

print("====================")
#numpy.array + 10
beans_list = [[100,200,300,400],[10,20,30,40]]
ndarray = np.array(beans_list) + 25

print(np.sum(ndarray), np.mean(ndarray))

print("====================")
print("np.mean & np.average")
print("mean:", np.mean(range(11)))
print("average:", np.average(range(11)))
print("average:", np.average(range(11),weights=range(0,11,1)))
print("average:", np.average(range(11),weights=range(10,-1,-1)))


print("====================")
print("axis=1, axis=0")
print(beans_list)

print(np.sum(beans_list))
print("rows sum:",np.sum(beans_list, axis=1))
print("col sum:",np.sum(beans_list, axis=0))

print("====================")
print("import random")
import random

lst = []
for i in range(10):
    #lst.append(random.random())
    lst.append(random.randrange(1,100+1))
print(lst)


print("====================")
print("numpy random : randn")
ndarray = np.random.randn(10)
print(ndarray)

print("====================")
print("numpy random : randint")
ndarray = np.random.randint(10, size=(10))
print(ndarray)
print("item length:",len(ndarray))

#2row * 5col = 10
ndarray = np.random.randint(10, size=(2,5))
print(ndarray)
print("row length:",len(ndarray))

#3row * 4col = 12
ndarray = np.random.randint(12, size=(3,4))
print(ndarray)
print("row length:",len(ndarray)) #row length


print("====================")
print("numpy random : rand")
ndarray = np.random.rand(3,4)
print(ndarray)
print("row length:", len(ndarray))
print("====================")

print(ndarray[0], ndarray[0][0])
print(ndarray[1])
print(ndarray[2])
print("====================")

print([ndarray[0][0],ndarray[1][0],ndarray[2][0]])
print(ndarray[0:,0])
print(ndarray[0:,1])
        
print("====================")
#choice row : fancy indexing

print(ndarray[0])
print(ndarray[[0]])
print(ndarray[[0,1]])
print(ndarray[[0,2]])

print("====================")
print("boolean indexing")

print(ndarray[[True, False, True]])

ndarray = np.array(range(6))
print(ndarray) # 0 1 2 3 4 5 
print(ndarray[[True,False,True,False,False,True]])

print("====================")
print("operator indexing")

ndarray = np.array(range(10))
print(ndarray)
print(ndarray[ndarray%2==0])

print(ndarray[(ndarray%2==0) & (ndarray>3)])


print("====================")
print("tolist()")

lst = ndarray[ndarray%2!=0].tolist()
print(lst)
print(type(lst))

print("====================")
print("list vs ndarray : speed")
random_2d_ndarray = np.random.randint(100, size=(3000,300))
lst = random_2d_ndarray.tolist()

print(len(random_2d_ndarray))
print(random_2d_ndarray.size)
print(len(lst))

def list_sum():
    all_sum=0
    for row in lst:
        temp_sum=0
        for col in row:
           temp_sum += col
        all_sum += temp_sum
    return all_sum
    
        


import time
print(time.time())


start_time = time.time()

#print(list_sum())
print(np.sum(random_2d_ndarray))

run_time = time.time() - start_time
print("run_time:", run_time)

