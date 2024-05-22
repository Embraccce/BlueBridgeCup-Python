n,m,a,b=map(int,input().split())
arr = [[0]*(m+1)]
mod = 998244353
for _ in range(n):
    arr.append([0]+list(map(int,input().split())))
tot = 0
for x in range(1,n-a+2):
    for y in range(1,m-b+2):
        tot += (max(max(row[y:y+b]) for row in arr[x:x+a]) * min(min(row[y:y+b]) for row in arr[x:x+a])) % mod
print(tot % mod)
