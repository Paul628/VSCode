# GCD(20,10)
# Ergebnis=
import time
import timeit

ITER = 100000000

def gcdi(x,y):
    while y!=0:
        rem = y
        y = x%y
        x = rem
    return x

    
def gcdr(a, b):
    if b == 0:
        return a
    else:
        return gcdr(b, a % b)


start_time = time.time()
for i in range(ITER):
    gcdi(32769,77)
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time, "seconds")

start_time = timeit.default_timer()
for i in range(ITER):
    gcdi(32769,77)
print(timeit.default_timer() - start_time)


start_time = time.time()
for i in range(ITER):
    gcdr(32767,77)
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time, "seconds")

start_time = timeit.default_timer()
for i in range(ITER):
    gcdr(32767,77)
print(timeit.default_timer() - start_time)