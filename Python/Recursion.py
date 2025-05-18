#0,1,1,2,3,5,8,....
#fib_n = fib_n-1 + fib_n-2
#fib_1 = 0
#fib_2 = 1

import time

def fib(n):#simple recursive 
    if n < 2:
        return n
    return(fib(n-1) + fib(n-2))

def fibm(n, memo):#we did some thinking
    if n not in memo:
        memo[n] = fibm(n-1, memo) + fibm(n-2, memo)
    return memo[n]


def fibi(n):#why not try iterative
    i = 2
    a = 1
    b = 1
    while i<n:
        c = a + b
        a = b
        b = c
        i+=1
    return c    

start = time.time()
m = fib(40)
end = time.time()
print(m)
print("Rekursiv: %f\n" %(end-start))

memo={1:1, 2:1}

start = time.time()
m = fibm(990,memo)
end = time.time()
print(m)
print("Memo: %f\n" %(end-start))

start = time.time()
m = fibi(10000)
end = time.time()
print(m)
print("Iterativ: %f" %(end-start))