
import time
from unicodedata import name
from itertools import permutations

def recurPermute(index, s, ans):
    if index == len(s):
        ans.append("".join(s))
        return

    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]
        recurPermute(index + 1, s, ans)
        s[index], s[i] = s[i], s[index]


def findPermutation(s):

    # Stores the final answer
    ans = []

    recurPermute(0, list(s), ans)

    # sort the resultant list
    ans.sort()

    return ans


if __name__ == "__main__":
    s = "ABCDEFGHIJK"
    print("Python own anagram naive implementation")
    print("Size of string: ", len(s))
    #res = findPermutation(s)
    start = time.time()
    res = findPermutation(s)
    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")

    # for x in res:
    #     print(x, end=" ")

# s = "ABC"
# def recurPermute(index, s, ans):
#     if index == len(s): //3
#         ans.append("".join(s))
#         return

#     for i in range(index, len(s)):
#         s[index], s[i] = s[i], s[index]
#         recurPermute(index + 1, s, ans)
#         s[index], s[i] = s[i], s[index]