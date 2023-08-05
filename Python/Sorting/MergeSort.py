def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        print(left)
        mergeSort(left)
        mergeSort(right)

        
        i = 0 #left
        j = 0 #right
        k = 0 #combined
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1




mergeSort(arr)
print(arr)