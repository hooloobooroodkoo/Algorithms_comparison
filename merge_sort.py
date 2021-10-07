COUNT = 0

def merge(left, right):
    global COUNT
    sorted_list = []
    left_i = right_i = 0
    left_len, right_len = len(left), len(right)
    for _ in range(left_len + right_len):
        COUNT = COUNT + 1
        if left_i < left_len and right_i < right_len:
            if left[left_i] <= right[right_i]:
                sorted_list.append(left[left_i])
                left_i += 1
            else:
                sorted_list.append(right[right_i])
                right_i += 1
        elif left_i == left_len:
            sorted_list.append(right[right_i])
            right_i += 1
        elif right_i == right_len:
            sorted_list.append(left[left_i])
            left_i += 1
    return sorted_list

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    return merge(left_list, right_list)

def merge_sort_main(lst):
    sorted_arr = merge_sort(lst)
    return sorted_arr, COUNT