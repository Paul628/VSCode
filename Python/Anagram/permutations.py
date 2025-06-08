from itertools import permutations
import time


if __name__ == "__main__":
    s = "ABCDEFGHIJK"
    print("Python itertools anagram implementation")
    print("Size of string: ", len(s))
    start = time.time()
    perms = [''.join(p) for p in permutations(s)]
    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")