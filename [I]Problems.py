""" My solutions from daily newslatter of TechLead"""

import random
import numpy as np
import math


def sum_sorting_list(input_list, k):
    """ 24.12.2019. Find any combination of 2 number_index from list, that summ up to k """
    output_list = []
    print(input_list)
    for number_index in range(len(input_list)):
        for i in range(number_index, len(input_list)):
            if input_list[number_index] + input_list[i] == k:
                output_list.append((input_list[number_index], input_list[i]))
    return output_list

input_list = np.random.randint(1, 20, size=100)
print(sum_sorting_list(input_list, 20))


#**********************************************************************************************************************************
""" 25.12.2019. Given an array of integers, return a new array such that each element at index i of the new array 
is the product of  all the numbers in the original array except the one at i. For example,
 if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
 the expected output would be [2, 3, 6]."""


def d19_12_25_a(input_list):
    counting_var = 1
    output_list = []
    for i in range(len(input_list)):
        for index, value in enumerate(input_list):
            if index != i:
                counting_var *= value
        output_list.append(counting_var)
        counting_var = 1
    return output_list


def d19_12_25_b(input_list):
    clear_lists = [[value for index, value in enumerate(input_list) if index != i] for i in range(len(input_list))]
    return [np.prod(x) for x in clear_lists]


input_list = [1, 2, 3, 4, 5]
print(d19_12_25_b(input_list))

#**********************************************************************************************************************************

