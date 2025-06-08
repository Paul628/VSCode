import concurrent.futures
import random
import time
import multiprocessing
import os
import math

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        
        i = 0
        j = 0
        k = 0

        result = [0] * len(arr)
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            result[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            result[k] = right[j]
            j += 1
            k += 1
        return result
    else:
        return arr

def mergeSortParallel(arr, depth, max_depth):
    if len(arr) > 1:
        mid = len(arr) // 2
        if depth < max_depth:
            with concurrent.futures.ProcessPoolExecutor() as executor:
                # Submit tasks to the executor for parallel processing
                # Use the depth to limit the number of parallel processes
                left_future = executor.submit(mergeSortParallel, arr[:mid], depth+1, max_depth)
                right_future = executor.submit(mergeSortParallel, arr[mid:], depth+1, max_depth)
                left = left_future.result()
                right = right_future.result()
        else:
            # Fallback to single-threaded merge sort if max depth is reached
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
        
        i = 0
        j = 0
        k = 0
        result = [0] * len(arr)
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            result[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            result[k] = right[j]
            j += 1
            k += 1
        return result
    else:
        return arr

if __name__ == "__main__":
    n = 10_000_000
    # get amount of logical cores and divide by 2 to get the amount of physical cores
    # we use it to limit the amount of parallel processes to their respective cores to make it more efficient  
    # and avoid overloading the CPU
    max_depth = math.log2(os.cpu_count()/2) 
    arr = list(range(n))
    # shuffle the array to make it unsorted
    random.shuffle(arr)

    arr_parallel = arr.copy()
    arr_buildin = arr.copy()

    print("Single-threaded mergesort:")
    start = time.time()
    sorted_single = mergeSort(arr)
    end = time.time()
    print(f"Single-threaded time: {end - start:.2f} seconds\n")

    print("Parallel mergesort:")
    start = time.time()
    sorted_parallel = mergeSortParallel(arr_parallel, 0 , max_depth)
    end = time.time()
    print(f"Parallel time: {end - start:.2f} seconds\n")

    print("Buildin sort...")
    start = time.time()
    sorted_parallel = sorted(arr_buildin)
    end = time.time()
    print(f"Buildin time: {end - start:.2f} seconds")




    #print("Results equal:", sorted_single == sorted_parallel)