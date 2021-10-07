def shell_sort(lst):
    size = len(lst)
    step = size//2
    comparison = 0
    while step > 0:
        for i in range(step, size):
            comparison += 1
            flag = lst[i]
            j = i
            while j >= step and lst[j-step] > flag:
                comparison += 1
                lst[j] = lst[j-step]
                j -= step        
            lst[j] = flag
        step //= 2
    return lst, comparison