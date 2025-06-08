#include <stdio.h>
#include <string.h>
#include <time.h>
#include <windows.h>

inline void GPUassert(cudaError_t code, const char *file, int line, bool Abort=true) {
    if (code != cudaSuccess) {
        fprintf(stderr, "GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
        if (Abort) exit(code);
    }
}

#define GPUerrchk(ans) { GPUassert((ans), __FILE__, __LINE__); }

__host__ __device__ void swap(char *x, char *y) {
    char temp = *x;
    *x = *y;
    *y = temp;
}

__device__ void permute_device(char *a, int i, int n, int tid, int* count) {
    if (i == n) {
        char* c = a - 1; // Points to the start of the original array
        //printf("Permutation nr. %i from thread nr. %i: %s\n", *count, tid, c);
        count[0]++;
    } 
    else {
        for (int j = i; j <= n; j++) {
            swap(a + i, a + j);
            permute_device(a, i + 1, n, tid, count);
            swap(a + i, a + j); // backtrack
        }
    }
}

__global__ void permute_kernel(char* d_A, int size, int* d_counts) {
    int tid = threadIdx.x + blockIdx.x * blockDim.x;
    int permute_length = size - 1; // Exclude null terminator
    if (tid >= permute_length) return;

    int count = 0;
    char* local_array = new char[size];

    // Copy from global to local memory
    for (int i = 0; i < size; i++) {
        local_array[i] = d_A[i];
    }

    swap(&local_array[0], &local_array[tid]);
    permute_device(local_array + 1, 0, permute_length - 2, tid, &count);
    d_counts[tid] = count; // Store each thread's count
    delete[] local_array;
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

    char h_a[] = "ABCDEFGHIJK"; // Example input
    int permute_length = strlen(h_a);
    size_t total_size = permute_length + 1; // Include null terminator

    printf("String length: %d, \n", permute_length);

    char* d_a;
    GPUerrchk(cudaMalloc((void**)&d_a, total_size));
    GPUerrchk(cudaMemcpy(d_a, h_a, total_size, cudaMemcpyHostToDevice));

    // Allocate device and host memory for counts
    int* d_counts;
    int* h_counts = (int*)malloc(permute_length * sizeof(int));
    GPUerrchk(cudaMalloc((void**)&d_counts, permute_length * sizeof(int)));

    printf("\nPermutations on GPU:\n");
    double start = clock();
    permute_kernel<<<1, permute_length>>>(d_a, total_size, d_counts);
    GPUerrchk(cudaPeekAtLastError());
    GPUerrchk(cudaDeviceSynchronize());
    double end = clock();

    // Get counts and sum them up
    GPUerrchk(cudaMemcpy(h_counts, d_counts, permute_length * sizeof(int), cudaMemcpyDeviceToHost));
    int total = 0;
    for (int i = 0; i < permute_length; i++) total += h_counts[i];
    
    printf("Total number of permutations: ");
    print_with_separator(total, '.');
    printf("\nTime taken: %f seconds\n", (end - start) / CLOCKS_PER_SEC);

    cudaFree(d_a);
    cudaFree(d_counts);
    free(h_counts);
    getchar();
    return 0;
}