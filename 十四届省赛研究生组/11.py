prims = []
n=1000
vis = [False]*(n+1)
for i in range(2,n+1):
    if not vis[i]:
        prims.append(i)
    j=0
    while i*prims[j] <= n:
        vis[i*prims[j]]=True
        if i % prims[j] == 0:break
        j+=1
print(len(prims))
