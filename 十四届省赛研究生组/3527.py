import math
import sys
d = [0 for i in range(100010)]
n = int(input())
arr = list(map(int,input().split()))
for i in arr:
    if i < 10**5:
        d[i] += 1
# 合成版
for i in range(1, 100002):
    if d[i] % (i+1) != 0:
        print(i)
        sys.exit()
    else:
        d[i+1] += d[i] // (i + 1)
# 合成不了，取最小即可
print(min(arr))
