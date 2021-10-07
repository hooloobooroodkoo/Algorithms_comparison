from average_time import randomArraysAverageTime, ascendingOrder, decliningOrder, arrayWithRepeatings


# for degree in range(7, 16):
#     randomArraysAverageTime(degree)

# for degree in range(7, 16):
#     ascendingOrder(degree)

# for degree in range(7, 16):
#     decliningOrder(degree)

for degree in range(7, 16):
    arrayWithRepeatings(degree)


































# randnums2= np.random.randint(1,10001,2**9)
# randnums3= np.random.randint(1,10001,2**11)
# randnums4= np.random.randint(1,10001,2**13)
# randnums5= np.random.randint(1,10001,2**15)
# sorted_numbers1 = [i for i in range(1, 2**7)]
# sorted_numbers2 = [i for i in range(1, 2**9)]
# sorted_numbers3 = [i for i in range(1, 2**11)]
# sorted_numbers4 = [i for i in range(1, 2**13)]
# sorted_numbers5 = [i for i in range(1, 2**15)]
# arrays = [randnums1, randnums2, randnums3, randnums4, randnums5]
# sorted_arrays = [sorted_numbers1, sorted_numbers2, sorted_numbers3, sorted_numbers4, sorted_numbers5]

# power = 7
# for arr in arrays:
#     power += 2
#     for sort_method in sortings:
#         start = timeit.default_timer()
#         sort_method(arr)
#         stop = timeit.default_timer()
#         print('Time of', sort_method.__name__, f'2^{power}: ', stop - start)
# power = 7
# for arr in sorted_arrays:
#     power += 2
#     for sort_method in sortings:
#         start = timeit.default_timer()
#         sort_method(arr)
#         stop = timeit.default_timer()
#         print('Time of', sort_method.__name__, f'sorted 2^{power}: ', stop - start)
# power = 7
# for arr in sorted_arrays:
#     power += 2
#     for sort_method in sortings:
#         start = timeit.default_timer()
#         sort_method(arr.reverse())
#         stop = timeit.default_timer()
#         print('Time of', sort_method.__name__, f'sorted 2^{power}: ', stop - start)
# start2 = timeit.default_timer()
# merge_sort(randnums)
# stop2 = timeit.default_timer()
# print('Time of merge sort 2^7: ', stop2 - start2)

# start3 = timeit.default_timer()
# selection_sort(randnums)
# stop3 = timeit.default_timer()
# print('Time of selection sort 2^7: ', stop3 - start3)

# start4 = timeit.default_timer()
# shell_sort(randnums)
# stop4 = timeit.default_timer()
# print('Time shell sort 2^7: ', stop4 - start4, '\n')



# start5 = timeit.default_timer()
# insertion_sort(randnums2)
# stop5 = timeit.default_timer()
# print('Time of insertion sort 2^9: ', stop5 - start5)

# start6 = timeit.default_timer()
# merge_sort(randnums2)
# stop6 = timeit.default_timer()
# print('Time of merge sort 2^9: ', stop6 - start6)

# start7 = timeit.default_timer()
# selection_sort(randnums2)
# stop7 = timeit.default_timer()
# print('Time of selection sort 2^9: ', stop7 - start7)

# start8 = timeit.default_timer()
# shell_sort(randnums2)
# stop8 = timeit.default_timer()
# print('Time shell sort 2^9: ', stop8 - start8, '\n')



# start9 = timeit.default_timer()
# insertion_sort(randnums3)
# stop9 = timeit.default_timer()
# print('Time of insertion sort 2^11: ', stop9 - start9)

# start10 = timeit.default_timer()
# merge_sort(randnums3)
# stop10 = timeit.default_timer()
# print('Time of merge sort 2^11: ', stop10 - start10)

# start11 = timeit.default_timer()
# selection_sort(randnums3)
# stop11 = timeit.default_timer()
# print('Time of selection sort 2^11: ', stop11 - start11)

# start12 = timeit.default_timer()
# shell_sort(randnums3)
# stop12 = timeit.default_timer()
# print('Time shell sort 2^11: ', stop12 - start12, '\n')



# start13 = timeit.default_timer()
# insertion_sort(randnums4)
# stop13 = timeit.default_timer()
# print('Time of insertion sort 2^13: ', stop13 - start13)

# start14 = timeit.default_timer()
# merge_sort(randnums4)
# stop14 = timeit.default_timer()
# print('Time of merge sort 2^13: ', stop14 - start14)

# start15 = timeit.default_timer()
# selection_sort(randnums4)
# stop15 = timeit.default_timer()
# print('Time of selection sort 2^13: ', stop15 - start15)

# start16 = timeit.default_timer()
# shell_sort(randnums4)
# stop16 = timeit.default_timer()
# print('Time shell sort 2^13: ', stop16 - start16, '\n')



# start17 = timeit.default_timer()
# insertion_sort(randnums5)
# stop17 = timeit.default_timer()
# print('Time of insertion sort 2^15: ', stop17 - start17)

# start18 = timeit.default_timer()
# merge_sort(randnums5)
# stop18 = timeit.default_timer()
# print('Time of merge sort 2^15: ', stop18 - start18)

# start19 = timeit.default_timer()
# selection_sort(randnums5)
# stop19 = timeit.default_timer()
# print('Time of selection sort 2^15: ', stop19 - start19)

# start20 = timeit.default_timer()
# shell_sort(randnums5)
# stop20 = timeit.default_timer()
# print('Time shell sort 2^15: ', stop20 - start20)
