""" My solutions from daily newslatter of TechLead
"""


import random
import numpy as np


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


