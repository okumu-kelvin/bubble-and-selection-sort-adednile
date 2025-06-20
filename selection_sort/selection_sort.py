def selection_sort(arr):
    n = len(arr)
    # TODO: Implement selection sort
    sorted_arr = arr[:]

    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j
    
        if min_index != i:
            sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]

    return sorted_arr
    pass
