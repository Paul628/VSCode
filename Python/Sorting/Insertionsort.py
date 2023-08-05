def insertionSort(arr):

    for i in range(1,len(arr)):
        k = arr[i]
        j = i - 1

        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = k



def insertionSort2(arr):
     for i in range(1,len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1







arr = [10, 9, 2, 4, 6, 13, 1, 3, 5, 7, 8, 11, 12]
insertionSort2(arr)
print(arr)