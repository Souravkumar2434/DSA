

def swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp
    return lst

def pivot(lst, pivot_idx, end_idx):
    swap_idx = pivot_idx
    for i in range(pivot_idx + 1, end_idx + 1):
        if lst[i] < lst[pivot_idx]:
            swap_idx += 1
            swap(lst, swap_idx, i)
    swap(lst, pivot_idx, swap_idx)
    return swap_idx


def quick_sort_helper(lst, left, right):
    if left < right:
        pivot_idx = pivot(lst, left, right)
        quick_sort_helper(lst, left, pivot_idx -1)
        quick_sort_helper(lst, pivot_idx + 1, right)
    return lst

def quick_sort(lst):
    return quick_sort_helper(lst, 0, len(lst) - 1)



print(quick_sort([5,3,4,2,1,6,8,7,9]))