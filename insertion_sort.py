import numpy as np
import timeit

from numpy.lib.function_base import insert
def insertion_sort(lst):
    comparisons = 0
    for i in range(1, len(lst)):
        comparisons += 1
        key = lst[i]
        j = i - 1
        while j >= 0 and key <= lst[j]:
            lst[j+1] = lst[j]
            comparisons += 1
            j -= 1
        lst[j+1] = key
    return lst, comparisons





