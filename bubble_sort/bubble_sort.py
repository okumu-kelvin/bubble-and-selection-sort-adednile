# TODO: Implement bubble sort
def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    sorted_arr = unsorted_list[:]  # Create a copy of the list

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break

    return sorted_arr
    pass
