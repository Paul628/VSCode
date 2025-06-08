import time
from itertools import permutations
from multiprocessing import Pool, cpu_count

def recurPermute(index, s, ans):
    if index == len(s):
        ans.append("".join(s))
        return
    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]
        recurPermute(index + 1, s, ans)
        s[index], s[i] = s[i], s[index]

def permute_with_fixed_first(args):
    first, rest = args
    ans = []
    recurPermute(0, list(rest), ans)
    # Prepend the fixed character to each permutation
    return [first + perm for perm in ans]

def findPermutationParallel(s):
    tasks = []
    used = set()
    for i, c in enumerate(s):
        if c in used:
            continue  # Avoid duplicate work for repeated characters
        used.add(c)
        rest = s[:i] + s[i+1:]
        tasks.append((c, rest))
    with Pool(min(len(tasks), cpu_count())) as pool:
        results = pool.map(permute_with_fixed_first, tasks)
    # Flatten the list of lists
    perms = [item for sublist in results for item in sublist]
    perms.sort()
    return perms

if __name__ == "__main__":
    s = "ABCDEFGHIJK"
    print("Parallel anagram implementation")
    print("Size of string: ", len(s))
    start = time.time()
    res = findPermutationParallel(s)
    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")
    #print("Permutations:", res)
