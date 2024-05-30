import time
prims=list()
n=1000000
vis = [False for i in range(n+10)]
for i in range(2,n):
    if not vis[i]:
        vis[i] = True
        prims.append(i)
    j=0
    while j<len(prims) and i*prims[j]<=n:
        vis[i*prims[j]] = True
        if i % prims[j]==0:break
        j+=1
ans=0
sdef is_subsequence(s, t):
    t_iter = iter(t)
    return all(char in t_iter for char in s)
start = time.time()
for num in range(2,1000000+1):
    if num in prims:
        ans += 1
        continue
    for prime in prims:
        if prime > num:
            break
        if is_subsequence(str(prime), str(num)):
            ans += 1
            break
    if num % 10000 == 0:
        print(time.time()-start)
print(ans)
        
