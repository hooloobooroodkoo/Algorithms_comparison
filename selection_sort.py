def selection_sort(lst: list) -> list:
    comparisons = 0
    for i in range(len(lst)):
        first_element_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[first_element_index]:
                comparisons += 1     
                first_element_index = j
            comparisons += 1
        lst[i], lst[first_element_index] = lst[first_element_index], lst[i]
        
    return lst, comparisons
