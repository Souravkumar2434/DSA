

def merge(lst1, lst2):
    i = 0
    j = 0
    combined = []

    while i < len(lst1)  and j < len(lst2):
        if lst1[i] < lst2[j]:
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1
    
    while i < len(lst1):
        combined.append(lst1[i])
        i += 1

    while j < len(lst2):
        combined.append(lst2[j])
        j += 1
    
    return combined


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    min_idx = int(len(lst) / 2)
    left = merge_sort(lst[:min_idx])
    right = merge_sort(lst[min_idx: ])

    return merge(left, right)


original_list = [3,2,1,7,6,5,4]

print(merge_sort(original_list))