#include <stdio.h>
#include <cuda_runtime.h>
#include <stdlib.h>
#include <string.h>

inline void GPUassert(cudaError_t code, char * file, int line, bool Abort=true)
{
    if (code != 0) {
        fprintf(stderr, "GPUassert: %s %s %d\n", cudaGetErrorString(code),file,line);
        if (Abort) exit(code);
    }       
}

#define GPUerrchk(ans) { GPUassert((ans), __FILE__, __LINE__); }

__host__ __device__ void swap(char *x, char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

__device__ void permute_device(char *a, int l, int r, int tid, int* count, int n)
{
    if (l == r) {
        // Print the permutation
        //printf("Count: %d  Thread %d: Permutation: %s\n",*count, tid, a);
        //for (int i = 0; i < n; i++) printf("%c", a[i]);
        //printf("\n");
        (*count)++;
    } else {
        for (int i = l; i <= r; i++) {
            swap(&a[l], &a[i]);
            permute_device(a, l + 1, r, tid, count, n);
            swap(&a[l], &a[i]); // backtrack
        }
    }
}

__global__ void permute_kernel(char* d_A, int n, int* d_counts)
{
    int tid = threadIdx.x + blockIdx.x * blockDim.x;
    if (tid >= n) return;

    char* local_array = new char[n];
    for (int i = 0; i < n; i++) local_array[i] = d_A[i];
    swap(&local_array[0], &local_array[tid]);

    int count = 0;
    permute_device(local_array, 1, n - 1, tid, &count, n);

    d_counts[tid] = count; // Store each thread's count
    delete[] local_array;
}

int main()
{
    char h_a[] = "ABCDEFGHIJK"; // Give string here. TODO: Make set in the end because recurring characters reduce unique permutations
    int n = strlen(h_a); //Dynamic for string length

    printf("\nSize of string: %d\n", n);

    char* d_a;
    GPUerrchk(cudaMalloc((void**)&d_a, n * sizeof(char)));
    GPUerrchk(cudaMemcpy(d_a, h_a, n * sizeof(char), cudaMemcpyHostToDevice));

    // Allocate device and host memory for counts
    int* d_counts;
    int* h_counts = (int*)malloc(n * sizeof(int));
    GPUerrchk(cudaMalloc((void**)&d_counts, n * sizeof(int)));

    printf("\nGenerating permutations on GPU\n");
    double start = clock();
    permute_kernel<<<1, n>>>(d_a, n, d_counts);
    GPUerrchk(cudaPeekAtLastError());
    GPUerrchk(cudaDeviceSynchronize());
    double end = clock();

    // Copy counts back and sum
    GPUerrchk(cudaMemcpy(h_counts, d_counts, n * sizeof(int), cudaMemcpyDeviceToHost));
    int total = 0;
    for (int i = 0; i < n; i++) total += h_counts[i];

    cudaFree(d_a);
    cudaFree(d_counts);
    free(h_counts);

    printf("Total number of permutations: %'d\n", total);
    printf("Time taken: %f seconds\n", (end - start) / CLOCKS_PER_SEC);
    getchar();
    return 0;
}