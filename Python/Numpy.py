import numpy as np
import time

# Create two NumPy arrays
a = np.arange(1000000)
b = np.arange(1000000)

# Add arrays element-wise
start = time.time()
c = a + b
end = time.time()
print(f"NumPy time: {end - start:.6f} seconds")