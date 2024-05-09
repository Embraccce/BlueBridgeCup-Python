from collections import Counter
mod = 998244353
n,m,k = map(int,input().split())
d = Counter(map(int, input().split()))
for _ in range(m):
    X,Y = map(int,input().split())
    d = {key+X: val % mod for key, val in d.items() if key+X>0}
    for key,val in d.copy().items():
        if key > k:
            del d[key]
            d[1] = (d.get(1, 0) + (key - k) * val) % mod
            d[k]= (d.get(k ,0) + val) % mod
    if Y != 0:
        d[Y] = (d.get(Y, 0) + 1) % mod
    print(sum((key * value) % mod for key, value in d.items()) % mod)

