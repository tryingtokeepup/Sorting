# TO-DO: Complete the selection_sort() function below


def swapping_helper(index_a, index_b, arr):

    # cool_dude = array
    temp = arr[index_a]
    arr[index_a] = arr[index_b]
    arr[index_b] = temp

    return arr


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if cur_index != smallest_index:
            arr = swapping_helper(smallest_index, cur_index, arr)

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # call my swap function
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # well, aggghhhhhh. i suck at variable names, so here. let's just assume that at the beginning, we are still wanting to swap.
    swap_actually_happened = True

    while swap_actually_happened:
        swap_actually_happened = False
        for i in range(0, len(arr) - 1):  # remember to minus 1 so we don't go out of bounds
            if arr[i] > arr[i+1]:
                arr = swapping_helper(i, i+1, arr)
                swap_actually_happened = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
