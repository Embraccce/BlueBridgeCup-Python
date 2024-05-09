mod = 998244353
n,m,k = map(int,input().split())
arr = [0]+list(map(int,input().split()))
d = {i: arr[i] for i in range(1, n+1)}
del arr
for _ in range(m):
    X,Y = map(int,input().split())
    for key,value in d.items():
        d[key] += X
    d = {key: value for key, value in d.items() if value > 0}
    temp = dict()
    idx = len(d)+1
    for key,value in d.items():
        if value > k:
            d[key] = k
            for i in range(value-k):
                temp[idx] = 1
                idx+=1
    if Y != 0:
        temp[idx] = Y
    d.update(temp)
    print(sum(d.values()) % mod)

    
