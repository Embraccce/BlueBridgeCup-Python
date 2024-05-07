import math
n = 2021041820210418
arr = []
for i in range(1, int(math.sqrt(n)+1)):
    if n % i ==0:
        arr.append(i)
        arr.append(n//i)
#arr.sort()

ans = 0
for l in arr:
    for w in arr:
        for h in arr:
            if l*w*h == n:
                ans += 1
print(ans)
