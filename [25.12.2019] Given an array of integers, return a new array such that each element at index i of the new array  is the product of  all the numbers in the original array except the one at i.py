import random
import numpy as np
import math

""" 25.12.2019. Given an array of integers, return a new array such that each element at index i of the new array 
is the product of  all the numbers in the original array except the one at i. For example,
 if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
 the expected output would be [2, 3, 6]."""


def d19_12_25_b(input_list):
    clear_lists = [[value for index, value in enumerate(input_list) if index != i] for i in range(len(input_list))]
    return [np.prod(x) for x in clear_lists]


input_list = [1, 2, 3, 4, 5]
print(d19_12_25_b(input_list))
