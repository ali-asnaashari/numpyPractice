import numpy as np
import matplotlib.pyplot as plt
from numpy import random

''' Numpy Arrays: creating Arrays '''

# Creating One-Dimensional list
list_1 = [1, 2, 3, 4, 5]
np_arr_1 = np.array(list_1, dtype=np.int8)
print(np_arr_1)

# Creating Multi-Dimensional list
m_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_m_arr_1 = np.array(m_list_1)
print(np_m_arr_1)

# arrange ---> start - stop - step
print(np.arange(1, 10, 2))

# linspace
print(np.linspace(0, 5, 7))

# zeros ---> arrays that just filled up with zeros
print(np.zeros(4))
print(np.zeros((2, 3)))

# ones ---> arrays that just filled up with ones
print(np.ones(3))
print(np.ones((3, 2)))

# size ---> number of items that inside array
print(f'size = {np_m_arr_1.size}')

# Generate array using default values
np_arr_2 = np.array([1, 2, 3, 4, 5, 6])
print(np_arr_2)

# get dtype
print(f'dtype = {np_arr_2.dtype}')

# Generate Random array
print(np.random.randint(10, 50, 5))
print(np.random.randint(10, 50, size=(2, 3)))

''' Slicing & indexes '''
print(np_m_arr_1)
# get
print(np_m_arr_1[0, 0])
print(np_m_arr_1.item(0, 2))
# set
np_m_arr_1.itemset((0, 1), 1)
print(np_m_arr_1)
# Shape
print(np_m_arr_1.shape)
# take ---> get specific value by index
print(np.take(np_m_arr_1, [0, 3, 6]))
# put ---> replace provided index values with new values
np.put(np_m_arr_1, [0, 3, 6], [10, 9, 8])
print(np_m_arr_1)
# slicing One-Dimensional array
print(np_arr_1)
print(np_arr_1[:5:2])
# slicing Two-Dimensional array ---> Get Second Value Each row
print(np_m_arr_1)
print(np_m_arr_1[:, 1])
# flip
print(np_m_arr_1[::-1])
# get even value
evenValue = np_m_arr_1[np_m_arr_1 % 2 == 0]
print(evenValue)
# get value grater than 5 and equal to 10
print(np_m_arr_1[(np_m_arr_1 > 5) & (np_m_arr_1 == 10)])
# get unique value
print(np.unique(np_m_arr_1))

''' Reshaping Arrays '''
print(np_m_arr_1)
print(np_m_arr_1.reshape((1, 9)))
print(np.resize(np_m_arr_1, (2, 5)))
# transpose
print(np_m_arr_1)
print(np_m_arr_1.transpose())
# swapaxes
print(np_m_arr_1)
print(np_m_arr_1.swapaxes(0, 1))
# Flatten
print(np_m_arr_1)
print(np_m_arr_1.flatten())
# Flatten Column order
print(np_m_arr_1)
print(np_m_arr_1.flatten('F'))
# sort
print(np_m_arr_1)
# Column
np_m_arr_1.sort(axis=0)
print(np_m_arr_1)
# Row
np_m_arr_1.sort(axis=1)
print(np_m_arr_1)
