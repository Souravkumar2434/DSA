
def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while temp < lst[j] and j > -1:
            lst[j + 1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst

num = [2,1,3,4,6,5,8,7]

print(insertion_sort(num))