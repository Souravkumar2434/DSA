

def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_idx = i
        for j in range(i + 1, len(lst)):
            # my logic
            # if lst[i] > lst[j]:
            #     min_idx = j
            #     lst[i], lst[j] = lst[j], lst[i]
            # 2nd logic
            if lst[j] < lst[min_idx]:
                min_idx = j
        if i!= min_idx:
            lst[min_idx], lst[i] = lst[i], lst[min_idx]
    return lst

#num = [1,4,5,3,2]

num = [1,4,5,3,2,7,9,8]


print(selection_sort(num))