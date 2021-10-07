import timeit
import numpy as np
from insertion_sort import insertion_sort
from merge_sort import merge_sort_main
from selection_sort import selection_sort
from shell_sort import shell_sort

def randomArraysAverageTime(power):
    sortings = [insertion_sort, merge_sort_main, selection_sort, shell_sort]
    sorting_time = {}
    for sort_method in sortings:
        sorting_time[sort_method.__name__] = [0, 0, 0]
    for i in range(0, 5):
        arr = np.random.randint(1,10001,2**power)
        for sort_method in sortings:
            start = timeit.default_timer()
            comparisons = sort_method(arr)[1]
            stop = timeit.default_timer()
            work_time = stop - start
            sorting_time[sort_method.__name__][1] += work_time
            sorting_time[sort_method.__name__][2] += comparisons
    for key in sorting_time.keys():
        sorting_time[key][1] /= 5
        sorting_time[key][2] /= 5
        sorting_time[key][0] = power
    print(sorting_time)
    return sorting_time

def ascendingOrder(power):
    sortings = [insertion_sort, merge_sort_main, selection_sort, shell_sort]
    sorting_time = {}
    arr = [i for i in range(1, 2**power+1)]
    for sort_method in sortings:
        sorting_time[sort_method.__name__] = [0, 0, 0]
        sorting_time[sort_method.__name__][0] = power
        start = timeit.default_timer()
        comparisons = sort_method(arr)[1]
        stop = timeit.default_timer()
        work_time = stop - start
        sorting_time[sort_method.__name__][1] += work_time
        sorting_time[sort_method.__name__][2] += comparisons
    print(sorting_time)
    
def decliningOrder(power):
    sortings = [insertion_sort, merge_sort_main, selection_sort, shell_sort]
    sorting_time = {}
    arr = [i for i in range(2**power, 0, -1)]
    for sort_method in sortings:
        sorting_time[sort_method.__name__] = [0, 0, 0]
        sorting_time[sort_method.__name__][0] = power
        start = timeit.default_timer()
        comparisons = sort_method(arr)[1]
        stop = timeit.default_timer()
        work_time = stop - start
        sorting_time[sort_method.__name__][1] += work_time
        sorting_time[sort_method.__name__][2] += comparisons
    print(sorting_time)

def arrayWithRepeatings(power):
    sortings = [insertion_sort, merge_sort_main, selection_sort, shell_sort]
    sorting_time = {}
    for sort_method in sortings:
        sorting_time[sort_method.__name__] = [0, 0, 0]
    for i in range(0, 3):
        arr = np.random.randint(1,4,2**power)
        for sort_method in sortings:
            start = timeit.default_timer()
            comparisons = sort_method(arr)[1]
            stop = timeit.default_timer()
            work_time = stop - start
            sorting_time[sort_method.__name__][1] += work_time
            sorting_time[sort_method.__name__][2] += comparisons
    for key in sorting_time.keys():
        sorting_time[key][1] /= 3
        sorting_time[key][2] /= 3
        sorting_time[key][0] = power
    print(sorting_time)
    return sorting_time
