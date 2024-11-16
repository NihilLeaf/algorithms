def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        minors = [i for i in arr if i < pivot]
        majors = [i for i in arr if i > pivot]
        pivots = [i for i in arr if i == pivot]
        return quicksort(minors) + pivots + quicksort(majors)

print(quicksort([3, 3, 2, 5, 6, 7, 9, 15, 15, 27, 13]))