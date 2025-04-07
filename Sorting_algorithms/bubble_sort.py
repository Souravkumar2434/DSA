

def bubble_sort(lst):
    for i in range(len(lst) -1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


num = [1,4,5,3,2]

print(bubble_sort(num))