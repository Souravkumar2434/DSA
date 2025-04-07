
def binary_search_op(input_array):
    left = 0
    right = len(input_array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if input_array[mid] == element_to_search:
            return mid

        elif input_array[mid] < element_to_search:
            left = mid + 1

        else:
            right = mid - 1

    return -1


input_array = [1,2,3,4,5]


# ELement in the list
element_to_search = 2

result = binary_search_op(input_array)

print(f"result: {result}")


# ELement not in the list
element_to_search = 6

result = binary_search_op(input_array)

print(f"result: {result}")


