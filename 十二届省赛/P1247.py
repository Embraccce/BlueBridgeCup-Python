from functools import reduce
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if reduce(lambda x, y: x ^ y, arr):
        print("Yes")
    else:
        print("No")
