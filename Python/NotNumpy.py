import time

# Create two lists
a = [i for i in range(1000000)]
b = [i for i in range(1000000)]

# Add lists element-wise
start = time.time()
c = [a[i] + b[i] for i in range(1000000)]
end = time.time()
print(f"Pure Python time: {end - start:.6f} seconds")