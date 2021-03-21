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
