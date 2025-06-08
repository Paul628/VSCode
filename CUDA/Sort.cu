#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <algorithm>
#include <time.h>

#define N 10000000  // Number of elements to sort
#define CHUNK 1024  // Each block sorts CHUNK elements

__device__ void insertion_sort(int* data, int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = data[i];
        int j = i - 1;
        while (j >= left && data[j] > key) {
            data[j + 1] = data[j];
            j--;
        }
        data[j + 1] = key;
    }
}

__global__ void sort_chunks(int* d_arr, int n) {
    //int idx = blockIdx.x * blockDim.x;
    int idx = blockIdx.x * CHUNK;
    int left = idx;
    int right = min(idx + CHUNK - 1, n - 1);
    if (left < n) {
        insertion_sort(d_arr, left, right);
    }
}

// Host merge for two sorted subarrays
void merge(int* arr, int left, int mid, int right, int* temp) {
    int i = left, j = mid + 1, k = left;
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    for (int l = left; l <= right; l++) arr[l] = temp[l];
}

void swap (int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void randomize ( int arr[], int n )
{
    // Use a different seed value so that we don't get same
    // result each time we run this program
    srand ( time(NULL) );

    // Start from the last element and swap one by one. We don't
    // need to run for the first element that's why i > 0
    for (int i = n-1; i > 0; i--)
    {
        // Pick a random index from 0 to i
        int j = rand() % (i+1);

        // Swap arr[i] with the element at random index
        swap(&arr[i], &arr[j]);
    }
}

void print_with_separator(int num, char sep) {
    char buffer[50];
    sprintf(buffer, "%d", num); // Convert to string
    int len = strlen(buffer);
    int pos = len % 3 == 0 ? 3 : len % 3; // Position for first separator

    for (int i = 0; i < len; i++) {
        putchar(buffer[i]);
        if ((i + 1 - pos) % 3 == 0 && i != len - 1) {
            putchar(sep); // Insert separator
        }
    }
}

int main() {
    int* h_arr = (int*)malloc(N * sizeof(int));
    int* temp = (int*)malloc(N * sizeof(int));
    int n = sizeof(h_arr)/ sizeof(h_arr[0]);
    for (int i = 0; i < N; i++) h_arr[i] = i;
    randomize(h_arr, n);

    int* d_arr;
    cudaMalloc(&d_arr, N * sizeof(int));
    cudaMemcpy(d_arr, h_arr, N * sizeof(int), cudaMemcpyHostToDevice);

    int num_blocks = (N + CHUNK - 1) / CHUNK;

    printf("Sorting: ");
    print_with_separator(N, '.');
    printf(" Elements\n");
    clock_t start = clock();
    sort_chunks<<<num_blocks, 1>>>(d_arr, N);
    cudaDeviceSynchronize();
    clock_t end = clock();
    printf("GPU chunk sort time: %.2f seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    cudaMemcpy(h_arr, d_arr, N * sizeof(int), cudaMemcpyDeviceToHost);

    // Iterative merge on host
    start = clock();
    for (int size = CHUNK; size < N; size *= 2) {
        for (int left = 0; left < N; left += 2 * size) {
            int mid = std::min(left + size - 1, N - 1);
            int right = std::min(left + 2 * size - 1, N - 1);
            if (mid < right)
                merge(h_arr, left, mid, right, temp);
        }
    }
    end = clock();
    printf("Host merge time: %.2f seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    // Optional: check if sorted
    bool sorted = true;
    for (int i = 1; i < N; i++) {
        if (h_arr[i-1] > h_arr[i]) {
            sorted = false;
            break;
        }
    }
    printf("Sorted: %s\n", sorted ? "True" : "False");

    cudaFree(d_arr);
    free(h_arr);
    free(temp);
    getchar();
    return 0;
}