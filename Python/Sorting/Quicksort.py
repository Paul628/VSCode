def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            
            i=i+1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            #(arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1



def quicksort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)













arr = [10, 9, 2, 4, 6, 13, 1, 3, 5, 7, 8, 11, 12]

quicksort(arr, 0, len(arr)-1)
print(arr)