import math
n = int(input())
def solve(n):
    k = 1
    while True:
        if math.comb(k, 2) + k >= n:
            return k
        k += 1
print(solve(n))
