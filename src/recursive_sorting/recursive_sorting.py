# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(left, right):
    # we start with 0 and 0 on both side, because we want the left index
    merged_array = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1
    # append all indicies right of left index
    merged_array.extend(left[left_index:])
    # append all indicies right of right index
    merged_array.extend(right[right_index:])

    return merged_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    midpoint = len(arr) // 2

    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    return merge(left, right)

#     def merge(left, right):
#     result = []
#     left_index = right_index = 0
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1
#     result.extend(left[left_index:])
#     result.extend(right[right_index:])
#     return result
# # TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort(arr):
#     # edge case
#     if len(arr) < 2:
#         return arr
#     # TO-DO
#     # divide
#     middle = len(arr) // 2
#     left = merge_sort(arr[:middle])
#     right = merge_sort(arr[middle:])
#     # conquer
#     return merge(left, right)














# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def tim_insertion(arr, left, right):

    for i in range(left + 1, right+1):

        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= left:

            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

# merge function merges the sorted runs
def tim_merge(arr, l, m, r):

    len1, len2 =  m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len1:

        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def tim_sort(arr, length):
    RUN = 32
    for i in range(0, length, RUN):
        tim_insertion(arr, i, min((i+31), (length-1)))

    size = RUN
    while size < length:

        for left in range(0, length, 2*size):

            mid = left + size - 1
            right = min((left + 2*size - 1), (length-1))

            tim_merge(arr, left, mid, right)

        size = 2*size

    return arr
